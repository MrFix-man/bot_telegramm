import os
from pytube import YouTube


def download(video_url):
    yt = YouTube(video_url, use_oauth=True)
    video = yt.streams.filter(only_audio=True).first()

    destination = 'Download audio'

    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file
