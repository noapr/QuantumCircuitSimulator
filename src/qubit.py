import numpy as np
from src.entangled_system import EntangledSystem
from src.exceptions.quantum_circuit_exceptions import MissingControlError
from src.utilities.quantum_constants import ZERO_STATE_KET, ONE_STATE_KET
from src.utilities.quantum_math import is_entangled, get_qubit_states_from_shared_space


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

    def measure(self):
        outcome = np.random.choice([0, 1], p=[abs(self.state[0]) ** 2, abs(self.state[1]) ** 2])
        if outcome == 0:
            self.state = ZERO_STATE_KET
        else:
            self.state = ONE_STATE_KET
        # TODO add _apply_measure_result_on_entangled_system(

    def _apply_measure_result_on_entangled_system(self):
        pass
