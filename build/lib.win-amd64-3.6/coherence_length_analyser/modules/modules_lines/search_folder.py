import os
import numpy as np
from ...lib import functions
substring_in_list = functions.substring_in_list


class search_folder:
    """gets all relevent images in folder"""

    def __init__(self, path):
        self.path = path
        self.tmp = next(os.walk(path))[1]
        self.folders = [os.path.abspath(
            os.path.join(path, x)) for x in self.tmp]
        self.files = []
        window = "Boxcar"
        for item in self.folders:
            tmp = os.listdir(item)
            for item2 in tmp:
                if window not in item2:
                    continue
                temp = item2.split("_")
                if temp[-1].endswith("alignment2.png"):
                    self.files.append(os.path.join(item, item2))
        self.tmp = [x for x in self.tmp if substring_in_list(x, self.files)]
        self.file_names = np.array((self.files, self.tmp))
