import re
from clint.textui import colored


def validate_youtube_video_link(url):
    youtube_regex_video = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = bool(re.match(youtube_regex_video, url))
    return youtube_regex_match


def validate_youtube_playlistLink(url):
    youtube_regex_playlist = (r"^.*(youtu.be\/|list=)([^#\&\?]*).*")
    youtube_regex_match = bool(re.match(youtube_regex_playlist, url))
    return youtube_regex_match


def regex_check_video():
    link = str(input("Enter the youtube video link: "))
    if validate_youtube_video_link(link):
        return link
    else:
        print(colored.red("Link invalid"))
        choice = str(input("Do you want to try again? (y/n) "))
        if choice.lower() == "y":
            catch = regex_check_video()
            return catch
        elif choice.lower() == "n":
            return False


def regex_check_playlist():
    link = str(input("Enter the youtube playlist link: "))
    if validate_youtube_playlistLink(link):
        return link
    else:
        print(colored.red("Link invalid"))
        choice = str(input("Do you want to try again? (y/n) "))
        if choice.lower() == "y":
            catch = regex_check_playlist()
            return catch
        elif choice.lower() == "n":
            return False
