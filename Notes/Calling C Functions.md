# Calling C Functions 
Explain calling C library functions from Cython code 

[List of standard cimport files in Cython](https://github.com/cython/cython/tree/master/Cython/Includes)

.pxd -> standard way to provide resuable Cython declarations that cam be shared across modules

Example of calling function : 
```
from libc.math cimport sin

cdef double f(double x):
    return sin(x * x)
```
* notice the from (refer to the C library) and cimport (specific declaration from library)

## Dynamic Linking 
- link against shared libary 
- only names of external or shared libraries is placed into the memory
- lets many programs use single copy of executable memory 

Example: 
- libc math library -> not linked by default on some Unix-like systems
- cimporting the declarations + configure build system to link against shared library (for now, let's say "m")

```
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("demo",
              sources=["demo.pyx"],
              libraries=["m"]  # Unix-like specific
              )
]

setup(name="Demos",
      ext_modules=cythonize(ext_modules))
```

## External Declarations 
- access C code that Cython does not provide ready to use declaration 
- declare it yourself 
```
cdef extern from "math.h":
    double sin(double x)
```
- ```sin()``` is now available to Cython code and tell Cython to create C code that includes ```math.h``` header file 
- compiler sees original declaration in math.h at compile time, but Cython does not go through math.h and requires separate definition 
- declare and call into any C library as long as module is properly linked against shared or static library 
```cpdef``` -> export external C function from Cython model -> generate Python wrapper and adds it to module dict

```
cdef extern from "math.h":
    cpdef double sin(double x)
```

## Naming parameters
- provide own declarations for external C or C++ functions 
- avoid ambiguities and make code more readable
