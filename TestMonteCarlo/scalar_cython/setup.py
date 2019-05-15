from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    ext_modules=cythonize("mcy.pyx"),
    cmdclass={'build_ext': build_ext},
)
