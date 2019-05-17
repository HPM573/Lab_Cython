import numpy as np
import cython
from SimulationCython import number as me


class Simulation:
	def __init__(self):
		self.rng = np.random.RandomState(seed=0)
		self.sum = 0
	def simulate(self, n_steps):
		for i in range(n_steps):
			self.sum += self.rng.random_sample()
		extra_number = me.Number()
		self.sum += extra_number.get_number()
