from download_preference import *
from selection_validation import validate_selection_input
from exception_handler_core import video_link_exception_validate
from yt_dlp import YoutubeDL
from clint.textui import colored
from typing import Any, Union

# from debugger import logger_func


def on_complete_again_download_or_not() -> None:
    user_selection_input: str = input("Do you want to download another video? (y/n) ")

    choose_wanna_download_another_video = validate_selection_input(user_selection_input)

    if choose_wanna_download_another_video:
        video_processor: Union[list[Any], bool] = video_link_exception_validate()

        if video_processor:
            video_ux_func(video_processor)
    else:
        exit()


def video_downloader_func(url: str):
    user_selection_input = input(
        "Do you want to download subtile (english only)? (y/n) "
    )
    subtile_yes_or_not: bool = validate_selection_input(user_selection_input)

    if subtile_yes_or_not:
        ydl_opts = video_with_subtitle()
    else:
        ydl_opts = video_without_subtitle()

    with YoutubeDL(ydl_opts) as ydl:
        print(colored.yellow("\nDownloading..."))
        ydl.download(url)
        print(colored.cyan("Download complete\n"))
        on_complete_again_download_or_not()


def video_ux_func(video_obj_info_url):

    print("\n")
    for key, value in video_obj_info_url[1].items():
        print(colored.green(key + ":"), value)

    user_selection_input: str = input(
        "Do you want to see the video description? (y/n) "
    )
    catch_description_choice: bool = validate_selection_input(user_selection_input)

    if catch_description_choice:
        print("\n")
        print(video_obj_info_url[0].description)
        print("\n")

    user_selection_input = input("Do you want to download the video? (y/n) ")
    catch_download_choice: bool = validate_selection_input(user_selection_input)
    if catch_download_choice:
        video_downloader_func(video_obj_info_url[2])
    else:
        return False


# return is received by selection_menu (cydl.py)
