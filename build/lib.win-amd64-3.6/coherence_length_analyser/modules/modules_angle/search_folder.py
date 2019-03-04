import os
import numpy as np
from ...lib import functions
substring_in_list = functions.substring_in_list


class search_folder:
    """searches the folder for files"""

    def __init__(self, path, window):
        self.path = path
        self.tmp = next(os.walk(path))[1]
        self.folders = [os.path.abspath(
            os.path.join(path, x)) for x in self.tmp]
        self.files = []
        for item in self.folders:
            tmp = os.listdir(item)
            for item2 in tmp:
                if window not in item2:
                    continue
                temp = item2.split("_")
                temp = temp[-1].split(".")
                if temp[0].isdigit() is True and temp[-1].endswith("png"):
                    self.files.append(os.path.join(item, item2))
        self.tmp = [x for x in self.tmp if substring_in_list(x, self.files)]
        self.file_names = np.array((self.files, self.tmp))
