from .choose_filter import choose_filter
import matplotlib.ticker as ticker
from ...lib import functions
from pymediainfo import MediaInfo
import os
import ctypes
import cv2
import numpy as np
import qimage2ndarray
from PySide2 import QtCore, QtGui

substring_in_list = functions.substring_in_list

# get dpi of monitor
LOGPIXELSX = 88
LOGPIXELSY = 90
dc = ctypes.windll.user32.GetDC(0)
h_dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
v_dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSY)
ctypes.windll.user32.ReleaseDC(0, dc)


class pyplot_cv2(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ind = None
        self.save = False
        self.ax = None
        self.indexes = None

    def run(self):
        indexes = []
        self.ind = None
        self.ax = self.parent.canvas.figure.add_subplot(111)
        path = self.parent.fname
        file_name = os.path.splitext(os.path.basename(path))[0]
        file_direc = os.path.dirname(path)
        step_width = float(os.path.splitext(
            os.path.basename(path).split("_")[-1])[0]) * 0.11
        video = False
        # check if file is video
        if os.path.exists(path):
            fileInfo = MediaInfo.parse(path)
            for track in fileInfo.tracks:
                if track.track_type == "Video":
                    video = True
                    break
            else:
                print("Please choose a correct File.")
        else:
            print("The File does not exist.")
        if video is True and self.parent.ends is False:
            # check if Use is toggled
            if self.parent.Use.isChecked() is False:
                print(
                    "The first run is to determine the location of the peak in the fft.")
                print(
                    "The time this will take depends on the number of frames and the visibility of the peak.")
                print("Please wait.")
                cap = cv2.VideoCapture(path)
                frame_number = None
                max_count = 190  # 255 204 216 190
                i = 0
                while True:
                    if self.parent.ends is True:
                        break
                    ret, frame = cap.read()
                    if ret is True:
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    else:
                        i = 0
                        print("Checking Threshold: ", max_count)
                        indexes = functions.set_list(indexes)
                        self.indexes = indexes
                        if len(indexes) > 0:
                            if len(indexes) == 0:
                                self.ind = tuple((indexes[0])[0])
                            else:
                                ind = []
                                inde = []
                                # find index with maximum itensity
                                for index in indexes:
                                    cap.set(
                                        cv2.CAP_PROP_POS_FRAMES, frame_number)
                                    ret, frame = cap.read()
                                    c = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    dft = functions.dft(c)
                                    fft = functions.fft_cv2(dft)
                                    fft = functions.fft_shift_py(
                                        fft.astype(np.float64)).astype(np.uint8)
                                    row, col = fft.shape
                                    h_fft, w_fft = fft.shape
                                    row, col = int(row / 2), int(col / 2)
                                    tmp_value = int(
                                        int(self.parent.Section_Size_Text.text()) / 2)
                                    section = fft[row -
                                                  tmp_value:row +
                                                  tmp_value, col -
                                                  tmp_value:col +
                                                  tmp_value]
                                    tempo = tuple(index)
                                    ind.append(tempo)
                                    inde.append(section[tempo])
                                    try:
                                        if inde[1] > inde[0]:
                                            del ind[0]
                                            del inde[0]
                                        else:
                                            del ind[-1]
                                            del inde[-1]
                                    except IndexError:
                                        pass
                                self.ind = ind[0]
                            break
                        else:
                            frame_number = None
                            max_count -= 1
                        if max_count <= 0:
                            print("No Peak found")
                            break
                        cap = cv2.VideoCapture(path)
                        ret, frame = cap.read()
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    dft = functions.dft(c)
                    fft = functions.fft_cv2(dft)
                    fft = functions.fft_shift_py(
                        fft.astype(np.float64)).astype(np.uint8)
                    row, col = fft.shape
                    h_fft, w_fft = fft.shape
                    row, col = int(row / 2), int(col / 2)
                    tmp_value = int(
                        int(self.parent.Section_Size_Text.text()) / 2)
                    section = fft[row - tmp_value:row +
                                  tmp_value, col - tmp_value:col + tmp_value]
                    h_sec, w_sec = section.shape
                    for glubber in range(11, 2, -2):  # 11 - 3

                        # find maxima in FFT
                        points = functions.maxi(
                            section, max_count, glubber, 0)
                        if len(points) > 0:
                            points = tuple(map(tuple, points))
                            indexes.append(points)
                            frame_number = i
                            break
                    i += 1

            else:
                self.ind = (self.parent.Spin_Row.value(),
                            self.parent.Spin_Col.value())
                print("Skipping Peak Detectcion. Using provided Peak Location.")
            print("The second run is to determine the theshold value.")
            print("Please wait.")
            cap = cv2.VideoCapture(path)
            data = []
            x = []
            i = 0
            if video is True and self.parent.ends is False:

                # save the intensity values of the FFT at the location
                # of the peak and the relative motor position in lists
                while True:
                    if self.parent.ends is True:
                        break
                    ret, frame = cap.read()
                    if ret is False:
                        break
                    else:
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        dft = functions.dft(c)
                        fft = functions.fft_cv2(dft)
                        fft = functions.fft_shift_py(
                            fft.astype(np.float64)).astype(np.uint8)
                        row, col = fft.shape
                        h_fft, w_fft = fft.shape
                        row, col = int(row / 2), int(col / 2)
                        tmp_value = int(
                            int(self.parent.Section_Size_Text.text()) / 2)
                        section = fft[row - tmp_value:row + tmp_value,
                                      col - tmp_value:col + tmp_value]
                        h_sec, w_sec = section.shape
                        data.append(section[self.ind])
                        x.append(step_width * i)
                        i += 1

            # calculates threshold value
            if video is True and self.parent.ends is False:
                data_a = np.array(data)
                tmp_for_filter = self.parent.Filter_Switch.currentIndex()
                data_a = choose_filter(data_a, tmp_for_filter, x)
                threshold, maxi, mini = functions.threshold(
                    data_a, 7.5)
                data_threshold = [threshold] * len(data)
                data_maxi = [maxi] * len(data)
                data_mini = [mini] * len(data)
                array_max = np.argmax(data_a)

                cap.set(cv2.CAP_PROP_POS_FRAMES, array_max)
                ret, frame = cap.read()
                c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                dft = functions.dft(c)
                fft = functions.fft_cv2(dft)
                fft = functions.fft_shift_py(
                    fft.astype(np.float64)).astype(np.uint8)
                row, col = fft.shape
                h_fft, w_fft = fft.shape
                row, col = int(row / 2), int(col / 2)
                tmp_value = int(
                    int(self.parent.Section_Size_Text.text()) / 2)
                section = fft[row - tmp_value:row + tmp_value,
                              col - tmp_value:col + tmp_value]
                h_sec, w_sec = section.shape
                section = cv2.cvtColor(
                    section, cv2.COLOR_GRAY2BGR)
                section[self.ind] = [0, 0, 255]

                # save FFT and image at maximum intensity
                if self.parent.demo is False:
                    cv2.imwrite(os.path.join(
                        file_direc, file_name + "_alignment2.png"), c)
                    cv2.imwrite(
                        os.path.join(
                            file_direc,
                            file_name +
                            "_alignment_%d.png" %
                            tmp_value),
                        section)

                # display FFT and image at maximum intensity
                section = functions.resize(
                    section, h_fft / h_sec, w_fft / w_sec)
                c = cv2.cvtColor(
                    c, cv2.COLOR_GRAY2BGR)
                fft = cv2.cvtColor(
                    fft, cv2.COLOR_GRAY2BGR)
                res = np.concatenate(
                    (c, fft, section), axis=1)
                convertToQtFormat = qimage2ndarray.array2qimage(
                    res).rgbSwapped()
                p_cv2 = convertToQtFormat.scaled(
                    self.parent.cv2_width,
                    self.parent.cv2_height,
                    QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p_cv2)
                print("The third run is to determine the coherence length.")
                print("Please wait.")

            if video is True and self.parent.ends is False:
                # set matplotlib image dpi
                self.parent.canvas.figure.set_dpi(h_dpi)
                self.parent.canvas.figure.set_size_inches(
                    self.parent.pyplot_width / h_dpi, self.parent.pyplot_height / h_dpi)
                self.ax.clear()
                if x[-1] >= 50:
                    self.ax.xaxis.set_major_locator(
                        ticker.MultipleLocator(10))
                self.ax.margins(x=0)

                # plot graph
                self.ax.plot(x, data_a, color="black")
                self.ax.plot(x, data_threshold, color="red")
                self.ax.plot(x, data_maxi, color="cyan")
                self.ax.plot(x, data_mini, color="magenta")

                # calculate coherence length by
                # finding the position of the first value above the treshold
                # and the position of the first value under the treshold and
                # after the maximum and calculating the distance between
                # theese points
                if self.parent.Calculate.isChecked() is True:
                    s = -1
                    e = 0
                    for i, item in zip(x, data_a):
                        if self.parent.ends is True:
                            break
                        j = i / step_width
                        if item > threshold and s == -1:
                            s = j
                        elif item < threshold and s != -1 and e == 0 and j > array_max:
                            e = j
                    print(
                        "The Coherence Length is:",
                        (e - s) * step_width)
##################################################################################
                     # add the parameters to the plot
                    self.ax.axvline(s * step_width, color="green")
                    self.ax.axvline(e * step_width, color="green")
                    self.parent.canvas.figure.text(
                        0.0, 0.97, "Results:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.94, "First Occurence:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.91, "%0.2f" %
                        (s * step_width), fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.89, "Last Occurence:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.86, "%0.2f" %
                        (e * step_width), fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.83, "Coherence Length:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(0, 0.81, "%0.2f" % (
                        (e - s) * step_width), fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.78, "Maximum Value:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.75, "%0.2f" % maxi, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.72, "Minumum Value:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.69, "%0.2f" % mini, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.66, "Threshold Value:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.63, "%0.2f" %
                        threshold, fontsize=8, zorder=10)
