import sys
import os
import ctypes
import math
import imghdr
import cv2
import numpy as np
import scipy.signal
from screeninfo import get_monitors
from PIL import Image, ImageChops
import serial.tools.list_ports
import serial
from . import c_funktionen
from collections import Counter
from pyueye import ueye


def Number_Of_Cameras():
    """gets number of availible uEye Cameras"""
    number = ueye.int(0)
    ueye.is_GetNumberOfCameras(number)
    return number.value


def get_frame_extremes(cam):
    """returns the maximum and minumum time bewtween frames"""
    min = ueye.double(0)
    max = ueye.double(0)
    intervall = ueye.double(0)
    ueye.is_GetFrameTimeRange(cam, min, max, intervall)
    return {'max': max.value, 'min': min.value, 'intervall': intervall.value}


def is_SetFrameRate(cam, FPS):
    """sets the framerate of the uEye camera"""
    FPS = ueye.double(FPS)
    newFPS = ueye.double()
    return ueye.is_SetFrameRate(cam, FPS, newFPS)


def Init_Cam(width=640, heigth=480, gain_boost=1):
    """inits the uEye camera"""
    # inits next available cam
    cam = ueye.HIDS(0)
    ueye.is_InitCamera(cam, None)

    ueye.is_EnableAutoExit(cam, ueye.IS_ENABLE_AUTO_EXIT)

    # sets the Colourmode of the camera
    ueye.is_SetColorMode(cam, ueye.IS_CM_SENSOR_RAW8)

    # sets the trigger
    ret = ueye.is_SetExternalTrigger(cam, ueye.IS_SET_TRIGGER_SOFTWARE)
    mode = ueye.int(0)

    # sets the blacklevel
    ueye.is_Blacklevel(
        cam,
        ueye.IS_BLACKLEVEL_CMD_SET_MODE,
        mode,
        ueye.sizeof(mode))

    # sets the size of the image
    rectAOI = ueye.IS_RECT()
    rectAOI.s32X = 44
    rectAOI.s32Y = 0
    rectAOI.s32Width = 480
    rectAOI.s32Height = 480
    ueye.is_AOI(cam, ueye.IS_AOI_IMAGE_SET_AOI, rectAOI, ueye.sizeof(rectAOI))

    # allocates memory with given size
    width = ueye.int(width)
    heigth = ueye.int(heigth)
    bitspixel = ueye.int(8)
    pcImgMem = ueye.c_mem_p()
    pid = ueye.int()
    ueye.is_AllocImageMem(cam, 480, heigth, bitspixel, pcImgMem, pid)

    # sets the image memory as active
    ueye.is_SetImageMem(cam, pcImgMem, pid)

    # activates video mode
    ueye.is_CaptureVideo(cam, ueye.IS_DONT_WAIT)

    # sets gain boost mode
    if gain_boost == 1:
        ueye.is_SetGainBoost(cam, ueye.IS_SET_GAINBOOST_ON)
    else:
        ueye.is_SetGainBoost(cam, ueye.IS_SET_GAINBOOST_OFF)
    return cam, ret, pcImgMem, pid


def BOOOOOOOOOOST(cam, mode):
    """set the gain boost mode of the camera"""
    if mode == 1:
        ueye.is_SetGainBoost(cam, ueye.IS_SET_GAINBOOST_ON)
    else:
        ueye.is_SetGainBoost(cam, ueye.IS_SET_GAINBOOST_OFF)


def Get_Values(cam, exposure):
    """gets the current exposure time and gain of the camera"""
    exposure = ueye.double(exposure)
    gain = ueye.int()
    ueye.is_Exposure(
        cam,
        ueye.IS_EXPOSURE_CMD_GET_EXPOSURE,
        exposure,
        ueye.sizeof(exposure))
    gain = ueye.is_SetHardwareGain(
        cam,
        ueye.IS_GET_MASTER_GAIN,
        ueye.IS_IGNORE_PARAMETER,
        ueye.IS_IGNORE_PARAMETER,
        ueye.IS_IGNORE_PARAMETER)
    return exposure.value, gain


