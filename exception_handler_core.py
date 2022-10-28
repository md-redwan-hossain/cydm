from exception_handler_helper import video_exception_handler
from selection_validation import validate_selection_input
from typing import Any, Union


def video_link_exception_validate() -> Union[list, bool]:
    link: str = input("Enter the youtube video link: ")
    video_obj_info_url: Union[list[Any], bool] = video_exception_handler(link)
    if video_obj_info_url:
        return video_obj_info_url
    else:
        user_selection_input = input("Do you want to try again? (y/n) ")
        choice = validate_selection_input(user_selection_input)
        if choice:
            video_obj_info_url = video_link_exception_validate()
            return video_obj_info_url
        else:
            return False
