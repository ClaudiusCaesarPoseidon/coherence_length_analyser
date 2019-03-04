from PIL import Image, ImageEnhance
import os
import shutil
import numpy as np
import cv2
from ...lib import functions
from .analyser_miscellaneous import convert
from PySide2 import QtCore


default_imread = cv2.imread
default_imwrite = cv2.imwrite


# replaces the imread function, which can not read images whose path
# contains non ASCII characters
def imread(path, mode=1):
    if functions.isascii(path) is True:
        return default_imread(path, mode)
    else:
        if mode == 0:
            return np.asarray(Image.open(path).convert('L'))
        else:
            return np.asarray(Image.open(path).convert('RGB'))


# replaces the imwrite function, which can not read images whose path
# contains non ASCII characters
def imwrite(path, image):
    if functions.isascii(path) is True:
        return default_imwrite(path, image)
    else:
        im = Image.fromarray(image)
        im.save(path)


class ptv_thread(QtCore.QThread):
    exists = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.files = self.parent.files
        self.choice = ''

    def custom_function(self, width):
        try:
            x = eval(self.parent.CustomFunction.text())
            y = x
            X, Y = np.meshgrid(x, y)
            function_ = X * Y
            return function_
        except Exception:
            print(self.parent.CustomFunction.text())
            print("The function could not be evaluated.")
            return None

    def get_window_function(self, argument, width):
        switcher = {
            "Kaiser": functions.kaiser,
            "Boxcar": functions.boxcar,
            "Hamming": functions.hamming,
            "Hanning": functions.hanning,
            "Slepian": functions.slepian,
            "Gauss": functions.gauss,
            "Custom": self.custom_function,
        }
        func = switcher.get(argument, None)
        return func(width)

    def run(self):
        cv2.imread = imread
        cv2.imwrite = imwrite

        # builds name of video
        part1 = os.path.splitext(os.path.basename(self.files[0]))[0]
        gname = os.path.dirname(self.files[0])
        timestamp = os.path.basename(gname)
        part2 = part1.split('_')
        temporary_variable_for_mode = part2[0][-1]
        del part2[0]
        del part2[0]
        part3 = '_'.join(part2)
        r = part3
        a = cv2.imread(self.files[0], 0)
        height, width = a.shape
        while True:
            self.choice = ''
            extra_name = ""

            # builds name of video with extra arguments
            if self.parent.Subtract_Background.isChecked() is True:
                extra_name += "b"
            if self.parent.Mirror_Image.isChecked() is True:
                extra_name += "f"
            vidname = 'vid' + extra_name + temporary_variable_for_mode + \
                '_' + self.parent.Windows.currentText() + "_" + part3 + ".avi"
            r = "img" + temporary_variable_for_mode + "_" + \
                self.parent.Windows.currentText() + "_%d_" + r + ".png"
            window = self.get_window_function(
                self.parent.Windows.currentText(), width)
            i = 0

            # loads the images, multiplys them with the window function
            # and saves the min an temporary folder
            for img in self.files:
                a = (cv2.imread(img, 0) * window).astype(np.uint8)
                if i == 0:
                    background = a
                print("Processing image %d" % i)
                path_output = os.path.abspath(os.path.join(
                    os.path.dirname(img), '..', "output"))
                if os.path.isdir(path_output) is False:
                    functions.build_directory(path_output)
                if self.parent.Mirror_Image.isChecked() is True:
                    a = cv2.flip(a, 1)
                if self.parent.Subtract_Background.isChecked() is True:
                    a = cv2.subtract(a, background)
                    im = Image.fromarray(a)
                    enhancer = ImageEnhance.Contrast(im)
                    enhanced_im = enhancer.enhance(4.0)
                    a = np.asarray(enhanced_im)
                cv2.imwrite(
                    os.path.join(
                        path_output,
                        'img' +
                        temporary_variable_for_mode +
                        "_" +
                        self.parent.Windows.currentText() +
                        "_%d_" %
                        i +
                        part3 +
                        ".png"),
                    a)
                i += 1
            ffmpeg_img_path = os.path.join(path_output, r)
            if os.path.isdir(
                os.path.join(
                    self.parent.parent.direc_path,
                    "converted_videos")) is False:
                functions.build_directory(os.path.join(
                    self.parent.parent.direc_path, "converted_videos"))
            if os.path.isdir(
                os.path.join(
                    self.parent.parent.direc_path,
                    "converted_videos",
                    timestamp)) is False:
                functions.build_directory(
                    os.path.join(
                        self.parent.parent.direc_path,
                        "converted_videos",
                        timestamp))
            ffmpeg_vid_path = os.path.join(
                self.parent.parent.direc_path,
                "converted_videos",
                timestamp,
                vidname)
            print("Video Path:", ffmpeg_vid_path)
            if os.path.exists(ffmpeg_vid_path) is True:
                print("File %s already exists" % ffmpeg_vid_path)
                print("Please choose option how to proceed.")
                self.exists.emit(1)
                while True:
                    if self.parent.value == 1:
                        self.choice = "nein"
                        self.parent.value = 0
                        break
                    elif self.parent.value == 7:
                        self.parent.value = 0
                        txt = self.parent.dialogg.Again.currentText()
                        index = self.parent.Windows.findText(txt)
                        self.parent.Windows.setCurrentIndex(index)
                        self.choice = "again"
                        break
                    elif self.parent.value == 10:
                        self.parent.value = 0
                        os.remove(ffmpeg_vid_path)
                        self.choice = "ja"
                        break
            if self.choice == "nein":
                break
            if self.choice == "again":
                continue

            # converts the images to video
            convert(os.path.dirname(ffmpeg_img_path), ffmpeg_vid_path, 2)

            # removes the temporary folder
            shutil.rmtree(os.path.dirname(ffmpeg_img_path))
            if self.choice == "ja":
                break
            break
        self.parent.is_end = True
