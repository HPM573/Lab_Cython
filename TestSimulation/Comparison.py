import time
import TestSimulation.SimulationPython.PythonSimulationClass as PythonSim
import TestSimulation.SimulationCython.CythonSimulationClass as CythonSim

N_STEPS = 100000

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
print(mySim.sum)
end = time.time()
print('Time of cython implementation: ', end-start)