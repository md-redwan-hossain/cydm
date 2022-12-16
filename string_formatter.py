def convert_sec_to_readable(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return "%d:%02d:%02d" % (hour, minute, second)


def name_fixer(name) -> str:
    letter_bin = list(name)
    for i in range(0, len(letter_bin), 1):
        if letter_bin[i] == "(":
            letter_bin[i] = "["
        elif letter_bin[i] == ")":
            letter_bin[i] = "]"
        elif letter_bin[i] == "\\":
            letter_bin[i] = ","
        elif letter_bin[i] == "/":
            letter_bin[i] = ","
    name = "".join(letter_bin)
    return name
