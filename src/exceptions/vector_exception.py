class VectorError(Exception):
    """Base class for exceptions in the QuantumCircuitSimulator."""
    pass


class NotBraVectorError(VectorError):
    """Exception raised when a user try to use a not a bra vector as expected"""

    def __init__(self):
        super().__init__("Input is not a valid bra vector.")


class NotKetVectorError(VectorError):
    """Exception raised when a user try to use a not a ket vector as expected"""

    def __init__(self):
        super().__init__("Input is not a valid ket vector.")
