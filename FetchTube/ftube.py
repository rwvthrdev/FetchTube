#rwvthrdev. ♞ .20260428

#Imports
import os
import sys
import subprocess

#Checa a presença do pytubefix e instala caso não esteja presente.
try:
    import pytubefix
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytubefix"])


from pytubefix import YouTube
from pytubefix.cli import on_progress

print("\033[91m" + "=" * 50 + "\033[0m")
url = str(input("Type a video URL: "))
print("\033[91m" + "=" * 50 + "\033[0m")

yt = YouTube(url, on_progress_callback=on_progress)

print("\033[91m" + "=" * 50 + "\033[0m")
print(f'Title of video: {yt.title}')
print(f'Author: {yt.author}')
print("\033[91m" + "=" * 50 + "\033[0m")

ys = yt.streams.get_highest_resolution()

ys.download()



