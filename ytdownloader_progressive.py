from pytube import YouTube
import os

url = 'https://youtube.com/watch?v=kXShLPXfWZA'

# Create object with the video URL as a paramater
video_object = YouTube(url)  

# Getting streams from the selected video (from highest to lowest res)
# By declaring that we want only progressive streams, we can download the video and audio in one file
# But the highest resolution we can download will be 720p
# We can also download the audio and video separately by viewing the DASH streams (and therefore get 1080p)
# To do this, replace progressive with adapative:
# available_streams = video_object.streams.filter(adapative=True)
# However, we will have to later combine the video and audio streams using post-processing
available_streams = video_object.streams.filter(progressive=True).order_by('resolution').desc()

# Getting the highest quality stream
highest_quality = available_streams.first()

print("Highest quality progressive stream found:", highest_quality)

# Changing current program directory to the downloaded directory
os.chdir("downloaded")

# Downloading video
print("Downloading...", end="")
highest_quality.download()
print("Done!")









