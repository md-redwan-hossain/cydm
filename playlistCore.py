from pytube.cli import on_progress
from regex import *
from pytube import Playlist


def onSuccessAgainOrNot():
    print("Download completed")
    againplaylistDownloadChoice = str(
        input("Do you want to download another playlist? (y/n) "))
    if againplaylistDownloadChoice == "y" or againplaylistDownloadChoice == "Y":
        linkCheck = regexCheckPlaylist()
        if linkCheck:
            playlistDownloaderFunc(linkCheck)
        else:
            return False
    else:
        return False


def playlistDownloaderFunc(playlistLink):

    cydlp = Playlist(playlistLink)
    print(colored.green("Title: "), cydlp.title)
    print(colored.green("Owner: "), cydlp.owner)
    print(colored.green("Total videos: "), len(cydlp.videos))
    done = False
    playlistDownloadChoice = str(input(
        "Do you want to download the playlist? (y/n) "))

    if playlistDownloadChoice == "n" or playlistDownloadChoice == "N":
        return False

    elif playlistDownloadChoice == "y" or playlistDownloadChoice == "Y":
        folderName = cydlp.title
        print(colored.yellow("Downloading..."))
        for video in cydlp.videos:
            video.register_on_progress_callback(on_progress)
            video.streams.get_lowest_resolution().download(
                "./download/playlist/{makeDir}".format(makeDir=folderName))
            done = True

    if done:
        catch = onSuccessAgainOrNot()
        if catch:
            return True
        else:
            return False
