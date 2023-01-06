from download_preference import download_with_subtitle, download_without_subtitle
from typing import Any, Union
import download_engine
import ux_engine


def video_data_parse(verified_data: list) -> None:

    video_data: dict[str, Union[str, Any]] = {
        "title":  verified_data[1]["Title"],
        "channel_name": verified_data[1]["Channel Name"],
        "duration": verified_data[1]["Duration"],
        "url": verified_data[2],
        "raw_obj": verified_data[0]
    }
    initiate = ux_engine.VideoUXEngine(video_data)
    video_downloader_func(initiate, video_data)


def video_downloader_func(initiate, video_data) -> None:

    initiate.show_task_data()

    selection_data: dict = initiate.selection_choice("video")

    if selection_data.get("subtitle"):
        yt_dlp_config = download_with_subtitle()
    else:
        yt_dlp_config = download_without_subtitle()
    initiate_download = download_engine.SingleVideoDownloadEngine(
        video_data.get("title"), video_data.get("url"), yt_dlp_config)

    if selection_data.get("download"):
        initiate_download.downloader()
