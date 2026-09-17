"""Local solid-background keying. All jobs/revisions are new directories."""
import argparse
import os
import json
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

import cv2
import imageio_ffmpeg
import numpy as np
from PIL import Image


def run(args):
    subprocess.run([str(x) for x in args], check=True)


def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def color(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise argparse.ArgumentTypeError('Color must be #RRGGBB')
    return value.upper()


def detect(paths):
    samples = []
    for i in np.unique(np.linspace(0, len(paths)-1, min(9, len(paths))).astype(int)):
        a = np.asarray(Image.open(paths[i]).convert('RGB'))
        edge = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
        samples.append(edge[::max(1, len(edge)//2000)])
    pixels = np.concatenate(samples)
    bins, counts = np.unique(pixels // 16, axis=0, return_counts=True)
    dominant = bins[counts.argmax()]
    near = np.max(np.abs(pixels.astype(int) - (dominant.astype(int)*16+8)), axis=1) < 28
    rgb = np.median(pixels[near], axis=0).astype(int)
    # ponytail: border-color heuristic; use explicit color/segmentation if subjects cover edges.
    confidence = min(float(np.mean(np.max(np.abs(s.astype(int)-rgb), axis=1) < 35)) for s in samples)
    if confidence < .65:
        raise ValueError('Background detection uncertain. Inspect source frames and rerun with --color; do not blindly increase similarity.')
    return '#' + ''.join(f'{v:02X}' for v in rgb), confidence


def selected(value, count):
    result = set()
    for part in value.split(','):
        if not re.fullmatch(r'\d+(?:-\d+)?', part):
            raise ValueError('Frames must look like 20-30,78')
        limits = [int(x) for x in part.split('-')]
        lo, hi = limits[0], limits[-1]
        if not 1 <= lo <= hi <= count:
            raise ValueError('Frame range out of bounds')
        result.update(range(lo, hi+1))
    return sorted(result)


def key(ffmpeg, source, target, bg, similarity, blend):
    run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-nostdin', '-n', '-i', source,
         '-vf', f'format=rgba,colorkey=0x{bg[1:]}:{similarity}:{blend}',
         '-frames:v', '1', '-pix_fmt', 'rgba', target])


def finish(job, meta):
    frames = sorted((job/'frames').glob('*.png'))
    source = sorted((job/'source').glob('*.png'))
    if len(frames) != len(source) or not frames:
        raise ValueError('Source/output frame count mismatch')
    warnings = []
    areas = []
    for n, path in enumerate(frames, 1):
        if path.name != f"{meta['prefix']}_{n:04d}.png":
            raise ValueError('Non-contiguous numbering')
        with Image.open(path) as im:
            if im.mode != 'RGBA' or list(im.size) != meta['size']:
                raise ValueError('Invalid RGBA format or canvas size')
            alpha = np.asarray(im)[:, :, 3]
            area = float(np.mean(alpha > 127))
            areas.append(area)
            if alpha.max() == 0 or alpha.min() == 255:
                warnings.append({'frame': n, 'reason': 'empty_or_no_transparency'})
    for i in range(1, len(areas)):
        if abs(areas[i]-areas[i-1]) > .15:
            warnings.append({'frame': i+1, 'reason': 'foreground_area_jump_review_only'})
    meta.update(frame_count=len(frames), status='NEEDS_HUMAN_REVIEW', warnings=warnings)
    save_json(job/'job.json', meta)
    files = [p.name for p in frames]
    page = '''<!doctype html><meta charset="utf-8"><title>序列帧审核</title>
<style>body{font:16px system-ui;margin:24px;background:#eee;color:#222}canvas{max-width:46vw;height:auto;border:1px solid #999;background:repeating-conic-gradient(#ddd 0% 25%,#fff 0% 50%) 0/24px 24px}button,select,input{font:inherit;margin:6px}textarea{display:block;width:90%;height:90px}</style>
<h1>透明序列帧审核</h1><p>左侧原始帧，右侧透明结果。暂停后标记问题帧；可直接向 Codex 报告帧号和原因。当前结果尚未人工验收。</p>
<button id="play">播放 / 暂停</button><button id="prev">上一帧</button><button id="next">下一帧</button>
<label>背景<select id="bg"><option value="">棋盘格</option><option value="#000">黑</option><option value="#fff">白</option><option value="#808080">灰</option></select></label>
<label>帧<input id="seek" type="range" min="1"></label><strong id="label"></strong><br>
<canvas id="original"></canvas> <canvas id="result"></canvas><br>
<button id="mark">标记当前帧</button><button id="download">下载审核记录</button><textarea id="notes" aria-label="问题帧和说明" placeholder="例如：35-42 衣服缺失；78 紫边"></textarea>
<script>const files=FILES,fps=FPS;let index=0,playing=false,token=0;const by=id=>document.getElementById(id);by('seek').max=files.length;
function draw(){const t=++token;by('seek').value=index+1;by('label').textContent=`${index+1} / ${files.length}`;for(const [id,dir] of [['original','source'],['result','frames']]){const im=new Image();im.onload=()=>{if(t!==token)return;const c=by(id);c.width=im.width;c.height=im.height;const x=c.getContext('2d');x.clearRect(0,0,c.width,c.height);if(id==='result'&&by('bg').value){x.fillStyle=by('bg').value;x.fillRect(0,0,c.width,c.height)}x.drawImage(im,0,0)};im.src=dir+'/'+files[index]}}
by('play').onclick=()=>playing=!playing;by('prev').onclick=()=>{playing=false;index=(index+files.length-1)%files.length;draw()};by('next').onclick=()=>{playing=false;index=(index+1)%files.length;draw()};by('seek').oninput=()=>{playing=false;index=Number(by('seek').value)-1;draw()};by('bg').onchange=draw;by('mark').onclick=()=>{playing=false;by('notes').value+=(index+1)+'：\\n'};
by('download').onclick=()=>{const u=URL.createObjectURL(new Blob([JSON.stringify({notes:by('notes').value},null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=u;a.download='review.json';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)};
setInterval(()=>{if(playing){index=(index+1)%files.length;draw()}},1000/fps);draw();</script>'''
    (job/'review.html').write_text(page.replace('FILES', json.dumps(files)).replace('FPS', str(meta['fps'])), encoding='utf-8')
    with zipfile.ZipFile(job/'frames.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for path in frames:
            z.write(path, 'frames/'+path.name)
    print(json.dumps({'job': str(job), 'frames': len(frames), 'warnings': len(warnings), 'status': meta['status']}))


def process(a):
    video = a.video.resolve()
    if not video.is_file():
        raise ValueError('Input video does not exist')
    job = a.out.resolve()
    job.mkdir(parents=True, exist_ok=False)
    (job/'source').mkdir(); (job/'frames').mkdir()
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise ValueError('Cannot decode input video')
    fps = a.fps if a.fps is not None else cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    if not np.isfinite(fps) or not 0 < fps <= 240:
        raise ValueError('Invalid frame rate; specify --fps')
    ffmpeg = os.environ.get('IMAGEIO_FFMPEG_EXE') or shutil.which('ffmpeg') or imageio_ffmpeg.get_ffmpeg_exe()
    run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-nostdin', '-n', '-i', video,
         '-vf', f'fps={fps}', '-start_number', '1', job/'source'/f'{a.prefix}_%04d.png'])
    paths = sorted((job/'source').glob('*.png'))
    if not 1 <= len(paths) <= 9999:
        raise ValueError('Expected 1..9999 frames for four-digit naming; shorten input')
    bg, confidence = (a.color, None) if a.color else detect(paths)
    save_json(job/'detection.json', {'color': bg, 'border_confidence': confidence})
    run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-nostdin', '-n', '-framerate', str(fps),
         '-start_number', '1', '-i', job/'source'/f'{a.prefix}_%04d.png',
         '-vf', f'format=rgba,colorkey=0x{bg[1:]}:{a.similarity}:{a.blend}',
         '-pix_fmt', 'rgba', '-start_number', '1', job/'frames'/f'{a.prefix}_%04d.png'])
    finish(job, {'version': 1, 'source_video': str(video), 'fps': fps, 'prefix': a.prefix,
                 'size': list(Image.open(paths[0]).size), 'color': bg,
                 'similarity': a.similarity, 'blend': a.blend,
                 'timing': 'CFR resampled; no automatic trimming or per-frame cropping'})


