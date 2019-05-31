import PyExternalPy.SimClasses as PP
import PyExternalCy.SimClasses as PC
import CyExternalCy.SimClasses as CC
import time

# python simulation
ppStart = time.time()
ppModel = PP.MultiSim()
ppModel.simulate(n_steps=1000, n_iterations=100)
ppModel.export_results()
ppEnd = time.time()

print("Python simulation time with external support in Python: ", ppEnd - ppStart)

# cython simulation
pcStart = time.time()
pcModel = PC.MultiSim()
pcModel.simulate(n_steps=1000, n_iterations=100)
pcModel.export_results()
pcEnd = time.time()

print("Python simulation time with external support in Cython: ", pcEnd - pcStart)

# cython simulation
ccStart = time.time()
ccModel = CC.MultiSim()
ccModel.simulate(n_steps=1000, n_iterations=100)
ccModel.export_results()
ccEnd = time.time()

print("Cython simulation time with external support in Cython: ", ccEnd - ccStart)