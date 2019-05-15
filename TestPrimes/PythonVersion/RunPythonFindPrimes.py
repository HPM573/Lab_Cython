import time
import TestPrimes.PythonVersion.PythonFindPrimes as cls

start = time.time()
myClass = cls.PythonFindPrimes(n=1000)
print(myClass.get_prime_numbers())

end = time.time()
print("time ")
print(end - start)
