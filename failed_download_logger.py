from datetime import datetime


def create_error_log(video_title: str, video_url: str) -> None:
    date = datetime.now()
    with open("failed_download.log", "a") as error_msg:
        error_msg.write(date.strftime("[%d-%m-%Y %I:%M:%S %p]\n"))
        error_msg.write(f"{video_title}\n")
        error_msg.write(f"{video_url}\n\n")
