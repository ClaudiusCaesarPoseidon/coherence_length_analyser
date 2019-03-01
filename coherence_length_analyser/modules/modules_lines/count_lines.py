from ...lib import functions
import os
import numpy as np
import scipy.signal
import scipy.fftpack
from PySide2 import QtCore, QtGui


substring_in_list = functions.substring_in_list
VAL = functions.VAL


def get_column(nested_list, i):
    return [row[i] for row in nested_list]


class count_thread(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)
    changePixmap2 = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if self.parent is not None:
            self.direc_path = self.parent.direc_path

    def run(self):
        path = os.path.join(self.direc_path, "lines_csv")

        # loads angle.txt and converts it to a list
        with open(os.path.join(self.direc_path, "angles.txt"), "r") as file:
            tmp = file.read()
        tmp = tmp.split("\n")
        tmp[:] = [x.split('\t') for x in tmp]

        # parses the list multiple list by columns
        names = get_column(tmp, 0)
        angles = get_column(tmp, 1)
        lc = []
        for i in range(2, 100): # everything after name and angle
            try:
                lc.append(get_column(tmp, i))
            except IndexError:
                break
        z = lc[0] # window name
        lc = [y for y in lc if z[0] not in y] # remove the window name from the list
        lc.insert(0, z) # insert the window name once at the beginning
        tmp = []
        for j in range(len(lc[0])):
            for i in range(len(lc)):
                if ')' in lc[i][j] and ');' not in lc[i][j]:
                    tmp.append(lc[i][j] + "ö") # adds ö at file line end
                else:
                    tmp.append(lc[i][j])

        # convert list to string
        tmp = (' '.join(tmp))
        # add space at the begging
        tmp = " " + tmp
        # split string at every ö
        tmp = tmp.split("ö")
        # removes empty string
        try:
            tmp.remove("")
        except ValueError:
            pass
        lc = tmp

        # create dictionary with names as key and; angle and coherence length
        # as values
        tmp = [[item, item2] for item, item2 in zip(angles, lc)]
        self.values = VAL(**dict(zip(names, tmp)))

        # list of csv files
        tmp = [os.path.join(path, item) for item in os.listdir(path)]

        for item in tmp:
            # loads the csv file into a numpy array
            a = np.loadtxt(item, delimiter=",")
            a = a.transpose()
            a = np.delete(a, (0), axis=0)

            # convert the array to graysacle
            b = ((a[0] + a[1] + a[2]) // 3 + 0.0).astype(np.uint8)

            # smooth the graph with FFT- and savitzky-golay filter
            N = 5
            length = len(b)
            procent = int(length / 100)
            x = np.arange(length)
            tmp = b[0:procent]
            mean1 = np.mean(tmp)
            tmp = b[-1 - procent + 1:]
            mean2 = np.mean(tmp)
            n = mean1
            m = (mean2 - n) / (x[-1])
            b_min = m * x + n
            b = b.astype(np.float64)
            b -= b_min
            W = scipy.fftpack.fftfreq(b.size, d=x[1] - x[0])
            signal = scipy.fftpack.rfft(b)
            thresh = 1 / (2 * N * (x[1] - x[0]))
            signal[(W >= thresh)] = 0
            signal[(W <= -thresh)] = 0
            b = scipy.fftpack.irfft(signal) + b_min
            N = 51
            O = 11
            b = scipy.signal.savgol_filter(b, N, O)

            # find peaks
            temp = scipy.signal.find_peaks(b, prominence=10)
            result = len(temp[0])

            # save result in file (append)
            self.dirname = os.path.splitext(os.path.basename(item))[0]
            value = '\t'.join(getattr(self.values, self.dirname))
            print(self.dirname + "\t" + str(result) + "\t" + value)
            with open(os.path.join(self.direc_path, "lines.txt"), "a+") as file:
                file.seek(0)
                dump = file.read().split("\n")
            if dump[0] == '':
                del dump[0]
            i = 0
            for line in dump:
                if self.dirname in line:
                    dump[i] = self.dirname + "\t" + str(result) + "\t" + value
                i += 1
            if substring_in_list(self.dirname, dump) is True:
                pass
            else:
                dump.append(self.dirname + "\t" + str(result) + "\t" + value)
            with open(os.path.join(self.direc_path, "lines.txt"), "w") as file:
                file.write("\n".join(dump))
