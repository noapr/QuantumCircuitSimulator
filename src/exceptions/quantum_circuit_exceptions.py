class QuantumCircuitError(Exception):
    """Base class for exceptions in the QuantumCircuitSimulator."""
    pass


class GateNotFoundError(QuantumCircuitError):
    """Exception raised when a specified gate is not found."""

    def __init__(self, gate_name):
        self.gate_name = gate_name
        super().__init__(f"Gate '{gate_name}' not found in supported gates.")


class InvalidGatePositionError(QuantumCircuitError):
    """Exception raised for invalid positions of gates in the quantum circuit."""

    def __init__(self, target, control):
        self.target = target
        self.control = control
        super().__init__(f"Invalid gate position: target={target}, control={control}")


class InvalidControlError(QuantumCircuitError):
    """Exception raised when a control qubit is provided for a 1-qubit gate."""

    def __init__(self, gate_name):
        super().__init__(f"Gate '{gate_name}' does not support a control qubit.")


# src/quantum_circuit_exceptions.py
class MissingControlError(QuantumCircuitError):
    """Exception raised when a control qubit is missing for a two-qubit gate."""

    def __init__(self, gate_name):
        super().__init__(f"A control qubit is required for the two-qubit gate '{gate_name}'.")


class QubitMismatchError(QuantumCircuitError):
    """Exception raised for mismatch between the number of input qubits and the circuit size."""

    def __init__(self, expected_qubits, actual_qubits):
        self.expected_qubits = expected_qubits
        self.actual_qubits = actual_qubits
        message = f"Mismatch in the number of input qubits. Expected {expected_qubits}, but got {actual_qubits}."
        super().__init__(message)
