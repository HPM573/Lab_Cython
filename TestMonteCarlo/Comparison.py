import time
from scalar_python import mpy as regpy
from scalar_cython import mcy as regcy
from better_cython import bcy as betcy

start = time.time()
myClass = regpy.dice6_py(N=100, ndice=10, nsix=10)
#print(myClass)
end = time.time()
print("time in Scalar Python")
print(end - start)

start = time.time()
myClass = regcy.dice6_py(N=100, ndice=10, nsix=10)
#print(myClass)
end = time.time()
print("time in Scalar Cython")
print(end - start)

start = time.time()
myClass = betcy.dice6_cy1(N=100, ndice=10, nsix=10)
#print(myClass)
end = time.time()
print("time in Better Cython")
print(end - start)
