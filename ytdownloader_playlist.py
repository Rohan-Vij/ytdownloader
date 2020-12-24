from pytube import Playlist
import os
import shutil
import sys

url = 'https://www.youtube.com/playlist?list=PLcCNDZnq0ur1VstEQEbi6rIE1eg0QlGnl'

# Create playlist object with the video URL as a paramater
video_object = Playlist(url)
ptitle = video_object.title

print(video_object.video_urls)

# Create a directory for the playlist
# If one already exists, ask the user if they want delete the directory and redownload the playlist 
try:
    os.mkdir(ptitle)
except WindowsError:
    while True:
        redownload = input("A directory for this playlist already exists. Do you want to delete it and redownload the playlist? (y/n): ")
        if redownload == "y":
            shutil.rmtree(ptitle)
            os.mkdir(ptitle)
            break
        elif redownload == "n":
            print("Program ended prematurely.")
            sys.exit()
        else:
            print("Invalid selection. Enter either \"y\" or \"n\"!")

# Changing to the directory of the playlist
os.chdir(ptitle)

# Looping through each video and downloading them
enum = 0
for video in video_object.videos: 
    print("E")
    available_streams = video.streams.filter(progressive=True).order_by('resolution').desc()
    highest_quality = available_streams.first()

    print(f"Downloading video {enum}... ", end="")
    highest_quality.download()
    print("Done!")

    enum += 1










