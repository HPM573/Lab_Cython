import PyExternalCy.SimClasses as PC
import time

# cython simulation
pcStart = time.time()
pcModel = PC.MultiSim()
pcModel.simulate(n_steps=1000, n_iterations=100)
pcModel.export_results()
pcEnd = time.time()

print("Python simulation time with external support in Cython: ", pcEnd - pcStart)
