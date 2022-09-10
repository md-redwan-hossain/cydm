from pytube import YouTube
from pytube.cli import on_progress
from regex import *
from timeConverter import *


def videoDownloadSuccess(stream, path):
    print(colored.green("\nDownload complete"))
    WannaDownloadAgain()


def WannaDownloadAgain():
    againVideoDownloadChoice = str(
        input("Do you want to download another video? (y/n) "))
    if againVideoDownloadChoice.lower() == "y":
        linkCheck = regexCheckVideo()
        if linkCheck:
            videoDownloaderFunc(linkCheck)
        else:
            return False
    else:
        return False


def videoDownloaderFunc(videoLink):
    yt = YouTube(
        videoLink,
        on_progress_callback=on_progress,
        on_complete_callback=videoDownloadSuccess
    )

    print(colored.green("Title: "), yt.title)
    print(colored.green("Author: "), yt.author)
    print(colored.green("Duration: "), convert(yt.length))
    descriptionChoice = str(input(
        "Do you want to see video description? (y/n) "))

    if descriptionChoice.lower() == "y":
        print(yt.description)

    downloadChoice = str(input(
        "Do you want to download the video? (y/n) "))

    if downloadChoice.lower() == "y":
        print(colored.yellow("Downloading..."))
        downloadProcessor = yt.streams.get_highest_resolution()
        downloadProcessor.download("./download")

    return False
