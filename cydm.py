from playlist_core import *
from video_core import *
from typing import Union
import os



def selection_menu(prompt: str) -> None:
    video_loop_breaker = True
    playlist_loop_breaker = True

    while prompt == "1" and video_loop_breaker:
        print(colored.yellow("YouTube Video Downloader"))
        video_processor: Union[list, bool] = video_link_exception_validate()

        if video_processor is not False:
            video_loop_breaker = video_ux_func(video_processor)
        else:
            exit()

    while prompt == "2" and playlist_loop_breaker:
        print(colored.yellow("YouTube Playlist Downloader"))
        link = regex_check_playlist()
        if link:
            playlist_loop_breaker = playlist_ux_and_processor(link)
        else:
            exit()


def entry_func() -> None:
    option = input(str("Enter your choice (1/2/3): "))

    if option in ("1", "2"):
        selection_menu(option)

    elif option == "3":
        exit()

    elif option not in ("1", "2"):
        print(colored.red("Invalid selection!"))
        user_selection_input = input("Do you want to try again? (y/n) ")
        choice = validate_selection_input(user_selection_input)
        if choice:
            entry_func()
        else:
            exit()


print(colored.green("CYDL: A CLI Based YouTube Video and Playlist Downloader"))
print(colored.green("1. Download Video"))
print(colored.green("2. Download Playlist"))
print(colored.green("3. Exit"))

if __name__ == "__main__":
    entry_func()
