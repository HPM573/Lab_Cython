from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

setup(
    ext_modules=cythonize("SimulationClass.pyx"),
    cmdclass = {'build_ext': build_ext},
    include_dirs = [np.get_include()]
)
