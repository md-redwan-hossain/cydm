import re
from clint.textui import colored


def validateYoutubeLink(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = bool(re.match(youtube_regex, url))
    return youtube_regex_match


def regexCheck():
    link = str(input(colored.yellow("Input the youtube video link: ")))
    if validateYoutubeLink(link):
        return link
    else:
        print(colored.red("Link invalid"))
        choice = str(input(colored.yellow("Do you want to try again? (y/n) ")))
        if choice == "y" or choice == "Y":
            catch = regexCheck()
            return catch
        elif choice == "n" or choice == "N":
            return False
