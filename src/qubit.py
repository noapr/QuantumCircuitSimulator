import numpy as np
from src.entangled_system import EntangledSystem
from src.exceptions.quantum_circuit_exceptions import MissingControlError
from src.utilities.quantum_constants import ZERO_STATE_KET, ONE_STATE_KET, TWO_QUBIT_SHARED_SPACE
from src.utilities.quantum_math import is_entangled, get_qubit_states_from_shared_space, get_linear_dependence_on_basis_vectors


class Qubit:
    def __init__(self):
        self.state = ZERO_STATE_KET
        self.entangled_system = None

    def apply_gate(self, gate, control_qubit=None):
        if gate.is_two_qubit_gate():
            if control_qubit is None:
                MissingControlError(gate.name)
            else:
                target_in_state = self.state
                control_in_state = control_qubit.state
                joint_state = np.kron(target_in_state, control_in_state)
                result = np.dot(gate.matrix, joint_state)

                left_qubit_state, right_qubit_state = get_qubit_states_from_shared_space(result)
                self.state = left_qubit_state
                control_qubit.state = right_qubit_state

                if is_entangled(result):
                    entangled_system = EntangledSystem(self, control_qubit, result)
                    self.entangled_system = entangled_system
                    control_qubit.entangled_system = entangled_system

        else:
            self.state = np.dot(gate.matrix, self.state)
            if self.entangled_system is not None:
                left_qubit = self.entangled_system.left_qubit
                right_qubit = self.entangled_system.right_qubit
                joint_state = np.kron(left_qubit.state, right_qubit.state)
                if is_entangled(joint_state):
                    self.entangled_system.state = joint_state
                else:
                    left_qubit.entangled_system = None
                    right_qubit.entangled_system = None

    def measure(self):
        outcome = np.random.choice([0, 1], p=[abs(self.state[0][0]) ** 2, abs(self.state[1][0]) ** 2])
        if outcome == 0:
            self._apply_measure_result_on_entangled_system(ZERO_STATE_KET)
            self.state = ZERO_STATE_KET
        else:
            self._apply_measure_result_on_entangled_system(ONE_STATE_KET)
            self.state = ONE_STATE_KET

    def _apply_measure_result_on_entangled_system(self, measure_result):

        if self.entangled_system is None:
            return

        shared_state = self.entangled_system.state
        affected_qubit_new_state = np.array([[0], [0]], dtype=np.float64)
        linear_dependence = get_linear_dependence_on_basis_vectors(shared_state)

        for i in range(len(TWO_QUBIT_SHARED_SPACE)):
            shared_space_vector_tuple = TWO_QUBIT_SHARED_SPACE[i]
            coefficient = linear_dependence[i]
            if coefficient == 0:
                continue
            elif (shared_space_vector_tuple.left_qubit == measure_result).all() and self.entangled_system.left_qubit == self:
                affected_qubit_new_state += shared_space_vector_tuple.right_qubit
            elif (shared_space_vector_tuple.right_qubit == measure_result).all() and self.entangled_system.right_qubit == self:
                affected_qubit_new_state += shared_space_vector_tuple.left_qubit

        if self.entangled_system.left_qubit == self:
            affected_qubit = self.entangled_system.right_qubit
        else:
            affected_qubit = self.entangled_system.left_qubit

        norm = np.linalg.norm(affected_qubit_new_state)
        affected_qubit.state = affected_qubit_new_state / norm
