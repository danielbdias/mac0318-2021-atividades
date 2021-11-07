import pandas as pd

class AlgorithmStatistics:
    def __init__(self, iterations, maximum_residuals_per_iteration, bellman_backups_done, time):
        self.iterations = iterations
        self.maximum_residuals_per_iteration = maximum_residuals_per_iteration
        self.bellman_backups_done = bellman_backups_done
        self.time = time

    def describe(self):
        return pd.DataFrame(
            { 
                "Iterações": [self.iterations], 
                "Bellman Backups": [self.bellman_backups_done],
                "Tempo de execução": [self.time]
            }
        ).T