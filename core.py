from pytube import YouTube
from pytube.cli import on_progress
from regex import *
from timeConverter import *


def again(stream, path):
    print("\nDownload complete")
    againDownloadChoice = str(
        input("Do you want to download another video? (y/n) "))
    if againDownloadChoice == "y" or againDownloadChoice == "Y":
        linkCheck = regexCheck()
        if linkCheck:
            downloaderFunc(linkCheck)
        else:
            return False


def downloaderFunc(video_link):
    yt = YouTube(
        video_link,
        on_progress_callback=on_progress,
        on_complete_callback=again
    )
    print(colored.green("Title: "), yt.title)
    print(colored.green("Author: "), yt.author)
    print(colored.green("Duration: "), convert(yt.length))
    descriptionChoice = str(input(
        "Do you want to see video description? (y/n) "))

    if descriptionChoice == "y" or descriptionChoice == "Y":
        print(yt.description)

    downloadChoice = str(input(
        "Do you want to download the video? (y/n) "))

    if downloadChoice == "y" or downloadChoice == "Y":
        print(colored.yellow("Downloading..."))
        downloaderFuncownloader = yt.streams.get_highest_resolution()
        downloaderFuncownloader.download("./downloads")
        return True
    elif downloadChoice == "n" or downloadChoice == "N":
        return False
