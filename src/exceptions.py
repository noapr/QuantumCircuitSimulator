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
