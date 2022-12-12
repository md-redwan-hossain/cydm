class VideoConfig:
    def __init__(self) -> None:
        self.__ydl_opts: dict = {
            "format": "best",
            "quiet": True,
            "noplaylist": True,
            "forcetitle": True,
            "no_warnings": True,
            "allow_unplayable_formats": False,
            "outtmpl": "./cydm_download/%(title)s.%(ext)s",
        }

    @property
    def config(self) -> dict:
        return self.__ydl_opts

    @config.setter
    def config(self, updater_dict) -> None:
        self.__ydl_opts = self.__ydl_opts | updater_dict

    def add_subtitle_support(self):

        subtitle_support_config = {
            "writeautomaticsub": True,
            "writesubtitles": True,
            "subtitleslangs": ["en"],
        }

        self.__ydl_opts = self.__ydl_opts | subtitle_support_config


class PlaylistConfig(VideoConfig):

    def __init__(self, parent_folder_name):
        super().__init__()

        self.config.update(
            {"outtmpl":
                rf"./cydm_download/{parent_folder_name}/%(title)s.%(ext)s"}
        )


def video_with_subtitle() -> dict:
    config_obj = VideoConfig()
    config_obj.add_subtitle_support()
    return config_obj.config


def video_without_subtitle() -> dict:
    config_obj = VideoConfig()
    return config_obj.config


def playlist_with_subtitle(parent_folder_name) -> dict:
    config_obj = PlaylistConfig(parent_folder_name)
    config_obj.add_subtitle_support()
    return config_obj.config


def playlist_without_subtitle(parent_folder_name) -> dict:
    config_obj = PlaylistConfig(parent_folder_name)
    return config_obj.config
