import re
from clint.textui import colored


def validateYoutubeVideoLink(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = bool(re.match(youtube_regex, url))
    return youtube_regex_match


def validateYoutubePlaylistLink(url):
    youtube_regex = (r"^.*(youtu.be\/|list=)([^#\&\?]*).*")
    youtube_regex_match = bool(re.match(youtube_regex, url))
    return youtube_regex_match


def regexCheckVideo():
    link = str(input("Enter the youtube video link: "))
    if validateYoutubeVideoLink(link):
        return link
    else:
        print(colored.red("Link invalid"))
        choice = str(input("Do you want to try again? (y/n) "))
        if choice.lower() == "y":
            catch = regexCheckVideo()
            return catch
        elif choice.lower() == "n":
            return False


def regexCheckPlaylist():
    link = str(input("Enter the youtube playlist link: "))
    if validateYoutubePlaylistLink(link):
        return link
    else:
        print(colored.red("Link invalid"))
        choice = str(input("Do you want to try again? (y/n) "))
        if choice.lower() == "y":
            catch = regexCheckPlaylist()
            return catch
        elif choice.lower() == "n":
            return False
