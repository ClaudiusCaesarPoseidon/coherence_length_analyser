# tag: openmp
# cython: infer_types=True
# cython: language_level=3
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp

import os
import sys
import ctypes
import inspect

cimport cython

def get_package_root():
    from . import __file__ as initpy_file_path
    return os.path.dirname(initpy_file_path)

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
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def dll_path_uEye():
    """get uEye_api.dll path"""
    cdef int byteness=ctypes.sizeof(ctypes.c_voidp)
    cdef unicode dll_path=u""
#    if (os.path.exists(os.path.normcase(R"C:\WINDOWS\system32\ueye_api.dll")) is True or os.path.exists(os.path.normcase(R"C:\WINDOWS\system32\ueye_api_64.dll")) is True) and False:
    if byteness==4:
        dll_path=u"ueye_api.dll"
    elif byteness==8:
        dll_path=u"ueye_api_64.dll"
#    else:
#        if byteness==4:
#            dll_path=resource_path(os.path.join(tmp, u"dlls",u"ueye_api.dll"))
#        elif byteness==8:
#            dll_path=resource_path(os.path.join(tmp, u"dlls",u"ueye_api_64.dll"))
    return dll_path
