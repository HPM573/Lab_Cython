import time 
start = time.time()
import TestSimulation.SimulationCython.CythonSimulationClass as Sim

mySim = Sim.Simulation()
mySim.simulate(n_steps=100)

print(mySim.sum)

end = time.time()
print("time: ")
print(end-start)
