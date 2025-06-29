"""
This script downloads the absolute best viodeo stream and audio stream from a YouTube video URL.
Then merges them into a single file using ffmpeg.
"""
import os
import re
from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress
from sanitize import sanitize_filename


def download_absolute_best(url: str):
    video = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)
    video_title = sanitize_filename(video.title)
    video_stream = video.streams.filter(adaptive=True).order_by('resolution').desc().first()
    audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
    video_stream.download(filename=f"{video_title}_video.mp4")
    audio_stream.download(filename=f"{video_title}_audio.mp4")
    os.system(f'ffmpeg -i "{video_title}_video.mp4" -i "{video_title}_audio.mp4" -c:v copy -c:a aac "{video_title}_final.mp4"')
    os.remove(f"{video_title}_video.mp4")
    os.remove(f"{video_title}_audio.mp4")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    if not url:
        print("Please enter a valid YouTube URL.")
    else:
        download_absolute_best(url)
        print("Download completed and merged into a single file.")
