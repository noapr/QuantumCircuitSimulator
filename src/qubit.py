import numpy as np


class Qubit:
    def __init__(self):
        self.state = [1, 0]  # state |0⟩

    def apply_gate(self, gate):
        self.state = gate @ self.state

    def measure(self):
        outcome = np.random.choice([0, 1], p=[abs(self.state[0]) ** 2, abs(self.state[1]) ** 2])
        if outcome == 0:
            self.state = [1, 0]
        else:
            self.state = [0, 1]
        return outcome
