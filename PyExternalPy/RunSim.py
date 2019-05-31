import PyExternalPy.SimClasses as PP
import time

# python simulation
ppStart = time.time()
ppModel = PP.MultiSim()
ppModel.simulate(n_steps=1000, n_iterations=100)
ppModel.export_results()
ppEnd = time.time()

print("Python simulation time with external support in Python: ", ppEnd - ppStart)
