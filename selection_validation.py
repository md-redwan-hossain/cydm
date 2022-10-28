from clint.textui import colored


def validate_selection_input(received_input) -> bool:

    if received_input.lower() not in ("y", "n"):
        print(colored.red("Invalid input"))
        catch_retry_choice = retry()
        return catch_retry_choice

    elif received_input.lower() == "n":
        return False
    
    return True


def retry() -> bool:
    print(colored.cyan("Re-enter selection (y/n)"))
    print(colored.yellow("Exit (x)"))
    retry_choice: str = input("Choice: ")

    if retry_choice.lower() == "n":
        return False

    elif retry_choice.lower() == "y":
        return True

    return False
