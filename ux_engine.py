from selection_validation import validate_selection_input
from clint.textui import colored


class BaseUXEngine:
    def __init__(self, task_data: dict) -> None:
        print(colored.yellow("Processing..."))

        self.task_data: dict = task_data

        self.selection_data: dict = {
            "description": False,
            "download": False,
            "subtitle": True
        }

    def show_task_data(self) -> None:
        print("\n")
        print(colored.green("Title: "), self.task_data.get("title"))
        print(colored.green("Channel Name: "),
              self.task_data.get("channel_name"))

    def selection_choice(self, task_type: str) -> dict:
        print(colored.yellow(
            f"\nDo you want to see the {task_type} description?"))
        self.selection_data.update(description=validate_selection_input())
        if self.selection_data.get("description"):
            print("\n")
            try:
                print(self.task_data["raw_obj"].description)
            except KeyError:
                print(colored.red("Description not found"))
            print("\n")

        print(colored.yellow(f"\nDo you want to download the {task_type}?"))
        self.selection_data.update(download=validate_selection_input())

        print(colored.yellow("\nDo you want to download subtitle (english only)?"))
        self.selection_data.update(subtitle=validate_selection_input())

        return self.selection_data


class PlaylistUXEngine(BaseUXEngine):
    def __init__(self, task_data) -> None:
        super().__init__(task_data)

    def show_task_data(self) -> None:
        super().show_task_data()
        print(colored.green("Total videos: "),
              self.task_data.get("total_videos"))

    def selection_choice(self, task_type: str) -> dict:
        return super().selection_choice(task_type)


class VideoUXEngine(BaseUXEngine):
    def __init__(self, task_data) -> None:
        super().__init__(task_data)

    def show_task_data(self) -> None:
        super().show_task_data()
        print(colored.green("Duration: "),
              self.task_data.get("duration"))

    def selection_choice(self, task_type: str) -> dict:
        return super().selection_choice(task_type)
