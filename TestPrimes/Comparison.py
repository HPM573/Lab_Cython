import time
import TestPrimes.PythonVersion.PythonFindPrimes as pythonCls
import TestPrimes.CythonizedVersion.CythonFindPrimes as cythonCls

N_PRIMES = 10000

# testing the python implementation
start = time.time()
myClass = pythonCls.PythonFindPrimes(n=N_PRIMES)
print(myClass.get_prime_numbers())
end = time.time()

print("Time for python implementation: ", end - start)

# testing the cython implementation
start = time.time()
myClass = cythonCls.CythonFindPrimes(n=N_PRIMES)
print(myClass.get_prime_numbers())
end = time.time()

print("Time for cython implementation: ", end - start)
