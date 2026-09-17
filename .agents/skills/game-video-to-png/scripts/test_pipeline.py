"""Runnable synthetic integration test; no network or source assets required."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw
from process import detect, selected

script = Path(__file__).with_name('process.py')

def cli(*args, ok=True):
    result = subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True)
    assert (result.returncode == 0) == ok, result.stdout + result.stderr


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    for tag, bg in [('green', (0,255,0)), ('purple', (192,64,255))]:
        src = root/tag; src.mkdir()
        for n in range(1, 9):
            im = Image.new('RGB', (96,96), bg)
            ImageDraw.Draw(im).rectangle((28+n,25,60+n,70), fill=(230,100,50))
            im.save(src/f'{n:04d}.png')
        video = root/f'{tag}.mp4'
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-loglevel', 'error', '-framerate', '8', '-i', str(src/'%04d.png'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', str(video)], check=True)
        job = root/f'{tag}-job'
        cli('process', '--video', video, '--out', job)
        meta = json.loads((job/'job.json').read_text())
        assert meta['frame_count'] == 8 and meta['fps'] == 8
        assert meta['status'] == 'NEEDS_HUMAN_REVIEW'
        a = np.asarray(Image.open(job/'frames/eff_hero_0001.png'))
        assert a[0,0,3] == 0 and a[40,45,3] == 255
        assert np.max(np.abs(a[40,45,:3].astype(int)-[230,100,50])) < 15
        assert len(zipfile.ZipFile(job/'frames.zip').namelist()) == 8
        before = {p.name:digest(p) for p in (job/'frames').glob('*.png')}
        rev = root/f'{tag}-rev'
        cli('repair', '--job', job, '--out', rev, '--frames', '2-3', '--similarity', '.08', '--decontaminate')
        assert before == {p.name:digest(p) for p in (job/'frames').glob('*.png')}
        for n in [1,4,5,6,7,8]:
            name = f'eff_hero_{n:04d}.png'
            assert digest(job/'frames'/name) == digest(rev/'frames'/name)
        mask = Image.new('L', (96,96), 0)
        ImageDraw.Draw(mask).rectangle((40,40,45,45), fill=255)
        mask.save(root/'mask.png')
        damaged_path = rev/'frames/eff_hero_0002.png'
        damaged = np.array(Image.open(damaged_path))
        damaged[40:46,40:46,3] = 0
        Image.fromarray(damaged).save(damaged_path)
        cli('repair', '--job', rev, '--out', root/f'{tag}-mask', '--frames', '2', '--restore-mask', root/'mask.png')
        restored = np.asarray(Image.open(root/f'{tag}-mask'/'frames/eff_hero_0002.png'))
        original = np.asarray(Image.open(rev/'source/eff_hero_0002.png').convert('RGB'))
        assert restored[42,42,3] == 255 and np.array_equal(restored[42,42,:3], original[42,42])
        cli('process', '--video', video, '--out', job, ok=False)
        cli('repair', '--job', job, '--out', job/'nested', '--frames', '1', '--blend', '.1', ok=False)
        cli('repair', '--job', job, '--out', root/'invalid', '--frames', '0-2', '--blend', '.1', ok=False)
    assert selected('1,3-4', 4) == [1,3,4]
    noisy = root/'noise.png'
    Image.fromarray(np.random.default_rng(3).integers(0,256,(96,96,3), dtype=np.uint8)).save(noisy)
    try:
        detect([noisy])
        raise AssertionError('Uncertain background accepted')
    except ValueError:
        pass
print('PASS: two MP4 colors, RGBA, numbering, revision isolation, restore mask, ZIP, validation guards')
