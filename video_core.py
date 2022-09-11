from regex_link_validation import *
from time_converter import *
from yt_dlp import YoutubeDL
from pytube import YouTube


def on_complete_again_download_or_not():
    choose_wanna_download_another_video = str(
        input("Do you want to download another video? (y/n) "))
    if choose_wanna_download_another_video.lower() == "y":
        linkCheck = regex_check_video()
        if linkCheck:
            video_ux_func(linkCheck)
        else:
            return False
    else:
        return False


def video_downloader_func(url):
    ydl_opts = {
        'format': 'best',
        'quiet':  True,
        'outtmpl': './download/%(title)s.%(ext)s',
        'noplaylist':  True,
        'forcetitle':  True,
        'writeautomaticsub': True,
        'subtitleslangs':  ['en'],
    }

    with YoutubeDL(ydl_opts) as ydl:
        print(colored.yellow("\nDownloading..."))
        ydl.download(url)
        print(colored.cyan("Download complete\n"))
        catch_redownload_choice = on_complete_again_download_or_not()
        if catch_redownload_choice:
            return True
        else:
            return False


def video_ux_func(videoLink):
    single_video_obj = YouTube(videoLink)
    print("\n")
    print(colored.green("Title: "), single_video_obj.title)
    print(colored.green("Author: "), single_video_obj.author)
    print(colored.green("Duration: "),
          convert_sec_to_readable((single_video_obj.length)))

    description_choice = str(input(
        "Do you want to see video description? (y/n) "))

    if description_choice.lower() == "y":
        print(single_video_obj.description)

    download_choice = str(input(
        "Do you want to download the video? (y/n) "))

    if download_choice.lower() == "y":
        video_downloader_func(videoLink)

    return False
