import os


def hasNumber(inputString):
    return any(char.isdigit() for char in inputString)


def get_all_folders(path):
    return [
        x[0] for x in os.walk(path) if 'converted_videos' not in x[0]
        and hasNumber(x[0]) is True]
