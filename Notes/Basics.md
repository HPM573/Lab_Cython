# Basic Tutorial
Notes on the basics and purpose of Cython

## Basics
- Cython = Python with C Data Types
- Any piece of Python code is valid Cython code (almost)
- Cython compiler converts python to C code

## Cython Extension 
- save code in file named ___.pyx
- create setup.py -> it is like python Makefile [example](https://github.com/HPM573/Lab_Cython/blob/master/setup.py)
- commandline: $ python setup.py build_ext --inplace
** leave file with .pyd(unix) or .so(Windows)

Look at Fibonacci and Primes example 
