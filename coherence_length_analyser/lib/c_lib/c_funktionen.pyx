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

import scipy.ndimage
import scipy.signal
import math
from .resource_path import *

from .cython.parallel import prange
from numpy cimport ndarray
cimport numpy as np
cimport cython
from libcpp cimport bool as bool_t
from libc.stdint cimport uint32_t,int32_t
from numpy cimport uint8_t
from libc.stdlib cimport free

ctypedef uint32_t DWORD
ctypedef DWORD HIDS

ctypedef fused my_type:
    uint8_t
    int
    float
    double
    long long

cdef extern from "c_written_functions.c" nogil:
    void fft_shift(double*,int,int)
    void save_txt_c "save_txt" (char*,int*,int,int)
    void save_txt_double_c "save_txt_double" (char*,double*,int,int)
    cpdef int build_directory "build"(char*)
    cpdef int remove_directory "remove_c"(char*)
    cpdef double round_c(double)
    cpdef int is_admin_c "is_admin" ()
    char* vigenere_c "vigenere"(char*,char*) # cpdef -> memory leak
    void free_array(char*)


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int save_txt_int(unicode name,my_type [:,:] array):
    """Saves a 2-D array to a csv file"""
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    save_txt_c(name.encode("UTF-8"),<int *>&array[0][0],row,column)
    return 1

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int save_txt_double(unicode name,my_type [:,:] array):
    """Saves a 2-D array to a csv file"""
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    save_txt_double_c(name.encode("UTF-8"),<double *>&array[0][0],row,column)
    return 1

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray fft_shift_py(double [:,::1] arr):
    """Swicthes the 1st and 3rd; and the 2nd the 4th quadrant"""
    cdef int width=arr.shape[1]
    cdef int heigth=arr.shape[0]
    cdef double[:,::1] array=arr.copy()
    fft_shift(<double*>&array[0][0],width,heigth)
    numpy_array = np.asarray(array)
    return numpy_array


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

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef str vigenere(str string,str key):
    """encodes the text with an vigenere cipher"""
    string_p=string.encode("UTF-8")
    key_p=key.encode("UTF-8")
    cdef char* string_c=string_p
    cdef char* key_c=key_p
    string_c=vigenere_c(string_c,key_c)
    try:
        return string_c.decode("UTF-8")
    finally:
        free(string_c)
