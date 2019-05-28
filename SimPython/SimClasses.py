import numpy as np
from SimPython.SimSupport import Ave


class OneSim:
    def __init__(self):
        self.rng = np.random.RandomState(seed=0)
        self.sum = 0

    def simulate(self, n_steps):
        for i in range(n_steps):
            self.sum += self.rng.random_sample()


class MultiSim:
    def __init__(self):
        self.obs = []

    def simulate(self, n_steps, n_iterations):

        for i in range(n_iterations):
            sim = OneSim()
            sim.simulate(n_steps=n_steps)
            self.obs.append(sim.sum)

        stat = Ave(data=self.obs)

        print(stat.get_ave())
