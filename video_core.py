from exception_handler_core import video_link_exception_validate
from selection_validation import validate_selection_input
from clint.textui import colored
from typing import Any, Union
from yt_dlp import YoutubeDL
import download_preference


def on_complete_again_download_or_not() -> None:

    print(colored.yellow("Do you want to download another video? "))

    choose_wanna_download_another_video = validate_selection_input()

    if choose_wanna_download_another_video:
        video_processor: Union[list[Any],
                               bool] = video_link_exception_validate()

        if video_processor:
            video_ux_func(video_processor)
    else:
        print(colored.yellow("Bye!"))
        exit()


def video_downloader_func(url: str):
    print(colored.yellow("\nDo you want to download subtile (english only)?"))
    subtile_yes_or_not: bool = validate_selection_input()

    if subtile_yes_or_not:
        ydl_opts = download_preference.video_with_subtitle()
    else:
        ydl_opts = download_preference.video_without_subtitle()

    with YoutubeDL(ydl_opts) as ydl:
        print(colored.yellow("\nDownloading..."))

        try:
            ydl.download(url)
        except KeyboardInterrupt:
            print(colored.red("\nDownload forcefully stopped\n"))
            on_complete_again_download_or_not()
        except:
            print(colored.red("Download failed\n"))
        else:
            print(colored.cyan("Download complete\n"))
            on_complete_again_download_or_not()


def video_ux_func(video_obj_info_url) -> Union[bool, None]:

    print("\n")
    for key, value in video_obj_info_url[1].items():
        print(colored.green(key + ":"), value)

    print(colored.yellow("\nDo you want to see the video description?"))
    catch_description_choice: bool = validate_selection_input()
    if catch_description_choice:
        print("\n")
        print(video_obj_info_url[0].description)
        print("\n")

    print(colored.yellow("\nDo you want to download the video? "))
    catch_download_choice: bool = validate_selection_input()
    if catch_download_choice:
        video_downloader_func(video_obj_info_url[2])
    else:
        return False
    return True


# return is received by selection_menu (cydl.py)
