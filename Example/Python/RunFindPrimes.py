import time
start = time.time()
import Prime.Python.FindPrimes as cls

myClass = cls.FindPrimes(n=100)
print(myClass.get_prime_numbers())

end = time.time()
print("time ")
print(end - start)