def Set_Values(cam, exposure, gain, blacklevel, automode):
    """sets the exposure time and gain of the camera"""
    exposure = ueye.double(exposure)
    expo = ueye.double()
    gain = ueye.int(gain)
    # sets the exposure time and gain with the values
    # or sets them automatically
    if automode is False:
        ueye.is_SetHardwareGain(
            cam,
            gain,
            ueye.IS_IGNORE_PARAMETER,
            ueye.IS_IGNORE_PARAMETER,
            ueye.IS_IGNORE_PARAMETER)
        ueye.is_Exposure(
            cam,
            ueye.IS_EXPOSURE_CMD_SET_EXPOSURE,
            exposure,
            ueye.ueye.sizeof(exposure))
        expo = exposure
        ueye.is_Blacklevel(
            cam,
            ueye.IS_BLACKLEVEL_CMD_SET_OFFSET,
            blacklevel)
    elif automode is True:
        pval1 = ueye.double(1)
        pval2 = ueye.double(0)
        ueye.is_SetAutoParameter(
            cam, ueye.IS_SET_ENABLE_AUTO_GAIN, pval1, pval2)
        pval1 = ueye.double(1)
        pval2 = ueye.double(0)
        ueye.is_SetAutoParameter(
            cam, ueye.IS_SET_ENABLE_AUTO_SHUTTER, pval1, pval2)
    return Get_Values(cam.value, expo.value)


def CopyImg(cam, ImageData, pcImgMem, pid):
    """copys the image from the memory to a numpy array"""
    ret = ueye.is_CopyImageMem(cam, pcImgMem, pid, ImageData.ctypes.data)
    return ret


def Exit_Cam(cam, pcImgMem, pid):
    """exits the camera"""
    ueye.is_FreeImageMem(cam, pcImgMem, pid)
    ret = ueye.is_ExitCamera(cam)
    return ret


def encode(string):
    """encodes the string with the appropriate codec"""
    return c_funktionen.encode(string)


def resource_path(path):
    """returns correct path in script and in Pyinstaller exe"""
    return c_funktionen.resource_path(path)


def maxi(array, threshold=195, rangee=3, range_cross=0):
    """calculates the local maxima of the image"""
    return c_funktionen.maxi(array, threshold, rangee, range_cross)


def round_array(array, b=0):
    """round whole array"""
    return c_funktionen.round_array(array, b)


def save_txt(name, array):
    """save 2d array to csv"""
    return c_funktionen.save_txt(name, array)


def fft_shift_py(array):
    """switches 1st and 3rd, and 2nd and 4th quadrant of image"""
    return c_funktionen.fft_shift(array)


def dft(img):
    """calculates the dft of the image"""
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    return dft


def fft_cv2(dft):
    """calculates the 2d fft from the dft"""
    fft = (cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))
    fft = 20 * np.log(fft)
    maxx = np.amax(fft)
    fft = np.divide(fft, maxx)
    fft = np.multiply(fft, 255)
    return fft


def fft_cv2_clip(dft):
    """calculates the 2d ifft from the dft with clipping"""
    fft = (cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))
    fft = 20 * np.log(fft)
    fft = np.clip(fft, 0, 255)
    return fft


def ifft_cv2(dft):
    """calculates the 2d ifft from the dft"""
    # calculates the fft
    img_back = cv2.idft(dft)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    # converts the fft to uint8
    maxx = np.amax(img_back)
    img_back = np.divide(img_back, maxx)
    img_back = np.multiply(img_back, 255).astype(np.uint8)
    return img_back


def is_64():
    """checks if the programm is run with 64-bit"""
    return True if ctypes.sizeof(ctypes.c_voidp) == 8 else False


def arreq_in_list(myarr, list_arrays):
    """checks if array is in list of arrays"""
    return next(
        (True for elem in list_arrays if np.array_equal(
            elem, myarr)), False)


def set_list(lst):
    """returns a list of all tuple in the nested tuple input list"""\
        """excluding multiples"""
    # flatten list
    lst = [x for item in lst for x in item]

    # get a unique set and convert to list
    lst = list(set(lst))

    # sorts the list
    lst.sort(key=lambda x: (x[0], x[1]))
    return lst


