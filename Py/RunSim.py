import Py.SimClasses as P
import time

# python simulation
pStart = time.time()
pModel = P.MultiSim()
pModel.simulate(n_steps=1000, n_iterations=100)
pModel.export_results()
pEnd = time.time()

print("Python simulation time: ", pEnd - pStart)
