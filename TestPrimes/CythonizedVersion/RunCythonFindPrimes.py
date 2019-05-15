import time
import TestPrimes.CythonizedVersion.CythonFindPrimes as cls

start = time.time()
myClass = cls.CythonFindPrimes(n=100)
print(myClass.get_prime_numbers())

end = time.time()
print("time")
print(end - start)
