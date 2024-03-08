from collections import namedtuple
import numpy as np
from abc import ABC

TextIcon = namedtuple('TextIcon', ['target', 'control'])

UNICODE_CIRCLE_X = '\u29BB'
UNICODE_BULLET = '\u25CF'


def phase_matrix(phi):
    return np.array([[1, 0], [0, np.exp(1j * phi)]])


class QuantumGate(ABC):
    def __init__(self, name, matrix, icon):
        self.name = name
        self.matrix = matrix
        self.icon = icon

    def is_two_qubit_gate(self):
        return not (self.icon.control is None)


class IdentityGate(QuantumGate):
    def __init__(self):
        super().__init__(name='identity',
                         matrix=np.array([[1, 0], [0, 1]]),
                         icon=TextIcon(target='|I|', control=None))


class PauliXGate(QuantumGate):
    def __init__(self):
        super().__init__(name='pauli_x',
                         matrix=np.array([[0, 1], [1, 0]]),
                         icon=TextIcon(target='|X|', control=None))


class PauliYGate(QuantumGate):
    def __init__(self):
        super().__init__(name='pauli_y',
                         matrix=np.array([[0, -1j], [1j, 0]]),
                         icon=TextIcon(target='|Y|', control=None))


class PauliZGate(QuantumGate):
    def __init__(self):
        super().__init__(name='pauli_z',
                         matrix=np.array([[1, 0], [0, -1]]),
                         icon=TextIcon(target='|Z|', control=None))


class HadamardGate(QuantumGate):
    def __init__(self):
        super().__init__(name='hadamard',
                         matrix=(1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]]),
                         icon=TextIcon(target='|H|', control=None))


class PhaseGate(QuantumGate):
    def __init__(self):
        super().__init__(name='phase',
                         matrix=phase_matrix(np.pi / 2),
                         icon=TextIcon(target='|S|', control=None))


class TGate(QuantumGate):
    def __init__(self):
        super().__init__(name='t_gate',
                         matrix=phase_matrix(np.pi / 4),
                         icon=TextIcon(target='|T|', control=None))


class NotGate(QuantumGate):
    def __init__(self):
        super().__init__(name='not',
                         matrix=np.array([[0, 1], [1, 0]]),
                         icon=TextIcon(target='|+|', control=None))


class SwapGate(QuantumGate):
    def __init__(self):
        super().__init__(name='swap',
                         matrix=np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]),
                         icon=TextIcon(target='-X-', control='-X-'))


class CNotGate(QuantumGate):
    def __init__(self):
        super().__init__(name='cnot',
                         matrix=np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]),
                         icon=TextIcon(target=f'-{UNICODE_CIRCLE_X}-', control=f'-{UNICODE_BULLET}-'))


def get_quantum_gate_list():
    return [IdentityGate(),
            PauliXGate(),
            PauliYGate(),
            PauliZGate(),
            HadamardGate(),
            PhaseGate(),
            TGate(),
            NotGate(),
            SwapGate(),
            CNotGate()]
