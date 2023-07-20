from pytube import YouTube
import cv2
video_url = "https://www.youtube.com/watch?v=pY8oa8XS3ko"  
# Choose a video stream with resolution of 360p
streams = YouTube(video_url).streams.filter(adaptive=True, subtype="mp4", resolution="480p", only_video=True)

# Check if there is a valid stream
if len(streams) == 0:
  raise "No suitable stream found for this YouTube video!"

# Download the video as video.mp4
print("Downloading...")
vid_path = streams[0].download(filename="video.mp4")
print("Download completed.")

vid = cv2.VideoCapture(vid_path)

while True:
  ret, img = vid.read()
  if not ret:
    break
  
  cv2.imshow("a", img)
  cv2.waitKey(1)

