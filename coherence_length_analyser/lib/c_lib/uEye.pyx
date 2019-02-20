# tag: openmp
# cython: infer_types=True
# cython: language_level=3
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp

import ctypes
import os
from .resource_path import *

from .defines import *
from .enum_c_value import *
from libc.stdint cimport uint32_t,int32_t
from libc.stdio cimport printf
from numpy cimport ndarray
cimport cython
from . cimport uEye


uEyeDll=ctypes.cdll.LoadLibrary(dll_path_uEye())
pcImgMem=b''
pid=0
pcImgMem_c = ctypes.c_char_p() #create placeholder for image memory
pid_c=ctypes.c_int(pid)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef double is_SetFrameRate(HIDS cam, double FPS, char* path):
    cdef double newFPS = 0
    newFPS = is_SetFrameRate_Dll(cam, FPS, path)
    return newFPS

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef FrameRate is_GetFrameTimeRange(HIDS cam, double min, double max, double intervall, char* path):
    cdef FrameRate frame_rate
    frame_rate.min = min
    frame_rate.max = max
    frame_rate.intervall = intervall
    frame_rate = is_GetFrameTimeRange_Dll(cam,min,max,intervall,path)
    return frame_rate
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_getNumberofCameras(char* path):
    cdef int numm=0
    numm=is_getNumberofCameras_Dll(path)
    return numm
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef HIDS is_InitCamera(char* path):
    cdef HIDS cam=-1
    cam=is_InitCamera_Dll(path)
    return cam
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_ExitCamera(HIDS cam,char* path):
    cdef int err_chk=999
    err_chk=is_ExitCamera_Dll(cam,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_SetGainBoost(HIDS cam,INT mode,char* path):
    cdef int err_chk=999
    err_chk=is_SetGainBoost_Dll(cam,mode,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_Blacklevel(HIDS cam,UINT command,UINT param,char* path):
    cdef int err_chk=999
    err_chk=is_Blacklevel_Dll(cam,command,param,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_SetHardwareGain(HIDS cam, INT master,INT red, INT green, INT blue,char* path):
    cdef int err_chk=999
    err_chk=is_SetHardwareGain_Dll(cam,master,red,green,blue,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef double is_Exposure(HIDS cam,UINT command,double param,char* path):
    cdef double exposre
    exposure=is_Exposure_Dll(cam,command,param,path)
    return exposure
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_SetAutoParameter(HIDS cam,INT param,double pval1,double pval2,char* path):
    cdef double pval1_c=pval1
    cdef double pval2_c=pval2
    cdef int err_chk=999
    err_chk=is_SetAutoParameter_Dll(cam,param,pval1_c,pval2_c,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_CaptureVideo(HIDS cam, INT wait,char* path):
    cdef int err_chk=999
    err_chk=is_CaptureVideo_Dll(cam,wait,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_EnableAutoExit(HIDS cam, INT mode,char* path):
    cdef int err_chk=999
    err_chk=is_EnableAutoExit_Dll(cam,mode,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_SetColorMode(HIDS cam, INT mode,char* path):
    cdef int err_chk=999
    err_chk=is_SetColorMode_Dll(cam,mode,path)
    return err_chk
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_SetExternalTrigger(HIDS cam,INT TriggerMode,char* path):
    cdef int ret=-1
    ret=is_SetExternalTrigger_Dll(cam,TriggerMode,path)
    return ret
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_AllocImageMem(HIDS cam,INT width,INT height,INT bitspixel):
    global pcImgMem
    global pid
    global pcImgMem_c
    global pid_c
    cdef int ret
    ret=uEyeDll.is_AllocImageMem(cam, width, height,  bitspixel, ctypes.byref(pcImgMem_c), ctypes.byref(pid_c))
    return ret
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_SetImageMem(HIDS cam):
    global pcImgMem
    global pid
    global pcImgMem_c
    global pid_c
    cdef int ret
    ret=uEyeDll.is_SetImageMem(cam, pcImgMem_c, pid_c)
    pid=pid_c.value
    pcImgMem=pcImgMem_c.value
    return ret
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int is_CopyImageMem(HIDS cam,ndarray ImageData):
    global pcImgMem
    global pid
    global pcImgMem_c
    global pid_c
    cdef int ret
    ret=uEyeDll.is_CopyImageMem (cam, pcImgMem_c, pid_c, ImageData.ctypes.data)
    return ret


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef unicode glubber(int a,int b):
    print(dll_path_uEye())
    return dll_path_uEye()
