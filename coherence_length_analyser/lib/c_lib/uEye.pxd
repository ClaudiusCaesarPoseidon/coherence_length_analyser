import ctypes
from .defines import *
from .enum_c_value import *
from libc.stdint cimport uint32_t,int32_t
from numpy cimport ndarray
cimport cython


ctypedef uint32_t HIDS
ctypedef int32_t INT
ctypedef uint32_t UINT

cdef extern from "ueye_c.c" nogil:
    int is_getNumberofCameras_Dll(char*)                     #
    HIDS is_InitCamera_Dll(char*)                            #
    INT is_ExitCamera_Dll(HIDS,char*)                         #
    INT is_SetGainBoost_Dll(HIDS,INT,char*)                   #
    INT is_Blacklevel_Dll(HIDS,UINT,UINT,char*)               #
    INT is_SetHardwareGain_Dll(HIDS,INT,INT,INT,INT,char*)    #
    double is_Exposure_Dll(HIDS,UINT,double,char*)            #
    INT is_SetAutoParameter_Dll(HIDS,INT,double,double,char*) #
    INT is_CaptureVideo_Dll(HIDS,INT,char*)                   #
    INT is_EnableAutoExit_Dll(HIDS,INT,char*)                 #
    INT is_SetColorMode_Dll(HIDS,INT,char*)                   #
    INT is_SetExternalTrigger_Dll(HIDS,INT,char*)#ret         #
    cdef struct FrameRate:
        double min
        double max
        double intervall
    FrameRate is_GetFrameTimeRange_Dll(HIDS,double,double,double,char*)
    double is_SetFrameRate_Dll(HIDS, double,char*)


cpdef int is_getNumberofCameras(char*)
cpdef HIDS is_InitCamera(char*)
cpdef int is_ExitCamera(HIDS,char*)
cpdef int is_SetGainBoost(HIDS,INT,char*)
cpdef int is_Blacklevel(HIDS,UINT,UINT,char*)
cpdef int is_SetHardwareGain(HIDS, INT,INT, INT, INT,char*)
cpdef double is_Exposure(HIDS,UINT,double,char*)
cpdef int is_SetAutoParameter(HIDS,INT,double,double,char*)
cpdef int is_CaptureVideo(HIDS, INT,char*)
cpdef int is_EnableAutoExit(HIDS, INT,char*)
cpdef int is_SetColorMode(HIDS, INT,char*)
cpdef int is_SetExternalTrigger(HIDS,INT,char*)
cpdef int is_AllocImageMem(HIDS,INT,INT,INT)
cpdef int is_SetImageMem(HIDS)
cpdef int is_CopyImageMem(HIDS,ndarray)
cpdef FrameRate is_GetFrameTimeRange(HIDS,double,double,double,char*)
cpdef double is_SetFrameRate(HIDS, double, char*)