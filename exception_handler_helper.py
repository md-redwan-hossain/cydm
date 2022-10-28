import typing
from pytube import YouTube, exceptions
from clint.textui import colored
from time_converter import *
from typing import Any, Union


def error_message(error_type) -> None:
    print(colored.red("Error! " + error_type))


def video_exception_handler(url: str) -> Union[list[Any], bool]:
    vid_live: bool = False
    obj_retrive_failed: bool = False
    vid_age_restricted: bool = False

    try:
        single_video_obj: YouTube = YouTube(url)
        video_info: dict = {
            "Title": str(single_video_obj.title),
            "Channel Name": str(single_video_obj.author),
            "Duration": str(convert_sec_to_readable(single_video_obj.length)),
        }

        if video_info["Duration"] == "0:00:00":
            vid_live = True
            error_message("The video is a live strean.")

        elif video_info["Title"] == "age restricted":
            vid_age_restricted = True
            error_message("The video is age restricted.")

        elif not single_video_obj:
            obj_retrive_failed = True

    except exceptions.RegexMatchError:
        error_message("Invalid video link.")

    except exceptions.VideoPrivate:
        error_message("The video is private.")

    except exceptions.MaxRetriesExceeded:
        error_message("Maximum number of retries exceeded.")

    except exceptions.VideoRegionBlocked:
        error_message("The video is region blocked.")

    except exceptions.VideoUnavailable:
        error_message("Unknown error")

    else:
        if not True in (vid_live, obj_retrive_failed, vid_age_restricted):
            video_obj_info_url: list[Any] = [single_video_obj, video_info, url]
            return video_obj_info_url

    return False
