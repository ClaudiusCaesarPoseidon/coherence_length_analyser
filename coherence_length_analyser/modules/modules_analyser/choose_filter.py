import numpy as np
from scipy.signal import savgol_filter
import scipy.signal
import scipy.fftpack


def medfilt(x, k):
    """Apply a length-k median filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    assert k % 2 == 1, "Median filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    k2 = (k - 1) // 2
    y = np.zeros((len(x), k), dtype=x.dtype)
    y[:, k2] = x
    for i in range(k2):
        j = k2 - i
        y[j:, i] = x[:-j]
        y[:j, i] = x[0]
        y[:-j, -(i + 1)] = x[j:]
        y[-j:, -(i + 1)] = x[-1]
    return np.median(y, axis=1)


def choose_filter(array, value, x):
    """choses a filter for smoothing"""
    try:
        if value == 0:
            pass
        elif value == 1:
            N = 51
            if len(array) < N:
                N = len(array)
            array_padded = np.pad(
                array, (N // 2, N - 1 - N // 2), mode='edge')
            array = np.convolve(
                array_padded, np.ones(
                    (N,)) / N, mode='valid')
        elif value == 2:
            N = 51
            O = 11
            if len(array) < N:
                N = len(array)
            if N % 2 == 0:
                N -= 1
            if O >= N:
                O = N - 1
            array = savgol_filter(array, N, O)
        elif value == 3:
            N = 51
            O = 11
            if len(array) < N:
                N = len(array)
            if N % 2 == 0:
                N -= 1
            if O >= N:
                O = N - 1
            array_padded = np.pad(
                array, (N // 2, N - 1 - N // 2), mode='edge')
            array = np.convolve(
                array_padded, np.ones(
                    (N,)) / N, mode='valid')
            array = savgol_filter(array, N, O)
        elif value == 4:
            N = 51
            if len(array) < N:
                N = len(array)
            if N % 2 == 0:
                N -= 1
            array = medfilt(array, N)
        elif value == 5:
            N = 51
            O = 11
            if len(array) < N:
                N = len(array)
            if N % 2 == 0:
                N -= 1
            if O >= N:
                O = N - 1
            array = medfilt(array, N)
            array = savgol_filter(array, N, O)
        elif value == 6:
            N = 10
            if len(array) < N:
                N = len(array)
            length = len(x)
            procent = int(length / 100)
            if procent >= 1:
                tmp = array[0:procent]
                mean1 = np.mean(tmp)
                tmp = array[-1 - procent + 1:]
                mean2 = np.mean(tmp)
                n = mean1
                m = (mean2 - n) / (x[-1])
                x_a = np.array(x)
                array_min = m * x_a + n
                array = array.astype(np.float64)
                array -= array_min
                W = scipy.fftpack.fftfreq(
                    array.size, d=x[1] - x[0])
                signal = scipy.fftpack.rfft(array)
                thresh = 1 / (2 * N * (x[1] - x[0]))
                signal[(W >= thresh)] = 0
                signal[(W <= -thresh)] = 0
                array = scipy.fftpack.irfft(
                    signal) + array_min
        elif value == 7:
            N = 10
            length = len(x)
            procent = int(length / 100)
            if procent >= 1:
                tmp = array[0:procent]
                mean1 = np.mean(tmp)
                tmp = array[-1 - procent + 1:]
                mean2 = np.mean(tmp)
                n = mean1
                m = (mean2 - n) / (x[-1])
                x_a = np.array(x)
                array_min = m * x_a + n
                array = array.astype(np.float64)
                array -= array_min
                W = scipy.fftpack.fftfreq(
                    array.size, d=x[1] - x[0])
                signal = scipy.fftpack.rfft(array)
                thresh = 1 / (2 * N * (x[1] - x[0]))
                signal[(W >= thresh)] = 0
                signal[(W <= -thresh)] = 0
                array = scipy.fftpack.irfft(
                    signal) + array_min
            N = 51
            O = 11
            if len(array) < N:
                N = len(array)
            if O >= N:
                O = N - 1
            array = savgol_filter(array, N, O)
    except ValueError:
        pass
    return array
