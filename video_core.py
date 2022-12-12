from selection_validation import validate_selection_input
from clint.textui import colored
from datetime import datetime
from yt_dlp import YoutubeDL
import download_preference


def video_downloader_func(video_name: str, url: str):
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

        except:
            print(colored.red("Download failed."))
            print(colored.blue(
                "Error log is saved in the file -> \"failed_download.log\"\n"))

            date = datetime.now()
            with open("failed_download.log", "a") as failed:
                failed.write(date.strftime("[%Y-%m-%d %I:%M:%S %p]\n"))
                failed.write(f"{video_name}\n")
                failed.write(f"{url}\n\n")
        else:
            print(colored.cyan("Download complete\n"))


def video_ux_func(video_obj_info_url) -> None:

    print("\n")
    for key, value in video_obj_info_url[1].items():
        print(colored.green(key + ":"), value)

    print(colored.yellow("\nDo you want to see the video description?"))
    catch_description_choice: bool = validate_selection_input()
    if catch_description_choice is True:
        print("\n")
        print(video_obj_info_url[0].description)
        print("\n")

    print(colored.yellow("\nDo you want to download the video? "))
    catch_download_choice: bool = validate_selection_input()
    if catch_download_choice is True:
        video_downloader_func(
            video_obj_info_url[1]["Title"], video_obj_info_url[2])
