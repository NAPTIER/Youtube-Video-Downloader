from pytube import YouTube
print("--------------Welcome to free YouTube video downloader---------------")
link=input("Copy and Paste URL of the video you want to download--")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()
print("Video downloaded sucessfully")
print("-----------Thank You for using our services--------------")