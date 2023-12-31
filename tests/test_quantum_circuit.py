import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.quantum_circuit import QuantumCircuit
from src.exceptions.quantum_circuit_exceptions import InvalidGatePositionError, InvalidControlError, MissingControlError, GateNotFoundError, QubitMismatchError, \
    ExceedsQubitLimitError
from src.qubit import Qubit


class TestQuantumCircuit(unittest.TestCase):
    def setUp(self):
        self.qc = QuantumCircuit(input_size=3)

    def test_add_gate_valid(self):
        # Test adding a valid two-qubit gate
        self.qc.add_gate('cnot', target=1, control=0)
        self.assertEqual(len(self.qc), 1)

    def test_add_gate_invalid_position(self):
        # Test adding a gate with an invalid position
        with self.assertRaises(InvalidGatePositionError):
            self.qc.add_gate('cnot', target=3, control=0)

    def test_add_gate_invalid_control(self):
        # Test adding a gate with an invalid control for a 1-qubit gate
        with self.assertRaises(InvalidControlError):
            self.qc.add_gate('pauli_x', target=1, control=0)

    def test_add_gate_valid_single_qubit_gate(self):
        # Test adding a valid single-qubit gate
        self.qc.add_gate('pauli_x', target=2)
        self.assertEqual(len(self.qc), 1)

    def test_add_gate_invalid_single_qubit_gate_with_control(self):
        # Test adding a gate with control for a single-qubit gate
        with self.assertRaises(InvalidControlError):
            self.qc.add_gate('pauli_x', target=1, control=0)

    def test_add_gate_missing_control(self):
        # Test adding a two-qubit gate without providing a control qubit
        with self.assertRaises(MissingControlError):
            self.qc.add_gate('cnot', target=1)

    def test_add_invalid_gate_name(self):
        with self.assertRaises(GateNotFoundError):
            self.qc.add_gate('invalid_gate', target=0)

    def test_show_circuit(self):
        # Test displaying the circuit and check if the output matches the expected output
        expected_output = (
            "2 -------|X|-\n"
            "  -----------\n"
            "1 ---⦻-------\n"
            "  ---|-------\n"
            "0 ---●-------\n"
        )

        with StringIO() as buffer, redirect_stdout(buffer):
            self.qc.add_gate('cnot', target=1, control=0)
            self.qc.add_gate('pauli_x', target=2)
            self.qc.show()
            actual_output = buffer.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_apply_circuit_qubit_mismatch(self):
        # Test applying a circuit with a mismatch in the number of input qubits
        with self.assertRaises(QubitMismatchError) as context:
            self.qc.apply_circuit(0, 1, 2, 3)

    def test_exceeds_qubit_limit_error(self):
        qubit1 = Qubit()
        qubit2 = Qubit()
        qubit3 = Qubit()

        # Test for raising the ExceedsQubitLimitError
        with self.assertRaises(ExceedsQubitLimitError) as context:
            self.qc.apply_circuit(qubit1, qubit2, qubit3)


if __name__ == '__main__':
    unittest.main()
