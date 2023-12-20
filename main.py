from src.quantum_circuit import QuantumCircuit
from src.qubit import Qubit


def main():
    # Create a quantum circuit with 2 qubits
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
    qc.apply_circuit(qubit1, qubit2)
    print(f"\nApplying the circuit to the qubits...\n")

    # Measure the qubits
    qubit1.measure()
    qubit2.measure()

    # Print the results
    print(f"Measurement of Qubit 1: {qubit1}")
    print(f"Measurement of Qubit 2: {qubit2}")


if __name__ == "__main__":
    main()
