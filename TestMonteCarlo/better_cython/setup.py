from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    ext_modules=cythonize("bcy.pyx"),
    cmdclass={'build_ext': build_ext},
)
