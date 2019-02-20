import ctypes
from ...lib import functions


def Dll_Path():
    if ctypes.sizeof(ctypes.c_voidp) == 4:
        dll_path = functions.dll_path_uEye().encode("UTF-8")
    else:
        dll_path = functions.dll_path_uEye().encode("UTF-8")
    return dll_path
