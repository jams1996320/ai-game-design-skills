"""Create an isolated user runtime; never alter system PATH or global packages."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import venv

p = argparse.ArgumentParser()
p.add_argument('--root', type=Path, default=Path(os.environ.get('LOCALAPPDATA', Path.home() / '.local/share')) / 'game-video-to-png' / 'runtime-v1')
a = p.parse_args()
if sys.version_info < (3, 9):
    raise SystemExit('Python 3.9+ required (3.12 recommended).')
python = a.root / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
if not python.exists():
    venv.EnvBuilder(with_pip=True).create(a.root)
subprocess.run([str(python), '-m', 'pip', 'install', '--only-binary=:all:', '-r', str(Path(__file__).with_name('requirements.txt'))], check=True)
subprocess.run([str(python), '-c', 'import cv2, numpy, PIL, imageio_ffmpeg, subprocess; subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-version"], check=True, stdout=subprocess.DEVNULL)'], check=True)
print(json.dumps({'python': str(python.absolute()), 'status': 'ready'}))
