from regex_link_validation import *
from download_preference import *
from yt_dlp import YoutubeDL
from pytube import Playlist


def on_complete_again_download_or_not():
    choose_wanna_download_another_playlist = str(
        input("Do you want to download another playlist? (y/n) ")
    )
    if choose_wanna_download_another_playlist.lower() == "y":
        linkCheck = regex_check_playlist()
        if linkCheck:
            playlist_ux_and_processor(linkCheck)
        else:
            return False
    else:
        return False


def playlist_video_downloader(
    url: str, parent_folder_name: str, subtitle_choice: str
) -> None:

    if subtitle_choice.lower() == "y":
        ydl_opts = playlist_with_subtitle(parent_folder_name)
    else:
        ydl_opts = playlist_without_subtitle(parent_folder_name)

    with YoutubeDL(ydl_opts) as ydl:
        print(colored.yellow("\nDownloading..."))
        ydl.download(url)
        print(colored.cyan("Download complete\n"))


def playlist_ux_and_processor(playlist_link):
    print(colored.yellow("Processing..."))
    playlist_download_complete = False
    playlist_obj = Playlist(playlist_link)

    playlist_name = playlist_obj.title
    print("\n")
    print(colored.green("Title: "), playlist_obj.title)
    print(colored.green("Owner: "), playlist_obj.owner)
    print(colored.green("Total videos: "), len(playlist_obj.video_urls))

    playlist_download_choice = str(
        input("Do you want to download the playlist? (y/n) ")
    )

    if playlist_download_choice.lower() == "n":
        return False

    elif playlist_download_choice.lower() == "y":
        subtile_yes_or_not = input("Do you want to download subtile? (y/n)")
        video_links = playlist_obj.video_urls
        size, check = len(video_links), 0

        for url in video_links:
            playlist_video_downloader(url, playlist_name, subtile_yes_or_not)
            check += 1
            if check == size:
                playlist_download_complete = True

    if playlist_download_complete:
        catch = on_complete_again_download_or_not()
        if catch:
            return True
        else:
            return False
    else:
        return
