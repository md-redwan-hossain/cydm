from pathlib import Path


class BaseConfig:
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


def download_with_subtitle() -> dict:
    config_obj = BaseConfig()
    config_obj.add_subtitle_support()
    return config_obj.config


def download_without_subtitle() -> dict:
    config_obj = BaseConfig()
    return config_obj.config
