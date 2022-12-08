from selection_validation import validate_selection_input
from clint.textui import colored
from typing import Union, Any
import playlist_core
import video_core


def selection_menu(prompt: str) -> None:
    video_loop_breaker: Union[bool, None] = True
    playlist_loop_breaker: Union[bool, None] = True

    while prompt == "1" and video_loop_breaker:
        print(colored.yellow("YouTube Video Downloader"))
        video_processor: Union[list[Any],
                               bool] = video_core.video_link_exception_validate()

        if video_processor is not False:
            video_loop_breaker = video_core.video_ux_func(video_processor)
        else:
            print(colored.yellow("Bye!"))
            exit()

    while prompt == "2" and playlist_loop_breaker:
        print(colored.yellow("YouTube Playlist Downloader"))
        link = playlist_core.regex_check_playlist()
        if link:
            playlist_loop_breaker = playlist_core.playlist_ux_and_processor(
                link)
        else:
            print(colored.yellow("Bye!"))
            exit()


def entry_func() -> None:
    try:
        option = input(str("Enter your choice (1/2/3): "))

        if option in ("1", "2"):
            selection_menu(option)

        elif option == "3":
            print(colored.yellow("Bye!"))
            exit()

        elif option not in ("1", "2"):
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


print(colored.green("CYDL: A CLI Based YouTube Video and Playlist Downloader"))
print(colored.green("1. Download Video"))
print(colored.green("2. Download Playlist"))
print(colored.green("3. Exit"))

if __name__ == "__main__":
    entry_func()
