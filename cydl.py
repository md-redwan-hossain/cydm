from playlist_core import *
from video_core import *


def selection_menu(prompt):
    video_proceed_or_not = True
    playlist_proceed_or_not = True

    while prompt == "1" and video_proceed_or_not:
        print(colored.yellow("YouTube Video Downloader"))
        link = regex_check_video()
        if link:
            video_proceed_or_not = video_ux_func(link)
        else:
            return

    while prompt == "2" and playlist_proceed_or_not:
        print(colored.yellow("YouTube Playlist Downloader"))
        link = regex_check_playlist()
        if link:
            playlist_proceed_or_not = playlist_ux_and_processor(link)
        else:
            return


def entry_func():
    option = input(str("Enter your choice (1/2/3): "))

    if option == "1" or option == "2":
        selection_menu(option)

    elif option == "3":
        return

    elif option != "1" or option != "2":
        print(colored.red("Invalid selection!"))
        choice = str(input("Do you want to try again? (y/n) "))
        if choice.lower() == "y":
            entry_func()
        else:
            return


print(colored.green("CYDL: A CLI Based YouTube Video and Playlist Downloader"))
print(colored.green("1. Download Video"))
print(colored.green("2. Download Playlist"))
print(colored.green("3. Exit"))

entry_func()
