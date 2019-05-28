import SimPython.SimClasses as P

# python simulation
pModel = P.MultiSim()
pModel.simulate(n_steps=1000, n_iterations=5000)
pModel.export_results()
