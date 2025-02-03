import os
from yt_dlp import YoutubeDL

downloads_path = '/path/to/download/folder'  # Make sure to update this to the desired directory

def get_ydl_opts(format):
    """Returns yt-dlp options for extracting audio in the desired format."""
    return {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '320'
        }],
        'ffmpeg_location': '/path/to/ffmpeg'  # Set path to ffmpeg if necessary
    }

def download_from_url(url, format):
    """Downloads audio from a YouTube URL."""
    ydl_opts = get_ydl_opts(format)
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info_dict)
        base, ext = os.path.splitext(file_path)
        file_path = base + f'.{format}'
        title = info_dict.get('title', 'output')
        size = os.path.getsize(file_path)
        file_type = format.upper()
        return file_path, title, size, file_type
