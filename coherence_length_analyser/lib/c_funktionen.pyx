# tag: openmp
# cython: infer_types=True
# cython: language_level=3
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp
import cv2
import numpy as np
import serial
import timeit
import os
from encodings.aliases import aliases
import sys
_names = sys.builtin_module_names

import scipy.ndimage
import scipy.signal
import math
#from .resource_path import *

from .cython.parallel import prange
from numpy cimport ndarray
cimport numpy as np
cimport cython
from libcpp cimport bool as bool_t
from libc.stdint cimport uint32_t,int32_t
from numpy cimport uint8_t
#from libc.stdlib cimport free
from libc.stdio cimport FILE, fopen, fprintf, fclose

ctypedef uint32_t DWORD
ctypedef DWORD HIDS

ctypedef fused my_type:
    uint8_t
    int
    float
    double
    long long

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef unicode resource_path(unicode relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        if os.path.exists(os.path.abspath(relative_path)) is True:
            base_path=os.path.abspath(".")
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


cpdef list get_codecs(limiter=None):
    """gets all available codecs"""
    if limiter is not None:
        if isinstance(limiter, str):
            return [x for x in set(aliases.values()) if limiter in x]
        else:
            raise ValueError("Limiter must be a string.")
    else:
        return list(set(aliases.values()))


cpdef char* encode(unicode string):
    """encodes the string with the appropriate codec"""
    codecs = get_codecs('cp')
    for codec in codecs:
        try:
            return string.encode(codec)
        except UnicodeEncodeError:
            pass
#        finally:
#            print(codec)


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef list split_path(path):
    path_list = []
    if os.path.isabs(path) is True:
        path = path.split(os.sep)
        for item in path:
            path_list.append(item)
        if os.name == 'nt':
            path_list[0] = os.path.join(path_list[0], os.sep)
        else:
            path_list[0] = os.sep
    else:
        path = path.split(os.sep)
        for item in path:
            path_list.append(item)
    return path_list

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef list get_recursive_list(unicode path):
    lst = split_path(path)
    direc_list = []
    last_direc = ""
    for item in lst:
        direc = os.path.join(last_direc, item)
        last_direc = direc
        direc_list.append(direc)
    if os.path.isabs(path) is True:
        del direc_list[0]
    return direc_list



@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int save_txt(unicode name,ndarray array):
    """Saves a 2-D int array to a csv file"""
    temp = name.encode("UTF-8")
    cdef char* name_c = temp
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    cdef FILE *fp1
    fp1 = fopen(name_c, "w")
    cdef int i
    cdef double tmp
    array = array.reshape(row*column)
    if np.issubdtype(array.dtype, np.integer) is True:
        base = "%d%s"
    else:
        base = "%0.5f%s"
    for i in range(row*column):
        tmp = array[i]
        if i%column < column - 1:
            string = (base%(tmp,",")).encode("UTF-8")
        else:
            string = (base%(tmp,"\n")).encode("UTF-8")
        fprintf(fp1, string)
    fclose(fp1)
    return 1


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef double round_c(double number) nogil:
    return <double>(<int>(number + 0.5)) if number >= 0\
      else <double>(<int>(number - 0.5))


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray fft_shift(ndarray arr):
    """Swicthes the 1st and 3rd; and the 2nd the 4th quadrant"""
    cdef Py_ssize_t width=arr.shape[1]
    cdef Py_ssize_t height=arr.shape[0]
    arra = arr.copy()
    arra = arra.reshape(width * height)
    cdef double[::1] array = arra
    cdef Py_ssize_t r_h = <int>(width/2)
    cdef Py_ssize_t c_h = <int>(height/2)
    cdef Py_ssize_t m1to3 = height*c_h+c_h
    cdef Py_ssize_t m2to4 = height*c_h-c_h
    cdef Py_ssize_t i
    cdef double tmp
    for i in prange(width*height, nogil=True):
        if i/width < r_h and i%width < c_h:
            tmp = array[i+m1to3]
            array[i+m1to3] = array[i];
            array[i] = tmp;
        elif i/width < r_h and i%width >= c_h:
            tmp = array[i+m2to4];
            array[i+m2to4] = array[i];
            array[i] = tmp;
    arra = arra.reshape(height, width)
    return arra


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray resize(my_type[:,::1] a,double h_param, double w_param):
    """resize a 2-D array (greyscale image)"""
    cdef Py_ssize_t heigth=<int>(round_c(a.shape[0]*h_param))
    cdef Py_ssize_t width=<int>(round_c(a.shape[1]*w_param))
    cdef Py_ssize_t j_n
    cdef Py_ssize_t i_n
    cdef Py_ssize_t i, j
    if my_type is int:
        dtype = np.int
    elif my_type is double:
        dtype = np.double
    elif my_type is cython.longlong:
        dtype = np.longlong
    elif my_type is uint8_t:
        dtype=np.uint8
    elif my_type is float:
        dtype = np.float32
    result = np.zeros((heigth, width), dtype=dtype)
    cdef my_type[:,::1] result_view = result
    for j in prange(heigth, nogil=True):
        j_n=<int>(j/h_param)
        for i in range(width):
            i_n=<int>(i/w_param)
            result_view[j,i]=a[j_n,i_n]
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray resize_colour(my_type[:,:,::1] a,double h_param, double w_param):
    """resize a 3-D array (colour image)"""
    cdef Py_ssize_t heigth=<int>(round_c(a.shape[0]*h_param))
    cdef Py_ssize_t width=<int>(round_c(a.shape[1]*w_param))
    cdef Py_ssize_t j_n
    cdef Py_ssize_t i_n
    cdef Py_ssize_t i, j
    if my_type is int:
        dtype = np.int
    elif my_type is double:
        dtype = np.double
    elif my_type is cython.longlong:
        dtype = np.longlong
    elif my_type is uint8_t:
        dtype=np.uint8
    elif my_type is float:
        dtype = np.float32
    result = np.zeros((heigth, width,3), dtype=dtype)
    cdef my_type[:,:,::1] result_view = result
    for j in prange(heigth, nogil=True):
        j_n=<int>(j/h_param)
        for i in range(width):
            i_n=<int>(i/w_param)
            result_view[j,i,0]=a[j_n,i_n,0]
            result_view[j,i,1]=a[j_n,i_n,1]
            result_view[j,i,2]=a[j_n,i_n,2]
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef double round_cy(double a,int b=0) nogil:
    """import c-round"""
    cdef double result=0
    if b==0:
        return round_c(a)
    result=round_c(a*10**b)/(10**b)
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray round_array(ndarray a, int b=0):
    """rounds the whole array"""
    cdef Py_ssize_t i
    cdef int length = a.shape[0]
    cdef double[::1] array_view = a
    for i in prange(length, nogil=True):
        array_view[i] = round_cy(array_view[i], b)
    return a

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray cross(ndarray array, range_cross=0):
    """creates a black cross in the center"""
    cdef int row=array.shape[0]-1
    cdef int col=array.shape[1]-1
    cdef int rowh = int((row+1)/2)
    cdef int colh = int((col+1)/2)
    row = row + 1
    col = col + 1
    cdef Py_ssize_t range_cross_c = range_cross
    cdef Py_ssize_t i, j, k = 0
    array_k = array.astype(np.float64)
    cdef double [:,::1] array_view = array_k
    for i in prange(row, nogil=True):
        for j in range(range_cross_c*2):
            k = colh - range_cross_c + j
            array_view[i,k] = 0
    for i in prange(col, nogil=True):
        for j in range(range_cross_c*2):
            k = rowh - range_cross_c + j
            array_view[k,i] = 0
    array = array_k.astype(np.uint8)
    return array

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray border(ndarray array):
    """sets the image border to 0"""
    cdef int row = array.shape[0]
    cdef int col = array.shape[1]
    cdef Py_ssize_t i, j
    array_k = array.astype(np.float64)
    cdef double [:,::1] array_view = array_k
    for i in prange(row, nogil=True):
        array_view[i,0] = 0
        array_view[i,col-1] = 0
    for i in prange(col, nogil=True):
        array_view[0,i] = 0
        array_view[row-1,i] = 0
    array = array_k.astype(np.uint8)
    return array

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray maxi(ndarray array, int threshold=195, int rangee=3, range_cross=0):
    """get local maxima of image"""
    cdef int row=array.shape[0]-1
    cdef int col=array.shape[1]-1
    cdef int rowh = int((row+1)/2)
    cdef int colh = int((col+1)/2)
    if rangee%2==0:
        rangee+=1
    f=np.ones((rangee,rangee))
    f[int(math.floor(rangee/2))][int(math.floor(rangee/2))]=0
    cond1a = array > scipy.ndimage.maximum_filter(
    array, footprint=f, mode='constant', cval=-np.inf)
    cond1b=array>threshold
    cond1c=np.logical_and(cond1a,cond1b)
    cond1c[rowh,colh] = 0
    cond1d = array<250
    cond1c = np.logical_and(cond1c, cond1d)
    cond1c = cross(cond1c,range_cross).astype(np.bool)
    cond1c = border(cond1c).astype(np.bool)
    b=np.argwhere(cond1c==True)
    return b
