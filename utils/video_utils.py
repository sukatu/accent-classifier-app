import requests
import tempfile
from moviepy import VideoFileClip

def extract_audio_from_url(video_url):
    response = requests.get(video_url, stream=True)
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    with open(temp_video.name, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    clip = VideoFileClip(temp_video.name)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    clip.audio.write_audiofile(temp_audio.name)
    return temp_audio.name
