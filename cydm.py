from exception_handler_core import video_link_exception_validate
from selection_validation import validate_selection_input
from clint.textui import colored
from pathlib import Path
import regex_link_validation
from typing import Union
import playlist_core
import cydm_updater
import video_core
import warnings

warnings.filterwarnings("ignore")

BASE_DOWNLOAD_DIR = Path().cwd().joinpath("cydm_download").resolve()


def archive_cleaner():
    with open(f"{Path(BASE_DOWNLOAD_DIR).joinpath('completed_download_archive.log')}", "w") as download_archive:
        download_archive.write("")


def selection_menu(prompt: str):

    if prompt == "1":
        print(colored.yellow("YouTube Video Downloader\n"))
        verified_data: Union[bool, list] = video_link_exception_validate()

        if isinstance(verified_data, list):
            video_core.video_data_parse(verified_data)

    elif prompt == "2":
        print(colored.yellow("YouTube Playlist Downloader\n"))
        link = regex_link_validation.regex_check_playlist()
        if link:
            playlist_core.playlist_data_parse(link)

    entry_func()


def menu() -> None:
    print(colored.blue("\nCYDM: A CLI Based YouTube Video and Playlist Downloader"))
    print(colored.green("1. Download Video"))
    print(colored.green("2. Download Playlist"))
    print(colored.red("3. Exit"))
    print(colored.yellow("UPD. Check for CYDM update"))
    print(colored.cyan("CLR. Clear download logs"))


def entry_func() -> None:
    try:
        menu()
        option: str = input(str("\nEnter your choice (1/2/3/CLR/UPD): "))

        if option in ("1", "2"):
            selection_menu(option)

        elif option == "3":
            print(colored.yellow("Bye!\n"))
            exit()
        elif option == "CLR":
            archive_cleaner()
            print(colored.yellow("Previous download archive is cleaned.\n"))
            entry_func()

        elif option == "UPD":
            status = cydm_updater.run_update_check()
            if status == True:
                print(colored.cyan("CYDM is updated with new changes."))
                print(colored.yellow("Launch CYDM again to get new updates.\n"))
            else:
                print(colored.cyan("CYDM is up to date.\n"))
                entry_func()

        elif option not in ("1", "2", "3", "CLR", "UPD"):
            print(colored.red("Invalid selection!"))
            print(colored.yellow("Do you want to try again?"))
            choice = validate_selection_input()
            if choice:
                entry_func()
            else:
                print(colored.yellow("Bye!\n"))
                exit()
    except KeyboardInterrupt:
        print(colored.yellow("\nBye!"))


if __name__ == "__main__":
    entry_func()
