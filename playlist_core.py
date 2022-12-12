from selection_validation import validate_selection_input
from datetime import datetime
from clint.textui import colored
from yt_dlp import YoutubeDL
from pytube import Playlist
import download_preference
from pytube import YouTube
from typing import Union


def playlist_name_fixer(parent_folder_name) -> str:
    letter_bin = list(parent_folder_name)
    for i in range(0, len(letter_bin), 1):
        if letter_bin[i] == "(":
            letter_bin[i] = "["
        elif letter_bin[i] == ")":
            letter_bin[i] = "]"
        elif letter_bin[i] == "\\":
            letter_bin[i] = ","
        elif letter_bin[i] == "/":
            letter_bin[i] = ","
    parent_folder_name = "".join(letter_bin)
    return parent_folder_name


def playlist_video_downloader(
        url: str, ydl_opts: dict,
        playlist_size: int, check_progress: int = 0) -> dict:

    download_signal = {
        "forcefully_stopped": False,
        "download_failed": False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        print(colored.yellow("\nDownloading..."))
        try:
            ydl.download(url)
        except KeyboardInterrupt:
            print(colored.red("\nDownload forcefully stopped\n"))
            download_signal["forcefully_stopped"] = True

        except:

            print(colored.red(
                f"Download failed ({check_progress}/{playlist_size})\n"))

            single_video_obj: YouTube = YouTube(url)
            date = datetime.now()
            with open("failed_download.log", "a") as failed:
                failed.write(date.strftime("[%Y-%m-%d %I:%M:%S %p]\n"))
                failed.write(f"{single_video_obj.title}\n")
                failed.write(f"{url}\n\n")
            download_signal["download_failed"] = True

        else:
            check_progress += 1
            print(colored.cyan(
                f"Download complete ({check_progress}/{playlist_size})\n"))

        finally:
            return download_signal


def playlist_ux_func(playlist_link) -> Union[tuple, None]:
    print(colored.yellow("Processing..."))

    playlist_obj = Playlist(playlist_link)

    playlist_name = playlist_obj.title
    print("\n")
    print(colored.green("Title: "), playlist_name)
    print(colored.green("Channel Name: "), playlist_obj.owner)
    print(colored.green("Total videos: "), len(playlist_obj.video_urls))

    print(colored.yellow("\nDo you want to download the playlist?"))
    playlist_download_choice: bool = validate_selection_input()

    if playlist_download_choice:
        parent_folder_name = playlist_name_fixer(playlist_name)

        print(colored.yellow("\nDo you want to download subtile? (english only)"))
        subtile_yes_or_not: bool = validate_selection_input()
        if subtile_yes_or_not == True:
            ydl_opts = download_preference.playlist_with_subtitle(
                parent_folder_name)
        else:
            ydl_opts = download_preference.playlist_without_subtitle(
                parent_folder_name)

        return playlist_obj, parent_folder_name, ydl_opts
    return None


def playlist_processor(playlist_link) -> None:
    data_from_ux_func: Union[tuple, None] = playlist_ux_func(playlist_link)

    if data_from_ux_func is not None:
        playlist_obj = data_from_ux_func[0]
        parent_folder_name: str = data_from_ux_func[1]
        ydl_opts: dict = data_from_ux_func[2]

        video_links: list = playlist_obj.video_urls
        playlist_size: int = len(video_links)
        check_progress: int = 0

        for url in video_links:
            signal_from_downloader_func: dict = playlist_video_downloader(
                url, ydl_opts, playlist_size, check_progress)

            if signal_from_downloader_func["forcefully_stopped"] == True:
                break
            else:
                check_progress += 1
                if check_progress == playlist_size:
                    download_msg(parent_folder_name,
                                 signal_from_downloader_func)


def download_msg(playlist_name: str, signal: dict):
    print(colored.cyan("Download of "), end="")
    print(colored.yellow(f"{playlist_name} "), end="")
    if signal["download_failed"] == False:
        print(colored.cyan("is Completed.\n"))
    else:
        print(colored.cyan(
            "is completed "), end="")
        print(colored.red(
            "with some errors."))
        print(colored.blue(
            "Error log is saved in the file -> \"failed_download.log\"\n"))
