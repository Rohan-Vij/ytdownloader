from pytube import YouTube
import os

url = 'https://youtube.com/watch?v=eaEMSKzqGAg'

# Create object with the video URL as a paramater
video_object = YouTube(url)  

# Getting streams from the selected video (from highest to lowest bitrate)
# Declaring that we only want audio streams
available_streams = video_object.streams.filter(only_audio=True).order_by('abr').desc()

# Getting the highest quality stream (normally a webm)
highest_quality = available_streams.first()

print("Highest quality progressive stream found:", highest_quality)

# Changing current program directory to the "downloaded" directory
os.chdir("downloaded")

# Downloading video (as a webm file)
print("Downloading audio file... ", end="")
highest_quality.download()
print("Done!")









