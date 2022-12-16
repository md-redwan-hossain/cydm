from selection_validation import validate_selection_input
from clint.textui import colored
from typing import Union, Any
from exception_handler_core import video_link_exception_validate
import regex_link_validation
import playlist_core
import video_core
import warnings
import cydm_updater

warnings.filterwarnings("ignore")


def selection_menu(prompt: str):

    if prompt == "1":
        print(colored.yellow("YouTube Video Downloader"))
        verified_data: Union[bool, list] = video_link_exception_validate()

        if isinstance(verified_data, list):
            video_core.video_data_parse(verified_data)

    elif prompt == "2":
        print(colored.yellow("YouTube Playlist Downloader"))
        link = regex_link_validation.regex_check_playlist()
        if link:
            playlist_core.playlist_data_parse(link)

    entry_func()


def menu() -> None:
    print(colored.green("CYDL: A CLI Based YouTube Video and Playlist Downloader"))
    print(colored.green("1. Download Video"))
    print(colored.green("2. Download Playlist"))
    print(colored.red("3. Exit"))
    print(colored.yellow("99. Check for CYDM update"))


def entry_func() -> None:
    try:
        menu()
        option: str = input(str("Enter your choice (1/2/3/99): "))

        if option in ("1", "2"):
            selection_menu(option)

        elif option == "3":
            print(colored.yellow("Bye!"))
            exit()

        elif option == "99":
            status = cydm_updater.run_update_check()
            if status == True:
                print(colored.cyan("CYDM updated"))
                print(colored.yellow("Launch CYDM again to get new changes.\n"))
            else:
                print(colored.cyan("CYDM is up to date\n"))
                entry_func()

        elif option not in ("1", "2", "3", "99"):
            print(colored.red("Invalid selection!"))
            print(colored.yellow("Do you want to try again?"))
            choice = validate_selection_input()
            if choice:
                entry_func()
            else:
                print(colored.yellow("Bye!"))
                exit()
    except KeyboardInterrupt:
        print(colored.yellow("\nBye!"))


if __name__ == "__main__":
    entry_func()
