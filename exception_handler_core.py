from exception_handler_helper import video_exception_handler
from selection_validation import validate_selection_input
from clint.textui import colored
from typing import Any, Union


def video_link_exception_validate() -> Union[list, bool]:
    link: str = input("Enter the youtube video link: ")
    video_obj_info_url: Union[list[Any], bool] = video_exception_handler(link)
    if video_obj_info_url:
        return video_obj_info_url
    else:
        print(colored.yellow("Do you want to try again? "))
        retry_choice = validate_selection_input()
        if retry_choice:
            video_obj_info_url = video_link_exception_validate()
            return video_obj_info_url
        else:
            return False
