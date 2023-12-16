import unittest
import numpy as np
from src.qubit import Qubit, EntangledSystem
from src.utilities.quantum_constants import ZERO_STATE_KET, ONE_STATE_KET


class TestQubitMeasure(unittest.TestCase):
    def setUp(self):
        # Create instances needed for testing
        self.qubit = Qubit()
        self.control_qubit = Qubit()
        self.entangled_system = EntangledSystem(self.qubit, self.control_qubit, np.kron(ZERO_STATE_KET, ZERO_STATE_KET) + np.kron(ONE_STATE_KET, ONE_STATE_KET))

    def test_measure_zero_state(self):
        # Set up the qubit state to |0⟩
        self.qubit.state = ZERO_STATE_KET
        # Measure the qubit
        self.qubit.measure()
        # Assert that the qubit state is now |0⟩
        self.assertEqual(self.qubit.state.tolist(), ZERO_STATE_KET.tolist())

    def test_measure_one_state(self):
        # Set up the qubit state to |1⟩
        self.qubit.state = ONE_STATE_KET
        # Measure the qubit
        self.qubit.measure()
        # Assert that the qubit state is now |0⟩
        self.assertEqual(self.qubit.state.tolist(), ONE_STATE_KET.tolist())

    def test_measure_entangled_system(self):
        # Set up an entangled system state
        self.qubit.entangled_system = self.entangled_system
        self.control_qubit.entangled_system = self.entangled_system
        self.control_qubit.state = ZERO_STATE_KET + ONE_STATE_KET / np.sqrt(2)
        # Measure one of the qubits
        self.qubit.measure()
        # Assert that the entangled system state is updated accordingly
        self.assertEqual(self.control_qubit.state.tolist(), ZERO_STATE_KET.tolist())


if __name__ == '__main__':
    unittest.main()
