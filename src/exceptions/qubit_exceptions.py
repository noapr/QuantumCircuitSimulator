class QubitError(Exception):
    """Base class for exceptions in the QuantumCircuitSimulator."""
    pass


class CantGetStateFromEntangledQubit(QubitError):
    """Exception raised when a user try to get the state of an entangled qubit."""

    def __init__(self):
        super().__init__("Cannot get the state of an entangled qubit.")
