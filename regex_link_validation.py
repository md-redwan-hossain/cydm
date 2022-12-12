from selection_validation import validate_selection_input
from clint.textui import colored
from typing import Union
import re


def validate_youtube_playlist_link(url):
    youtube_regex_playlist = (r"^.*(youtu.be\/|list=)([^#\&\?]*).*")
    youtube_regex_match = bool(re.match(youtube_regex_playlist, url))
    return youtube_regex_match


def error_handler(link):
    validator = validate_youtube_playlist_link(link)
    return True if validator == True else False


def regex_check_playlist() -> Union[str, None]:

    while True:
        link = str(input("Enter the youtube playlist link: "))
        validate = error_handler(link)
        if validate == True:
            return link

        elif validate == False:
            print(colored.red("Link invalid"))
            print(colored.yellow("\nDo you want to try again?"))
            choice: bool = validate_selection_input()
            if choice == False:
                break
            else:
                continue
    return None
