import TestSimulation.SimulationPython.PythonSimulationClass as Sim

mySim = Sim.Simulation()
mySim.simulate(n_steps=100)

print(mySim.sum)