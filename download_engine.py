from clint.textui import colored
import failed_download_logger
from yt_dlp import YoutubeDL
from pathlib import Path


class BaseDownloadEngine:
    def __init__(self, video_title: str, video_url: str, yt_dlp_config: dict) -> None:
        self.video_url: str = video_url
        self.video_title: str = video_title
        self.yt_dlp_config: dict = yt_dlp_config
        self.BASE_DOWNLOAD_DIR = Path().cwd().joinpath("cydm_download").resolve()

        self.download_signal: dict = {
            "forcefully_stopped": False,
            "download_failed": False,
        }

    def downloader(self):
        with YoutubeDL(self.yt_dlp_config) as ydl:
            print(colored.yellow("\nDownloading..."))
            try:
                ydl.download(self.video_url)
            except KeyboardInterrupt:
                print(colored.red("\nDownload forcefully stopped\n"))
                self.download_signal.update(forcefully_stopped=True)
            except:
                self.download_signal.update(download_failed=True)
                failed_download_logger.create_error_log(
                    self.video_title, self.video_url)


class SingleVideoDownloadEngine(BaseDownloadEngine):
    def __init__(self, video_title: str, video_url: str, yt_dlp_config: dict) -> None:
        super().__init__(video_title, video_url, yt_dlp_config)

    def downloader(self):
        super().downloader()
        if self.download_signal.get("download_failed"):
            print(colored.red("Download failed."))
            print(colored.blue(
                "Error log is saved in the file -> \"failed_download.log\"\n"))

        elif not self.download_signal.get("download_failed") \
                and not self.download_signal.get("forcefully_stopped"):
            print(colored.cyan("Download complete\n"))


class PlaylistDownloadEngine(BaseDownloadEngine):
    def __init__(self, playlist_name: str, video_title: str, video_url: str, yt_dlp_config: dict,
                 playlist_size: int, check_progress: int = 0) -> None:
        super().__init__(video_title, video_url, yt_dlp_config)

        self.playlist_size = playlist_size
        self.playlist_name = playlist_name
        self.check_progress = check_progress
        self.PLAYLIST_DIR = Path(self.BASE_DOWNLOAD_DIR).joinpath(
            playlist_name).resolve()

    def video_file_renamer(self, serial_no: int) -> None:
        TEMP_FILES = list(Path(self.PLAYLIST_DIR).glob("temp_vid_download.*"))
        for file in TEMP_FILES:
            file_str_path = str(file)
            file_extension_index_start: int = file_str_path.rfind(".")
            file_extension = file_str_path[file_extension_index_start:]
            dst_path = None

            if file_str_path.rfind(".en") != -1:
                dst_path = Path(self.PLAYLIST_DIR).joinpath(
                    f"{serial_no}. {self.video_title}.en{file_extension}")
            else:
                dst_path = Path(self.PLAYLIST_DIR).joinpath(
                    f"{serial_no}. {self.video_title}{file_extension}")
            try:
                file.rename(dst_path)
            except FileExistsError:
                pass

    def downloader(self):
        super().downloader()
        if self.download_signal.get("download_failed"):
            print(colored.red(
                f"Download failed ({self.check_progress+1}/{self.playlist_size})\n"))

        elif not self.download_signal.get("download_failed") \
                and not self.download_signal.get("forcefully_stopped"):
            self.video_file_renamer(self.check_progress+1)
            self.check_progress += 1
            print(colored.cyan(
                f"Download complete ({self.check_progress}/{self.playlist_size})\n"))

        return self.download_signal