def min__(array, percentage, mode=0):
    """calculates the lower threshold of the array"""
    if mode == 0:
        # rounds the array to 2 decimal places if is it floating number format
        if np.issubdtype(array.dtype, np.integer) is False:
            array = round_array(array, 2)

        # gets a dictionary if the number of occurences of values in the array
        # and the most common value in the array
        count = Counter(array)
        tmp = count.most_common()[0][0]

        # calculates the mean of the values, which are no more 'precentage' higher
        # or lower than the most common value
        mean_ind = np.where(
            np.logical_and(
                array >= tmp -
                tmp *
                percentage /
                100,
                array <= tmp +
                tmp *
                percentage /
                100))
        mean_array = array[mean_ind]
        return np.mean(mean_array)
    elif mode == 1:
        # calvulates the mean of the first procent and last procent of values
        procent = int(len(array) / 100)
        if procent > 0:
            tmp = array[0:procent]
            mean1 = np.mean(tmp)
            tmp = array[-1 - procent + 1:]
            mean2 = np.mean(tmp)
            return np.mean([mean1, mean2])
    else:
        return np.amin(array)


def threshold(array, percentage, mode=0):
    """calculate the 1/e-threshold,the minimum value and the"""\
        """maximum value of the 1-D array"""
    min_ = min__(array, percentage, mode=mode)
    return np.amax(array) / math.e + (1 - 1 / math.e) * \
        min_, np.amax(array), min_


def monitor_format():
    """gets the size of the first monitor"""
    return get_monitors()[0].width / get_monitors()[0].height


def trim(img):
    """removes border around image"""
    img = img + 1
    im = Image.fromarray(img)
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return np.array(im.crop(bbox))
    else:
        return np.array(im)


def rotate_image(image, angle, row, col):
    """rotates the image around its center without cropping"""
    padX = [image.shape[1] - col, col]
    padY = [image.shape[0] - row, row]
    imgP = np.pad(image, [padY, padX, [0, 0]], 'constant')
    cols, rows = imgP.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -angle, 1)
    imgR = cv2.warpAffine(imgP, M, (cols, rows))
    result = imgR
    return result


def resize(array, h_param, w_param):
    """resises the array"""
    try:
        i, j = array.shape
    except ValueError:
        return c_funktionen.resize_colour(array, h_param, w_param)
    return c_funktionen.resize(array, h_param, w_param)


def connect(port='COM23'):
    """connects the arduino for the motor controll"""
    try:
        ser = serial.Serial(port, 9600, timeout=3)
        return ser
    except serial.SerialException:
        return None


def search():
    """search for all available devices on COM-ports"""
    return list(serial.tools.list_ports.comports())


def list_connect():
    """search for the arduino and connect to it automatically"""
    ports = search()
    for p in ports:
        ser = connect(port=p[0])
        a = ser.readline().strip()
        ser.close()
        if a == b'Start':
            port = p[0]
            break
    else:
        port = None
    ser = connect(port)
    return ser


def forward(serial):
    """moves the step motor 1 half-step forward"""
    serial.write(b'1')
    serial.readline().strip()
    return 10


def backward(serial):
    """moves the step motor 1 half-step backward"""
    serial.write(b'2')
    serial.readline().strip()
    return 10


def is_float(s):
    """check if string is floating point number"""
    try:
        float(s)
    except ValueError:
        return False
    return True


def is_admin():
    """check if the script was run as an administrator"""
    is_admin_ = ctypes.windll.shell32.IsUserAnAdmin() != 0
#    is_admin_ = c_funktionen.is_admin_c() != 0
    return is_admin_


def is_pyinstaller():
    """checks if the script is run from a pyinstaller created exe"""
    try:
        sys._MEIPASS
        return True
    except AttributeError:
        return False


def is_image(path):
    """checks if file is an image"""
    if imghdr.what(path) is None:
        return False
    return True


def string_is_int(string):
    """checks if a string is an intgeger"""
    return string.isdigit()


