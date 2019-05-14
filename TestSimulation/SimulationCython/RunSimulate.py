import time 
start = time.time()
import SimulationClass as Sim

mySim = Sim.Simulation()
mySim.simulate(n_steps=100)

print(mySim.sum)

end = time.time()
print("time: ")
print(end-start)
