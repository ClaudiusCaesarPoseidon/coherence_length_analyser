# tag: openmp
# cython: infer_types=True
# cython: language_level=3
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp
import cv2
import numpy as np
import lib.uEye as uEye
import serial.tools.list_ports
import serial
import timeit
import os
import sys

import scipy.ndimage
import scipy.signal
import math
import imghdr
from lib.resource_path import *

from cython.parallel import prange
from numpy cimport ndarray
cimport numpy as np
cimport cython
cimport lib.uEye as uEye
from libcpp cimport bool as bool_t
from libc.stdint cimport uint32_t,int32_t
from numpy cimport uint8_t
from libc.stdlib cimport free

ctypedef uint32_t DWORD
ctypedef DWORD HIDS

ctypedef fused my_type:
    uint8_t
    int
    double
    long long

cdef extern from "c_written_functions.c" nogil:
    int make_directory(char*)
    int delete_directory(char*)
    void fft_shift(double*,int,int)
    void save_txt_c "save_txt" (char*,int*,int,int)
    void save_txt_double_c "save_txt_double" (char*,double*,int,int)
    void square_array_c "square_array" (int*,int,int,int,int,int)
    void truncuate_array_c "truncuate_array" (int*,int,int,int,int)
    double round_c(double)
    void circle_c "circle"(int*,int,int,int,int,int)
    void save_img(char*,int*,int,int)
    char* vigenere_c "vigenere"(char*,char*)
    cpdef int build_directory "build"(char*)
    cpdef int remove_directory "remove_c"(char*)
    cpdef int is_admin_c "is_admin" ()

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def save_img_c(unicode name,int [:,:] array):
    """Saves a 2-D array to a pgm file"""
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    save_img(name.encode("UTF-8"),<int *>&array[0][0],row,column)
    return 1

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def list_string_to_int(str l, dtype=int):
    """converts a list of strings to a list of integers"""
    ll=l.split(sep=',')
    try:
        return list(map(dtype, ll))
    except ValueError:
        return []

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef np.ndarray square_array_cy(int [:,::1] array,int threshold, int minn=0,int maxx=255):
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    cdef int[:,::1] arr=array.copy()
    square_array_c(<int*>&arr[0][0],column,row,threshold,minn,maxx)
    return np.asarray(arr)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef np.ndarray truncuate_array_cy(int [:,::1] array,int threshold, int minn=0):
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    cdef int[:,::1] arr=array.copy()
    truncuate_array_c(<int*>&arr[0][0],column,row,threshold,minn)
    return np.asarray(arr)

def square_array(np.ndarray array,int threshold, int minn=0,int maxx=255):
    """set all values of the array under the trehsold to min and all values over the threshold to max"""
    dtype=array.dtype
    arr=(square_array_cy(array.astype(np.int),threshold,minn,maxx)).astype(dtype)
    return arr

