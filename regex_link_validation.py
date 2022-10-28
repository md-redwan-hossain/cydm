import re
from clint.textui import colored


def validate_youtube_playlistLink(url):
    youtube_regex_playlist = (r"^.*(youtu.be\/|list=)([^#\&\?]*).*")
    youtube_regex_match = bool(re.match(youtube_regex_playlist, url))
    return youtube_regex_match


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
