from download_preference import download_with_subtitle, download_without_subtitle
from string_formatter import name_fixer
from clint.textui import colored
from typing import Union, Any
from pytube import Playlist
import download_engine
import ux_engine


def playlist_data_parse(playlist_link) -> None:
    playlist_obj = Playlist(playlist_link)
    all_video_urls: list = list(playlist_obj.video_urls)

    playlist_data: dict[str, Union[str, list, Any]] = {
        "title": playlist_obj.title,
        "channel_name": playlist_obj.owner,
        "urls": all_video_urls,
        "total_videos": len(all_video_urls),
        "raw_obj": playlist_obj
    }

    initiate = ux_engine.PlaylistUXEngine(playlist_data)

    playlist_downloader_func_step_1(initiate, playlist_data)


def playlist_downloader_func_step_1(initiate, playlist_data) -> None:

    initiate.show_task_data()

    selection_data: dict = initiate.selection_choice("playlist")
    if selection_data.get("download"):
        playlist_data.update(title=name_fixer(
            playlist_data.get("title")))

    if selection_data.get("subtitle"):
        yt_dlp_config = download_with_subtitle()
    else:
        yt_dlp_config = download_without_subtitle()

    if selection_data.get("download"):
        playlist_downloader_func_step_2(playlist_data, yt_dlp_config)


def playlist_downloader_func_step_2(playlist_data, yt_dlp_config) -> None:

    check_progress: int = 0

    for url in playlist_data.get("urls"):
        initiate_download = download_engine.PlaylistDownloadEngine(
            playlist_data.get("title"), url, yt_dlp_config, playlist_data.get("total_videos"), check_progress)

        signal_from_initiate_download = initiate_download.downloader()

        if signal_from_initiate_download.get("forcefully_stopped"):
            break
        else:
            check_progress += 1
            if check_progress == playlist_data.get("total_videos"):
                download_msg(playlist_data.get("title"),
                             signal_from_initiate_download)


def download_msg(playlist_name: str, signal: dict):
    print(colored.cyan("Download of "), end="")
    print(colored.yellow(f"{playlist_name} "), end="")
    if not signal.get("download_failed"):
        print(colored.cyan("is Completed.\n"))
    else:
        print(colored.cyan(
            "is completed "), end="")
        print(colored.red(
            "with some errors."))
        print(colored.blue(
            "Error log is saved in the file -> \"failed_download.log\"\n"))
