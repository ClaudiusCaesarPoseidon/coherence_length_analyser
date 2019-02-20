import os
from ...lib import functions
from natsort import natsorted


class search():
    def __init__(self, path, files=''):
        self.path = path
        self.files = []
        if files == "image":
            self.files = [
                os.path.join(
                    path,
                    file) for file in os.listdir(path) if os.path.isdir(
                    os.path.join(
                        path,
                        file)) is False and functions.is_image(
                    os.path.join(
                        path,
                        file)) is True]
        else:
            self.files = [os.path.join(path, file)
                          for file in os.listdir(path)]
#        self.files.sort()
        self.files = natsorted(self.files)
