import unittest
import numpy as np
from src.quantum_gates.quantum_gate import get_quantum_gate_list
from src.qubit import Qubit
from src.utilities.quantum_constants import ZERO_STATE_KET, ONE_STATE_KET

EXPECTED_STATE_SINGLE_QUBIT_GATES_ON_ZERO_STATE = {'identity': ZERO_STATE_KET,
                                                   'pauli_x': ONE_STATE_KET,
                                                   'pauli_y': 1j * ONE_STATE_KET,
                                                   'pauli_z': ZERO_STATE_KET,
                                                   'hadamard': 1 / np.sqrt(2) * (ZERO_STATE_KET + ONE_STATE_KET),
                                                   'phase': ZERO_STATE_KET,
                                                   't_gate': ZERO_STATE_KET,
                                                   'not': ONE_STATE_KET}
EXPECTED_STATE_SINGLE_QUBIT_GATES_ON_ONE_STATE = {'identity': ONE_STATE_KET,
                                                  'pauli_x': ZERO_STATE_KET,
                                                  'pauli_y': -1j * ZERO_STATE_KET,
                                                  'pauli_z': -ONE_STATE_KET,
                                                  'hadamard': 1 / np.sqrt(2) * (ZERO_STATE_KET - ONE_STATE_KET),
                                                  'phase': np.exp(1j * np.pi / 2) * ONE_STATE_KET,
                                                  't_gate': np.exp(1j * np.pi / 4) * ONE_STATE_KET,
                                                  'not': ZERO_STATE_KET}

EXPECTED_STATES_TWO_QUBIT_GATES = {'cnot': {1: [ZERO_STATE_KET, ZERO_STATE_KET],
                                            2: [ZERO_STATE_KET, ONE_STATE_KET],
                                            3: [ONE_STATE_KET, ONE_STATE_KET],
                                            4: [ONE_STATE_KET, ZERO_STATE_KET]},
                                   'swap': {1: [ZERO_STATE_KET, ZERO_STATE_KET],
                                            2: [ONE_STATE_KET, ZERO_STATE_KET],
                                            3: [ZERO_STATE_KET, ONE_STATE_KET],
                                            4: [ONE_STATE_KET, ONE_STATE_KET]}
                                   }
INT_TO_JOINT_STATE = {1: [ZERO_STATE_KET, ZERO_STATE_KET],
                      2: [ZERO_STATE_KET, ONE_STATE_KET],
                      3: [ONE_STATE_KET, ZERO_STATE_KET],
                      4: [ONE_STATE_KET, ONE_STATE_KET]}


class TestQuantumGates(unittest.TestCase):
    def setUp(self):
        self.target_qubit = Qubit()
        self.control_qubit = Qubit()
        self.gates = get_quantum_gate_list()

    def test_apply_single_qubit_gates(self):
        for gate in self.gates:
            if not gate.is_two_qubit_gate():
                with self.subTest(f'zero state on gate {gate.name}'):
                    self.target_qubit.state = ZERO_STATE_KET
                    self.target_qubit.apply_gate(gate)
                    np.testing.assert_array_almost_equal(self.target_qubit.state, EXPECTED_STATE_SINGLE_QUBIT_GATES_ON_ZERO_STATE[gate.name])

                with self.subTest(f'one state on gate {gate.name}'):
                    self.target_qubit.state = ONE_STATE_KET
                    self.target_qubit.apply_gate(gate)
                    np.testing.assert_array_almost_equal(self.target_qubit.state, EXPECTED_STATE_SINGLE_QUBIT_GATES_ON_ONE_STATE[gate.name])

    def test_apply_two_qubit_gates(self):
        for gate in self.gates:
            if gate.is_two_qubit_gate():
                for initialize_states in EXPECTED_STATES_TWO_QUBIT_GATES[gate.name].keys():
                    with self.subTest(f'joint state number {initialize_states} on gate {gate.name}'):
                        self.target_qubit.state = INT_TO_JOINT_STATE[initialize_states][0]
                        self.control_qubit.state = INT_TO_JOINT_STATE[initialize_states][1]
                        self.target_qubit.apply_gate(gate, self.control_qubit)
                        np.testing.assert_array_almost_equal(self.target_qubit.state, EXPECTED_STATES_TWO_QUBIT_GATES[gate.name][initialize_states][0])
                        np.testing.assert_array_almost_equal(self.control_qubit.state, EXPECTED_STATES_TWO_QUBIT_GATES[gate.name][initialize_states][1])


if __name__ == '__main__':
    unittest.main()
