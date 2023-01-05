def convert_sec_to_readable(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return "%d:%02d:%02d" % (hour, minute, second)


def name_fixer(video_title) -> str:
    remove_punctuation_map = dict((ord(char), None) for char in r'\/*?:"<>|')
    return video_title.translate(remove_punctuation_map)


