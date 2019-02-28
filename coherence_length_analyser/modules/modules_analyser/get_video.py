import os


def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s and s.endswith('.avi'):
            return i
    return None


def hasNumber(inputString):
    return any(char.isdigit() for char in inputString)


class get_video:
    def __init__(self, path):
        self.order = ['Kaiser', 'Gauss', 'Hanning', 'Hamming', 'Hanning', 'Slepian', 'Boxcar']
        self.folders = [x[0] for x in os.walk(path) if hasNumber(x[0]) is True]
        self.files = None

    def get(self, window='Kaiser'):
        order = self.order.copy()
        order.remove(window)
        order.insert(0, window)
        files = []
        for item in self.folders:
            tmp = os.listdir(item)
            for window in order:
                index = index_containing_substring(tmp, window)
                if index is not None:
                    break
            files.append(os.path.join(item, tmp[index]))
        try:
            return files
        finally:
            self.files = files



if __name__ == '__main__':
    a = get_video(r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\converted_videos")
    print(a.folders)
