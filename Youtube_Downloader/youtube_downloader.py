from pytube import YouTube
import os

video_url=input("Enter YT video url: ")

youtube=YouTube(video_url)

video_stream = youtube.streams.get_highest_resolution()

output_directory = input("Enter the directory to save the downloaded video: ")
os.makedirs(output_directory, exist_ok=True)

video_stream.download(output_path=output_directory)

downloaded_video_path = os.path.join(output_directory, video_stream.default_filename)

print("Video downloaded successfully.")
print(f"Title: {youtube.title}")
print(f"Views: {youtube.views}")
print(f"Downloaded Video Path: {downloaded_video_path}")