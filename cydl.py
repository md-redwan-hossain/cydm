from playlistCore import *
from videoCore import *


def selectionMenu(prompt):
    videoProceedOrNot = True
    playlistProceedOrNot = True

    while prompt == "1" and videoProceedOrNot:
        print(colored.yellow("YouTube Video Downloader"))
        link = regexCheckVideo()
        if link:
            videoProceedOrNot = videoDownloaderFunc(link)
        else:
            return

    while prompt == "2" and playlistProceedOrNot:
        print(colored.yellow("YouTube Playlist Downloader"))
        link = regexCheckPlaylist()
        if link:
            playlistProceedOrNot = playlistDownloaderFunc(link)
        else:
            return


def validate():
    option = input(str("Enter your choice (1/2/3): "))

    if option == "1" or option == "2":
        selectionMenu(option)

    elif option == "3":
        return

    elif option != "1" or option != "2":
        print(colored.red("Invalid selection!"))
        choice = str(input("Do you want to try again? (y/n) "))
        if choice == "y" or choice == "Y":
            validate()
        else:
            return


print(colored.green("CYDL: A CLI Based YouTube Video Downloader"))
print(colored.green("1. Download Video"))
print(colored.green("2. Download Playlist"))
print(colored.green("3. Exit"))

validate()
