# importing packages
# pytube could be installed from pip
from pytube import YouTube
import os
import subprocess
  
# url input from user
yt = YouTube(
  str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.get_audio_only()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'

default_filename = base + ext

print(new_file)
print(default_filename)
subprocess.run([
    'ffmpeg',
    '-i', default_filename,
    new_file
])

# remove mp4 format
os.remove(default_filename)
  
# result of success
print(yt.title + " has been successfully downloaded.")
