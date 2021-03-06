import os
import numpy
from setuptools import setup
from setuptools import find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext


def setup_():
    with open("README.md", "r") as fh:
        long_description = fh.read()

    ext_modules = [
        Extension('coherence_length_analyser.lib.c_funktionen', [
                  os.path.join('coherence_length_analyser', 'lib', 'c_funktionen.pyx')],),
    ]

    REQUIREMENTS = [
        'opencv-python',
        'numpy',
        "pillow",
        "PySide2",
        "scipy",
        "pyserial",
        "matplotlib",
        "qimage2ndarray",
        "pymediainfo",
        "natsort",
        "screeninfo",
        "qtconsole",
        "pyueye"
    ]

    setup(
        install_requires=REQUIREMENTS,
        name="coherence_length_analyser",
        version="1.0.0",
        author="Thilo Haarmeyer",
        author_email="haarmeyer@out-ev.de",
        description="Module for master thesis",
        long_description=long_description,
        long_description_content_type="text/markdown",
#        url="https://ich.com/ich/ich",
        packages=find_packages(),
        ext_modules=ext_modules,
        include_dirs=[numpy.get_include()],
        cmdclass={'build_ext': build_ext},
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
        ],
    )


if __name__ == '__main__':
    setup_()
