from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as np

setup(
    ext_modules=cythonize(["SimClasses.pyx", "SimSupport.pyx"]),
    cmdclass={'build_ext': build_ext},
    include_dirs=[np.get_include()],
    compiler_directives={'embedsignature': True},
)

