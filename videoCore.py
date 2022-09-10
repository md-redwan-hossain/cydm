from pytube import YouTube
from pytube.cli import on_progress
from regex import *
from timeConverter import *


def again(stream, path):
    print(colored.green("\nDownload complete"))
    againDownloadChoice = str(
        input("Do you want to download another video? (y/n) "))
    if againDownloadChoice == "y" or againDownloadChoice == "Y":
        linkCheck = regexCheckVideo()
        if linkCheck:
            videoDownloaderFunc(linkCheck)
        else:
            return False


def videoDownloaderFunc(videoLink):
    yt = YouTube(
        videoLink,
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
        downloadProcessor = yt.streams.get_highest_resolution()
        downloadProcessor.download("./downloads")
        return True
    elif downloadChoice == "n" or downloadChoice == "N":
        return False
