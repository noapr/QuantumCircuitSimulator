import logging
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from src.exceptions.quantum_circuit_exceptions import ExceedsQubitLimitError
from src.qubit import Qubit
from src.utilities.quantum_constants import ZERO_STATE_KET_STRING, ZERO_STATE_KET, ONE_STATE_KET, ONE_STATE_KET_STRING, TWO_QUBIT_SHARED_SPACE
from src.utilities.quantum_math import get_base_shared_space_from_two_qubit_states

logging.getLogger('matplotlib').setLevel(logging.WARNING)


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

        element_counts = self.__processed_results(results)
        total_elements = len(results)
        density = {element: count / total_elements for element, count in element_counts.items()}
        labels, values = zip(*density.items())
        plt.bar(labels, values)

        plt.xlabel("Measurement Outcome")
        plt.ylabel("Probability Density")
        plt.title(f"Measurement Results\nNumber of runs: {len(results)}")
        plt.ylim(0, 1)
        plt.grid(axis="y", alpha=0.75)
        plt.show()

    def __processed_results(self, results):
        processed_results = []
        options = []

        if self.circuit.input_size == 2:
            options = [base_shared_space.str for base_shared_space in TWO_QUBIT_SHARED_SPACE]
            for measurements in results:
                base_shared_space = get_base_shared_space_from_two_qubit_states(measurements[0], measurements[1])
                processed_results.append(base_shared_space.str)
        if self.circuit.input_size == 1:
            options = [ZERO_STATE_KET_STRING, ONE_STATE_KET_STRING]
            for measurements in results:
                if all(measurements[0] == ZERO_STATE_KET):
                    processed_results.append(ZERO_STATE_KET_STRING)
                elif all(measurements[0] == ONE_STATE_KET):
                    processed_results.append(ONE_STATE_KET_STRING)

        element_counts = Counter(processed_results)
        for x in options:
            if x not in element_counts.keys():
                element_counts[x] = 0

        return element_counts
