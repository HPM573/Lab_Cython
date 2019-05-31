from Py.Support import Ave
import csv
import os
import C.RVGs as RVGs


class OneSim:
    def __init__(self, seed):
        self.rng = RVGs.RNG(seed=seed)
        self.beta = RVGs.Beta(a=1, b=2)
        self.sum = 0

    def simulate(self, n_steps):
        for i in range(n_steps):
            self.sum += self.rng.random_sample() + self.beta.sample(rng=self.rng)


class MultiSim:
    def __init__(self):
        self.obs = []

    def simulate(self, n_steps, n_iterations):

        for i in range(n_iterations):
            sim = OneSim(seed=i)
            sim.simulate(n_steps=n_steps)
            self.obs.append(sim.sum)

        stat = Ave(data=self.obs)

        print(stat.get_ave())

    def export_results(self):

        # create a new file
        file_name = os.path.join('Results.csv')

        with open(file_name, "w", newline='') as file:
            csv_file = csv.writer(file, delimiter=',')

            for obs in self.obs:
                csv_file.writerow([obs])

            file.close()
