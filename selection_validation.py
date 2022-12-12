from clint.textui import colored


def input_choice() -> str:
    print(colored.green("yes(y), no(n), exit(x)"))
    while True:
        user_choice = input("Enter choice: ").lower()
        if user_choice in ("y", "n", "x"):
            return user_choice
        else:
            print(colored.red("Invalid input. Try again!"))
            print(colored.green("\nyes(y), no(n), exit(x)"))


def validate_selection_input() -> bool:
    user_choice = input_choice()

    if user_choice == "n":
        return False

    elif user_choice == "x":
        print(colored.yellow("Bye!"))
        exit()

    return True
