from datetime import datetime
from pytube import YouTube


def create_error_log(video_url: str) -> None:
    try:
        video_title = YouTube(video_url).title
    except:
        video_title = "Failed to retrive video name!"
    date = datetime.now()
    with open("failed_download.log", "a") as error_msg:
        error_msg.write(date.strftime("[%d-%m-%Y %I:%M:%S %p]\n"))
        error_msg.write(f"{video_title}\n")
        error_msg.write(f"{video_url}\n\n")
