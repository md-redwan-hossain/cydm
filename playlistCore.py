from pytube.cli import on_progress
from regex import *
from pytube import Playlist, YouTube


'''
Design approach:
From the cydl.py file, a youtube playlist link comes into playlist processor function (ppf) after regex validation. ppf() has the following features:

- Shows playlist title
- Shows playlist owner name
- Shows total video count by counting an object length
- Asks for confirmation to download the playlist.
 ---- If no is entered, ppf() returns false and exits the program
 ---- If yes is entered, the playlist's video links are stored inside a list (videoLinks)
---------- Then a for loop runs for each items of the list (videoLinks)
---------- The loops evokes singleVidFromPlaylist() with url and foldername arguments


'''


def playlistDownloadSuccess(stream, path):
    print(colored.green("\nDownload complete"))


def onCompleteAgainOrNot():
    againplaylistDownloadChoice = str(
        input("Do you want to download another playlist? (y/n) "))
    if againplaylistDownloadChoice.lower() == "y":
        linkCheck = regexCheckPlaylist()
        if linkCheck:
            playlistProcessor(linkCheck)
        else:
            return False
    else:
        return False


def singleVidFromPlaylist(videoLink, folderName):
    videoObj = YouTube(
        videoLink,
        on_progress_callback=on_progress,
        on_complete_callback=playlistDownloadSuccess
    )

    print(colored.green("\nDownloading:"), videoObj.title)
    downloadProcessor = videoObj.streams.get_highest_resolution()
    downloadProcessor.download(
        "./download/playlist/{makeDir}".format(makeDir=folderName))


def playlistProcessor(playlistLink):
    done = False
    playlistObj = Playlist(playlistLink)
    print(colored.green("Title: "), playlistObj.title)
    print(colored.green("Owner: "), playlistObj.owner)
    print(colored.green("Total videos: "), len(playlistObj.videos))
    folderName = str(playlistObj.title)

    playlistDownloadChoice = str(input(
        "Do you want to download the playlist? (y/n) "))

    if playlistDownloadChoice.lower() == "n":
        return False

    elif playlistDownloadChoice.lower() == "y":
        videoLinks = playlistObj.video_urls
        size, check = len(videoLinks), 0

        for url in videoLinks:
            singleVidFromPlaylist(url, folderName)
            check += 1
            if check == size:
                done = True

    if done:
        catch = onCompleteAgainOrNot()
        if catch:
            return True
        else:
            return False
    else:
        return
