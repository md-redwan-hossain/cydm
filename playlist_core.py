from regex_link_validation import *
import download_preference
from selection_validation import validate_selection_input
from yt_dlp import YoutubeDL
from pytube import Playlist
from typing import Union
import os


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


def on_complete_again_download_or_not() -> bool:
    print(colored.yellow("Do you want to download another playlist?"))
    choose_wanna_download_another_playlist: bool = validate_selection_input()

    if choose_wanna_download_another_playlist:
        linkCheck = regex_check_playlist()
        if linkCheck:
            playlist_ux_and_processor(linkCheck)
        else:
            exit()

    return False


def playlist_video_downloader(
        url: str, parent_folder_name: str, subtitle_choice: bool) -> Union[None, bool]:

    if subtitle_choice:
        ydl_opts = download_preference.playlist_with_subtitle(
            parent_folder_name)
    else:
        ydl_opts = download_preference.playlist_without_subtitle(
            parent_folder_name)

    with YoutubeDL(ydl_opts) as ydl:
        print(colored.yellow("\nDownloading..."))
        try:
            ydl.download(url)
        except KeyboardInterrupt:
            print(colored.red("\nDownload forcefully stopped\n"))
            try_another_playlist_after_force_exit: bool = on_complete_again_download_or_not()
            if try_another_playlist_after_force_exit is False:
                print(colored.yellow("Bye!"))
                exit()

        except:
            print(colored.red("Download failed\n"))
        else:
            print(colored.cyan("Download complete\n"))
        return None


def playlist_ux_and_processor(playlist_link) -> bool:
    print(colored.yellow("Processing..."))
    playlist_download_complete = False
    playlist_obj = Playlist(playlist_link)

    playlist_name = playlist_obj.title
    print("\n")
    print(colored.green("Title: "), playlist_name)
    print(colored.green("Owner: "), playlist_obj.owner)
    print(colored.green("Total videos: "), len(playlist_obj.video_urls))

    print(colored.yellow("\nDo you want to download the playlist?"))
    playlist_download_choice: bool = validate_selection_input()

    if playlist_download_choice:
        parent_folder_name = playlist_name_fixer(playlist_name)

        print(colored.yellow("\nDo you want to download subtile? (english only)"))
        subtile_yes_or_not: bool = validate_selection_input()

        video_links = playlist_obj.video_urls
        size, check = len(video_links), 0

        for url in video_links:
            playlist_video_downloader(
                url, parent_folder_name, subtile_yes_or_not)

            check += 1
            if check == size:
                playlist_download_complete = True

    if playlist_download_complete:
        catch = on_complete_again_download_or_not()
        if catch:
            return True
        else:
            return False

    return False