def truncuate_array(np.ndarray array,int threshold, int minn=0):
    """set all values of the array under the trehsold to min"""
    dtype=array.dtype
    arr=(truncuate_array_cy(array.astype(np.int),threshold,minn)).astype(dtype)
    return arr

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def check_ffmpeg():
    """check if ffmpeg is in PATH"""
    check_list=[]
    for i in os.environ['PATH'].split(";"):
        if os.path.isfile(i+"\\ffmpeg.exe") is True:
            check_list.append(i)
    if len(check_list)>1:
        pass
    elif len(check_list)==1:
        pass
    else:
        return None
    return check_list[0]

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def get_var_value(str filename="varstore.txt"):
    """get value from varstore.txt"""
    cdef int val
    with open(filename, "r+") as f:
        val = int(f.read()) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def expand_1d_2d(my_type[::1] array,int row=480,int col=480):
    """expand a 1-D array to 2-D"""
    cdef int numb=array.shape[0]
    a=np.zeros((numb,numb),dtype=np.uint8)
    cdef int maxx=np.amax(np.absolute(array))
    cdef int length
    cdef Py_ssize_t i,j
    cdef double h_param=<double>row/<double>numb
    cdef double w_param=<double>col/<double>numb
    lis=[]
    cdef int m=255
    for i in range(numb):
        lis.append((np.absolute(array[i].real)/maxx*numb).astype(np.uint32))
    cdef my_type[:,::1] a_view=a
    for i in prange(numb,nogil=True):
        with gil:
            length=lis[i]
        for j in range(length):
            a_view[j,i]=m
    a=cv2.flip(a,0)
    a=np.invert(a,dtype=np.uint8)
    a=resize(a,h_param,w_param)
    return a

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def histogram(my_type[:,::1] array,int lrange,int urange,bins,rowcol=(480,640)):
    """get histogram of array as a 2-D array(greyscale image)"""
    cdef int heigth=urange-lrange+1
    cdef int width=urange-lrange+1
    cdef int row=rowcol[0]
    cdef int col=rowcol[1]
    hist,bins=np.histogram(array,bins=bins,range=(lrange,urange))
    cdef int a=bins.shape[0]
    cdef int maxx=np.amax(hist)
    cdef Py_ssize_t i,j
    cdef int length
    cdef double h_param
    cdef double w_param
    h_param=<double>row/<double>heigth
    w_param=<double>col/<double>width
    lis=[]
    cdef int m=255
    for i in range(a-1):
        lis.append((hist[i]/maxx*(a-1)).astype(np.uint8))
    lis.append(0)
    if my_type is int:
        dtype = np.int
    elif my_type is double:
        dtype = np.double
    elif my_type is cython.longlong:
        dtype = np.longlong
    elif my_type is uint8_t:
        dtype=np.uint8
    h = np.zeros((heigth, width), dtype=dtype)
    cdef my_type[:,::1] h_view = h
    for i in prange(a,nogil=True):
        with gil:
            length=lis[i]
        for j in range(length):
            h_view[j,i]=m
    h=cv2.flip(h,0)
    h=np.invert(h,dtype=np.uint8)
    h=resize(h,h_param,w_param)
    return h

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def circle(int [:,::1] array,int radius,int i_m=-1,int j_m=-1):
    """sets all values witch belong to the disk to zero"""
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    if i_m==-1:
        i_m=<int>(row/2)
    if j_m==-1:
        j_m=<int>(column/2)
    cdef int[:,::1] arr=array.copy()
    cdef Py_ssize_t i,j;
    for i in prange(row,nogil=True):
        for j in range(column):
            if (<double>(i-i_m)**2+<double>(j-j_m)**2)**(0.5)<=radius:
                arr[i,j]=0
    return np.asarray(arr)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def circle_outer(int [:,::1] array,int radius,int i_m=-1,int j_m=-1):
    """sets all values witch do not belong to the disk to zero"""
    cdef int row=array.shape[0]
    cdef int column=array.shape[1]
    if i_m==-1:
        i_m=<int>(row/2)
    if j_m==-1:
        j_m=<int>(column/2)
    cdef int[:,::1] arr=array.copy()
    cdef Py_ssize_t i,j;
    for i in prange(row,nogil=True):
        for j in range(column):
            if (<double>(i-i_m)**2+<double>(j-j_m)**2)**(0.5)>=radius:
                arr[i,j]=0
    return np.asarray(arr)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def mean_hori(np.ndarray img,int number):
    """gets the mean of the horizontal by roating the array"""
    hori=[]
    cdef int rows=img.shape[0]
    cdef int cols=img.shape[1]
    cdef ndarray M
    for i in range(number):
        M=cv2.getRotationMatrix2D((cols/2,rows/2),i,1)
        img =cv2.warpAffine(img,M,(cols,rows))
        hori.append(img[240])
    hori_a=np.asarray(hori)
    hori_m=np.mean((hori_a),axis=0)
    hori_m=np.divide(hori_m,np.amax(hori_m))
    hori_m=(hori_m*255).astype(np.uint8)
    return hori_m

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def rotate_1d(ndarray hori_m,int number):
    """calculate the array by rotating a 1-D array"""
    cdef int x=hori_m.shape[0]
    cdef int divisor=1
    cdef ndarray img=np.zeros((x,x),dtype=np.uint8)
    while True:
        if number/divisor<=360:
            break
        else:
            divisor*=10
    cdef double div=<double>(divisor)
    for i in range(number):
        img[240]=(hori_m)
        M=cv2.getRotationMatrix2D((x/2,x/2),i/div,1)
        img = cv2.warpAffine(img,M,(x,x))
    return img

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

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef ndarray fft_shift_py(double [:,::1] arr):
    """Swicthes the 1st and 3rd; and the 2nd the 4th quadrant"""
    cdef int width=arr.shape[1]
    cdef int height=arr.shape[0]
    cdef double[:,::1] array=arr.copy()
    fft_shift(<double*>&array[0][0],width,height)
    numpy_array = np.asarray(array)
    return numpy_array