# Primes Commands on Terminal and Testing

# Timing Testing 
## Setup Files 
```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("primes.pyx"),
)
```

```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("primes_python.pyx"),
)
```

```
time python setup.py build_ext --inplace
```

## Time PyInstaller 
```
time pyInstaller primes_python.py
```

```
time pyInstaller primes.pyx
```