def repair(a):
    old = a.job.resolve(); out = a.out.resolve()
    if old == out or old in out.parents or out in old.parents:
        raise ValueError('Revision must be a separate sibling directory')
    meta = json.loads((old/'job.json').read_text(encoding='utf-8'))
    numbers = selected(a.frames, meta['frame_count'])
    if out.exists():
        raise ValueError('Output already exists')
    if a.restore_mask and (not a.restore_mask.is_file()):
        raise ValueError('Restore mask missing')
    mask = None
    if a.restore_mask:
        mask = np.asarray(Image.open(a.restore_mask).convert('L'), dtype=float)/255
        if mask.shape != (meta['size'][1], meta['size'][0]):
            raise ValueError('Restore mask must match original canvas')
    shutil.copytree(old, out)
    bg = a.color or meta['color']
    sim = a.similarity if a.similarity is not None else meta['similarity']
    blend = a.blend if a.blend is not None else meta['blend']
    ffmpeg = os.environ.get('IMAGEIO_FFMPEG_EXE') or shutil.which('ffmpeg') or imageio_ffmpeg.get_ffmpeg_exe()
    for n in numbers:
        name = f"{meta['prefix']}_{n:04d}.png"
        src, dst = out/'source'/name, out/'frames'/name
        if a.color or a.similarity is not None or a.blend is not None:
            dst.unlink()
            key(ffmpeg, src, dst, bg, sim, blend)
        rgba = np.array(Image.open(dst).convert('RGBA'))
        if mask is not None:
            original = np.asarray(Image.open(src).convert('RGB'))
            rgba[:, :, :3] = np.rint(original*mask[..., None]+rgba[:, :, :3]*(1-mask[..., None])).astype('uint8')
            rgba[:, :, 3] = np.maximum(rgba[:, :, 3], np.rint(mask*255).astype('uint8'))
        if a.decontaminate:
            alpha = rgba[:, :, 3:4].astype(float)/255
            background = np.array([int(bg[i:i+2], 16) for i in (1,3,5)])
            original = np.asarray(Image.open(src).convert('RGB'), dtype=float)
            # ponytail: known-background unmix assumes accurate alpha; inspect before accepting.
            fixed = np.clip((original-(1-alpha)*background)/np.maximum(alpha, .1), 0, 255)
            edge = (alpha[:, :, 0] >= .1) & (alpha[:, :, 0] < .99)
            rgba[edge, :3] = np.rint(fixed[edge]).astype('uint8')
        Image.fromarray(rgba, 'RGBA').save(dst)
    meta.setdefault('repairs', []).append({'frames': a.frames, 'color': bg, 'similarity': sim,
        'blend': blend, 'decontaminate': a.decontaminate, 'restore_mask': str(a.restore_mask) if a.restore_mask else None})
    finish(out, meta)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    first = sub.add_parser('process')
    first.add_argument('--video', type=Path, required=True)
    first.add_argument('--prefix', default='eff_hero')
    first.add_argument('--fps', type=float)
    rev = sub.add_parser('repair')
    rev.add_argument('--job', type=Path, required=True)
    rev.add_argument('--frames', required=True)
    rev.add_argument('--restore-mask', type=Path)
    rev.add_argument('--decontaminate', action='store_true')
    for parser in (first, rev):
        parser.add_argument('--out', type=Path, required=True)
        parser.add_argument('--color', type=color)
        parser.add_argument('--similarity', type=float, default=.12 if parser is first else None)
        parser.add_argument('--blend', type=float, default=.08 if parser is first else None)
    a = p.parse_args()
    if a.command == 'process' and not re.fullmatch('[A-Za-z0-9_-]+', a.prefix):
        p.error('Prefix must contain only letters, numbers, underscore or hyphen')
    for keyname in ('similarity', 'blend'):
        value = getattr(a, keyname)
        if value is not None and not (.01 <= value <= 1 if keyname == 'similarity' else 0 <= value <= 1):
            p.error('similarity must be .01..1; blend must be 0..1')
    if a.command == 'repair' and not any([a.color, a.similarity is not None, a.blend is not None, a.restore_mask, a.decontaminate]):
        p.error('Choose a repair operation')
    try:
        (process if a.command == 'process' else repair)(a)
    except (ValueError, OSError, subprocess.CalledProcessError) as e:
        raise SystemExit(str(e))


if __name__ == '__main__':
    main()