##################################################################################
                    # save plot as png
                    self.parent.canvas.figure.text(
                        0, 0.16, filter_string, fontsize=8, zorder=10)
                    self.parent.canvas.canvas.draw()
                    cap.release()
                    if self.parent.demo is False:
                        tmp_array = np.column_stack((x, data_a))
                        self.parent.canvas.figure.savefig(
                            os.path.join(
                                file_direc,
                                file_name +
                                "_" +
                                filter_name +
                                ".png"),
                            format="png",
                            dpi=h_dpi)
                        functions.save_txt(
                            os.path.join(
                                file_direc,
                                file_name +
                                "_" +
                                filter_name +
                                "_" +
                                (
                                    self.parent.Section_Size_Text.text()) +
                                ".csv"),
                            tmp_array)

                        # save the coherence length in a text file
                        window = file_name.split("_")[1]
                        with open(os.path.join(file_direc, "coherence_length.txt"), "a+") as file:
                            file.seek(0)
                            dump = file.read().split("\n")
                        if dump[0] == '':
                            del dump[0]
                        i = 0
                        for line in dump:
                            if window in line and filter_name in line:
                                dump[i] = window + "\t" + filter_name + "\t" + \
                                    "%0.2f" % (
                                        (e - s) * step_width) + str(self.ind)
                            i += 1
                        if substring_in_list(
                                window + "\t" + filter_name, dump) is True:
                            pass
                        else:
                            dump.append(window +
                                        "\t" +
                                        filter_name +
                                        "\t" +
                                        "%0.2f" %
                                        ((e -
                                          s) *
                                         step_width) +
                                        str(self.ind))
                        with open(os.path.join(file_direc, "coherence_length.txt"), "w") as file:
                            file.write("\n".join(dump))
