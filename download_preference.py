from pathlib import Path


class VideoConfig:
    def __init__(self) -> None:
        self.BASE_DOWNLOAD_DIR = Path().cwd().joinpath("cydm_download").resolve()

        self.__yt_dlp_config: dict = {
            "format": "best",
            "quiet": True,
            "noplaylist": True,
            "forcetitle": True,
            "no_warnings": True,
            "windowsfilenames": True,
            "allow_unplayable_formats": False,
            "download_archive": f"{Path(self.BASE_DOWNLOAD_DIR).joinpath('completed_download_archive.log')}",
            "outtmpl": f"{Path(self.BASE_DOWNLOAD_DIR).joinpath('%(title)s.%(ext)s')}"
        }

    @property
    def config(self) -> dict:
        return self.__yt_dlp_config

    @config.setter
    def config(self, updater_dict) -> None:
        self.__yt_dlp_config = self.__yt_dlp_config | updater_dict

    def add_subtitle_support(self):

        subtitle_support_config = {
            "writeautomaticsub": True,
            "writesubtitles": True,
            "subtitleslangs": ["en"],
        }

        self.__yt_dlp_config = self.__yt_dlp_config | subtitle_support_config


class PlaylistConfig(VideoConfig):

    def __init__(self, playlist_name):
        super().__init__()
        self.PLAYLIST_DIR = Path(self.BASE_DOWNLOAD_DIR).joinpath(
            playlist_name).resolve()

        self.config.update(
            {"outtmpl":
                f"{Path(self.PLAYLIST_DIR).joinpath('temp_vid_download.%(ext)s')}"
             }
        )


def video_with_subtitle() -> dict:
    config_obj = VideoConfig()
    config_obj.add_subtitle_support()
    return config_obj.config


def video_without_subtitle() -> dict:
    config_obj = VideoConfig()
    return config_obj.config


def playlist_with_subtitle(playlist_name) -> dict:
    config_obj = PlaylistConfig(playlist_name)
    config_obj.add_subtitle_support()
    return config_obj.config


def playlist_without_subtitle(playlist_name) -> dict:
    config_obj = PlaylistConfig(playlist_name)
    return config_obj.config
