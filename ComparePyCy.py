import Py.SimClasses as P
import Cy.SimClasses as C
import time

# python simulation
pStart = time.time()
pModel = P.MultiSim()
pModel.simulate(n_steps=1000, n_iterations=100)
pEnd = time.time()

# cython simulation
cStart = time.time()
cModel = C.MultiSim()
cModel.simulate(n_steps=1000, n_iterations=100)
cEnd = time.time()

print("Python model time: ", pEnd - pStart)
print("Cython model time: ", cEnd - cStart)
