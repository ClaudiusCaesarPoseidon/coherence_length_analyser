from PIL import Image
from ...lib import functions
import math
import os
import datetime
import numpy as np
import cv2
import qimage2ndarray
from PySide2 import QtCore, QtGui


default_imwrite = cv2.imwrite

# replaces the imwrite function, which can not read images whose path
# contains non ASCII characters


def imwrite(path, image):
    if path.isascii() is True:
        return default_imwrite(path, image)
    else:
        im = Image.fromarray(image)
        im.save(path)


class Measure(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)
    do = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.number = self.parent.Step_Width
        self.Current = self.parent.Current
        self.Temperature = self.parent.Temperature
        self.ID = self.parent.ID
        self.Max_Width = self.parent.Max_Width
        self.i = 0
        self.j = 0
        self.step = float(self.number.text()) * 0.11
        self.max_int = math.ceil(float(self.Max_Width.text()) / self.step)
        self.img = np.zeros((480, 480), dtype=np.uint8)
        self.mode = self.parent.Mode.currentText().lower()
        self.string_direc = None
        self.string_direc2 = None
        self.ends = None
        self.th = None

    def run(self):
        # create unique directory
        self.direc_name = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S") + "_" + self.ID.text() + \
            "_" + self.Max_Width.text() + '_' + self.Temperature.text() + \
            "_" + self.Current.text()
        self.string_direc = os.path.join(
            self.parent.direc_path, self.direc_name)
        try:
            os.makedirs(self.string_direc, exist_ok=True)
            ret1 = 0
        except OSError:
            ret1 = 1

        self.parent.thread_run = True
        if self.parent.failed is True:
            ret1 = 1
        if ret1 == 1:
            pass
        else:
            ImageData = functions.np.zeros(
                (480, 480), dtype=functions.np.uint8)
            exposure = 0.0
            gain = 50
            if self.parent.Lock.isChecked() is False:
                exposure, gain = functions.Set_Values(
                    self.parent.cam, exposure, gain, 114, True)
            else:
                if self.parent.exposure_saved is not None and self.parent.gain_saved is not None:
                    exposure, gain = self.parent.exposure_saved, self.parent.gain_saved
                    exposure, gain = functions.Set_Values(
                        self.parent.cam, exposure, gain, 114, False)
                else:
                    exposure, gain = functions.Set_Values(
                        self.parent.cam, exposure, gain, 114, True)
            start = True
            print('Start')
            mode = None
            if self.mode == "forward":
                mode = 'f'
            elif self.mode == "backward":
                mode = 'b'
            while True:
                if self.parent.failed is True:
                    break
                if self.parent.ret == 0:
                    if start is True:
                        self.sleep(2)
                        start = False
                        exposure, gain = functions.Get_Values(
                            self.parent.cam, exposure)
                    exposure, gain = functions.Set_Values(
                        self.parent.cam, exposure, gain, 114, False)
                    # copy image from memory to numpy array
                    functions.CopyImg(
                        self.parent.cam,
                        ImageData,
                        self.parent.pcImgMem,
                        self.parent.pid)
                    self.img = ImageData.copy()
                    self.img = np.roll(self.img, 15, axis=0)

                    # calculate fft
                    dft = functions.dft(self.img)
                    fft = functions.fft_cv2(dft)
                    fft = functions.fft_shift_py(
                        fft.astype(np.float64)).astype(np.uint8)

                    # display image
                    res = np.concatenate((self.img, fft), axis=0)
                    convertToQtFormat = qimage2ndarray.gray2qimage(res)
                    p = convertToQtFormat.scaled(
                        self.parent.bild_width,
                        self.parent.bild_height,
                        QtCore.Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)

                    # save imgae in directory
                    print("step\t" + str(self.j + 1) + "/" + str(self.max_int)
                          + "\t " + str(self.parent.i) + "/" +
                          str(self.parent.number_of_measurements))
                    if mode is not None:
                        tmp1 = "img" + mode
                        tmp2 = "_%d_" % self.j + self.Max_Width.text()
                        tmp3 = '_' + self.Temperature.text() + "_" + self.Current.text()
                        tmp4 = "_" + self.number.text() + ".png"
                        tmp5 = tmp1 + tmp2 + tmp3 + tmp4
                        cv2.imwrite(os.path.join(
                            self.string_direc2, tmp5), self.img)
                    else:
                        tmp1 = "img"
                        tmp2 = "_%d_" % self.j + self.Max_Width.text()
                        tmp3 = '_' + self.Temperature.text() + "_" + self.Current.text()
                        tmp4 = "_" + self.number.text() + ".png"
                        tmp5 = tmp1 + tmp2 + tmp3 + tmp4
                        cv2.imwrite(os.path.join(
                            self.string_direc2, tmp5), self.img)

                    # end if max width is reached
                    if self.i < float(self.Max_Width.text()):
                        for k in range(int(self.number.text())):
                            if self.parent.failed is True:
                                break
                            if self.mode == "forward":
                                tmp = self.parent.position.copy()
                                tmp[0][0] += 0.11
                                self.parent.position = tmp
                            elif self.mode == "backward":
                                tmp = self.parent.position.copy()
                                tmp[0][0] -= 0.11
                                self.parent.position = tmp
                            params = (self.parent.ser,)
                            getattr(functions, self.mode)(*params)
                            functions.save_txt(
                                self.parent.pos_path, self.parent.position)
                            self.msleep(10)
                        self.do.emit()
                        self.i += self.step
                        self.j += 1
                        self.msleep(150)
                    else:
                        self.ends = True
                if self.i >= float(self.Max_Width.text()):
                    break
                if self.parent.ends is True:
                    break
                if self.parent.failed is True:
                    break
        print("Finished")
