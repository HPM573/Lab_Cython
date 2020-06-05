import Cy.SimClasses as C
import time

# cython simulation
cStart = time.time()
cModel = C.MultiSim()
cModel.simulate(n_steps=10000, n_iterations=100)
cModel.export_results()
cEnd = time.time()

print("Cython simulation time: ", cEnd - cStart)
