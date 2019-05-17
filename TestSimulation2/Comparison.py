#!python
#cython: language_level=3, boundscheck=False
import time
from SimulationPython import PythonSimulationClass as PythonSim
from SimulationCython import CythonSimulationClass as CythonSim

N_STEPS = 10000000

# testing the python implementation
start = time.time()
mySim = PythonSim.Simulation()
mySim.simulate(n_steps=N_STEPS)
print(mySim.sum)
end = time.time()
print('Time of python implementation: ', end-start)

# testing the cython implementation
start = time.time()
mySim = CythonSim.Simulation()
mySim.simulate(n_steps=N_STEPS)
print(mySim)
end = time.time()
print('Time of cython implementation: ', end-start)
