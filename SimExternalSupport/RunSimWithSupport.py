import SimExternalSupport.SimWithSupportClasses as P

# python simulation
pModel = P.MultiSim()
pModel.simulate(n_steps=10, n_iterations=50)
pModel.export_results()
