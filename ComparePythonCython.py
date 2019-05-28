import SimPython.SimClasses as P
import SimCython.SimClasses as C
import time

# python simulation
pStart = time.time()
pModel = P.MultiSim()
pModel.simulate(n_steps=1000, n_iterations=5000)
pEnd = time.time()

# cython simulation
cStart = time.time()
cModel = C.MultiSim()
cModel.simulate(n_steps=1000, n_iterations=5000)
cEnd = time.time()

print("Python model time: ", pEnd - pStart)
print("Cython model time: ", cEnd - cStart)
