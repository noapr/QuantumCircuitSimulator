import logging
import sys
from src.quantum_circuit import QuantumCircuit
from src.qubit import Qubit

# Configure the logging module to print to the console
RED = '\x1b[31m'
RESET = '\x1b[0m'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=RED+'%(asctime)s [%(levelname)s]: %(message)s'+RESET)


def main():
    # Create a quantum circuit with 2 qubits
    print(f"Creating a quantum circuit with 2 qubits...")
    qc = QuantumCircuit(2)

    # Add gates to the circuit
    qc.add_gate('pauli_x', 0)  # Apply Pauli-X gate to the first qubit
    qc.add_gate('hadamard', 1)  # Apply Hadamard gate to the second qubit
    qc.add_gate('cnot', 0, 1)  # Apply CNOT gate with qubit 0 as control and qubit 1 as target

    # Initialize two qubits
    qubit1 = Qubit()
    qubit2 = Qubit()

    # Show the circuit
    qc.show()
    print(f"Initial state of Qubit 1: {qubit1}")
    print(f"Initial state of Qubit 2: {qubit2}")

    # Apply the circuit to the qubits
    print(f"\nApplying the circuit to the qubits...")
    qc.apply_circuit(qubit1, qubit2)

    # Measure the qubits
    qubit1.measure()
    qubit2.measure()

    # Print the results
    print(f"\nMeasuring the qubits...")
    print(f"Measurement of Qubit 1: {qubit1}")
    print(f"Measurement of Qubit 2: {qubit2}")


if __name__ == "__main__":
    main()
