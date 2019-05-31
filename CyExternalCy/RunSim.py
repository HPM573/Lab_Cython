import CyExternalCy.SimClasses as CC
import time

# cython simulation
ccStart = time.time()
ccModel = CC.MultiSim()
ccModel.simulate(n_steps=1000, n_iterations=100)
ccModel.export_results()
ccEnd = time.time()

print("Cython simulation time with external support in Cython: ", ccEnd - ccStart)