def round(a, b=0):
    """always round half up"""
    result = 0
    if b == 0:
        return c_funktionen.round_c(a)
    result = c_funktionen.round_c(a * 10**b) / (10**b)
    return result


def kaiser(width):
    """returns a 2-D kaiser window function with the specified width"""
    x = scipy.signal.kaiser(width, 15)
    y = scipy.signal.kaiser(width, 15)
    X, Y = np.meshgrid(x, y)
    kaiser_ = X * Y
    return kaiser_


def boxcar(width):
    """returns a 2-D boxcar window function with the specified width"""
    x = scipy.signal.boxcar(width)
    y = scipy.signal.boxcar(width)
    X, Y = np.meshgrid(x, y)
    rect = X * Y
    return rect


def hanning(width):
    """returns a 2-D hanning window function with the specified width"""
    x = scipy.signal.hanning(width)
    y = scipy.signal.hanning(width)
    X, Y = np.meshgrid(x, y)
    hanning_ = X * Y
    return hanning_


#def hamming(width):
#    """returns a 2-D hamming window function with the specified width"""
#    x = scipy.signal.hamming(width)
#    y = scipy.signal.hamming(width)
#    X, Y = np.meshgrid(x, y)
#    hamming_ = X * Y
#    return hamming_

def bohman(width):
    """returns a 2-D bohman window function with the specified width"""
    x = scipy.signal.bohman(width)
    y = scipy.signal.bohman(width)
    X, Y = np.meshgrid(x, y)
    bohman_ = X * Y
    return bohman_


#def slepian(width):
#    """returns a 2-D slepian window function with the specified width"""
#    x = scipy.signal.slepian(width, 0.02)
#    y = scipy.signal.slepian(width, 0.02)
#    X, Y = np.meshgrid(x, y)
#    slepian_ = X * Y
#    return slepian_

def dolph_chebyshev(width):
    x = scipy.signal.chebwin(width, 140)
    y = scipy.signal.chebwin(width, 140)
    X, Y = np.meshgrid(x, y)
    dolph_ = X * Y
    return dolph_


def gauss(width):
    """returns a 2-D gauss window function with the specified width"""
    x = scipy.signal.gaussian(width, 0.3 * (width - 1) / 2)
    y = scipy.signal.gaussian(width, 0.3 * (width - 1) / 2)
    X, Y = np.meshgrid(x, y)
    gauss_ = X * Y
    return gauss_


def x(start, number, step_width):
    """returns an array, that begins at start has *number* elements with """\
        """*step width*"""
    return start + np.arange(number) * step_width


def substring_in_list(substring, lst):
    """checks if substring is in list of strings"""
    return any(substring in x for x in lst)


class VAL(dict):
    """creates a dictionary, whose items can be accesed like a class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__.update(**kwargs)

    def __setitem__(self, key, item):
        super().__setitem__(key, item)
        self.__dict__[key] = item


def inting(string):
    """converts string to an integer if possible, else returns None"""
    try:
        return int(string)
    except ValueError:
        return None


def toggle(button):
    """toggle the Qt Button"""
    if button.isChecked() is True:
        button.setChecked(False)
        button.setEnabled(True)
    else:
        button.setChecked(True)
        button.setEnabled(False)


def isascii(string):
    """checks if all characters in the string a available in the ASCII-table"""
    try:
        return string.isascii()
    except AttributeError:
        try:
            string.encode("ascii")
            return True
        except UnicodeEncodeError:
            return False


class search_folder:
    """gets all relevent images in folder"""

    def __init__(self, path, window="Boxcar", mode=0):
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
                if mode == 0:
                    temp = temp[-1].split(".")
                    if temp[0].isdigit() is True and temp[-1].endswith("png"):
                        self.files.append(os.path.join(item, item2))
                elif mode == 1:
                    if temp[-1].endswith("alignment2.png"):
                        self.files.append(os.path.join(item, item2))
                else:
                    raise RuntimeError("Mode not recognised")
        self.tmp = [x for x in self.tmp if substring_in_list(x, self.files)]
        self.file_names = np.array((self.files, self.tmp))
