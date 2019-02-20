# tag: openmp
# cython: infer_types=True
# cython: language_level=3
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp

cimport cython
from libcpp cimport bool as bool_t

cdef extern from "c_written_functions.c" nogil:
    pass

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def switch(int value, bool_t windowed, bool_t border, bool_t fullscreen, bool_t interactive, bool_t ipython):
    cdef int switch_value = value
    cdef bool_t windowed_c = windowed
    cdef bool_t border_c = border
    cdef bool_t fullscreen_c = fullscreen
    cdef bool_t interactive_c = interactive
    cdef bool_t ipython_c = ipython
    if switch_value == 0:
        pass
    elif switch_value == 1:
        windowed_c = not windowed_c
    elif switch_value == 10:
        border_c = not border_c
    elif switch_value == 11:
        windowed_c = not windowed_c
        border_c = not border_c
    elif switch_value == 100:
        fullscreen_c = not fullscreen_c
    elif switch_value == 101:
        windowed_c = not windowed_c
        fullscreen_c = not fullscreen_c
    elif switch_value == 110:
        border_c = not border_c
        fullscreen_c = not fullscreen_c
    elif switch_value == 111:
        windowed_c = not windowed_c
        border_c = not border_c
        fullscreen_c = not fullscreen_c
    elif switch_value == 1000:
        interactive_c = not interactive_c
    elif switch_value == 1001:
        windowed_c = not windowed_c
        interactive_c = not interactive_c
    elif switch_value == 1010:
        border_c = not border_c
        interactive_c = not interactive_c
    elif switch_value == 1011:
        windowed_c = not windowed_c
        border_c = not border_c
        interactive_c = not interactive_c
    elif switch_value == 1100:
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
    elif switch_value == 1101:
        windowed_c = not windowed_c
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
    elif switch_value == 1110:
        border_c = not border
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
    elif switch_value == 1111:
        windowed_c = not windowed_c
        border_c = not border_c
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
    elif switch_value == 10000:
        ipython_c = not ipython_c
    elif switch_value == 10001:
        windowed_c = not windowed_c
        ipython_c = not ipython_c
    elif switch_value == 10010:
        border_c = not border_c
        ipython_c = not ipython_c
    elif switch_value == 10011:
        windowed_c = not windowed_c
        border_c = not border_c
        ipython_c = not ipython_c
    elif switch_value == 10100:
        fullscreen_c = not fullscreen_c
        ipython_c = not ipython_c
    elif switch_value == 10101:
        windowed_c = not windowed_c
        fullscreen_c = not fullscreen_c
        ipython_c = not ipython_c
    elif switch_value == 10110:
        border_c = not border_c
        fullscreen_c = not fullscreen_c
        ipython_c = not ipython_c
    elif switch_value == 10111:
        windowed_c = not windowed_c
        border_c = not border_c
        fullscreen_c = not fullscreen_c
        ipython_c = not ipython_c
    elif switch_value == 11000:
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11001:
        windowed_c = not windowed_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11010:
        border_c = not border_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11011:
        windowed_c = not windowed_c
        border_c = not border_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11100:
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11101:
        windowed_c = not windowed_c
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11110:
        border_c = not border
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    elif switch_value == 11111:
        windowed_c = not windowed_c
        border_c = not border_c
        fullscreen_c = not fullscreen_c
        interactive_c = not interactive_c
        ipython_c = not ipython_c
    else:
        pass
    return windowed_c, border_c, fullscreen_c, interactive_c, ipython_c