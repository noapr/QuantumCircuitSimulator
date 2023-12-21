import numpy as np
import matplotlib.pyplot as plt
from src.exceptions.quantum_circuit_exceptions import ExceedsQubitLimitError
from src.qubit import Qubit
from src.utilities.quantum_constants import ZERO_STATE_KET_STRING, ZERO_STATE_KET, ONE_STATE_KET, ONE_STATE_KET_STRING
from src.utilities.quantum_math import get_base_shared_space_from_two_qubit_states


class QuantumCircuitRunner:
    def __init__(self, circuit):
        if circuit.input_size > 2:
            raise ExceedsQubitLimitError(circuit.input_size)

        self.circuit = circuit

    def run_circuit_multiple_times(self, num_times, show_plot=False):
        if num_times < 1:
            raise ValueError("num_times must be greater than or equal to 1")

        results = []
        for _ in range(num_times):
            qubits = [Qubit() for _ in range(self.circuit.input_size)]
            self.circuit.apply_circuit(*qubits)
            measurements = [q.measure() for q in qubits]
            results.append(measurements)

        if show_plot:
            self.__plot_results(results)

        return results

    def __plot_results(self, results):
        if not results:
            raise ValueError("No results to plot.")

        flat_results = self.__processed_results(results)
        plt.hist(flat_results, bins=np.arange(self.circuit.input_size + 1) - 0.5, align="mid", rwidth=0.8, density=True)
        plt.xlabel("Measurement Outcome")
        plt.ylabel("Probability Density")
        plt.title(f"Measurement Results\nNumber of runnings: {len(results)}")
        plt.xticks(range(self.circuit.input_size))
        plt.grid(axis="y", alpha=0.75)
        plt.show()

    def __processed_results(self, results):
        processed_results = []

        if self.circuit.input_size == 2:
            for measurements in results:
                base_shared_space = get_base_shared_space_from_two_qubit_states(measurements[0], measurements[1])
                processed_results.append(base_shared_space.str)
        if self.circuit.input_size == 1:
            for measurements in results:
                if all(measurements[0] == ZERO_STATE_KET):
                    processed_results.append(ZERO_STATE_KET_STRING)
                elif all(measurements[0] == ONE_STATE_KET):
                    processed_results.append(ONE_STATE_KET_STRING)

        return processed_results
