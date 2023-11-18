from collections import namedtuple
from src.quantum_gates.one_qubit_quantum_gates import *
from src.quantum_gates.two_qubits_quantum_gates import *
import numpy as np

TextIcon = namedtuple('TextIcon', ['target', 'control'])

UNICODE_CIRCLE_X = '\u29BB'
UNICODE_BULLET = '\u25CF'

QUANTUM_GATES = [  # name, matrix and icon
    ('identity', identity_matrix(), TextIcon(target='|I|', control=None)),
    ('pauli_x', pauli_x_matrix(), TextIcon(target='|X|', control=None)),
    ('pauli_y', pauli_y_matrix(), TextIcon(target='|Y|', control=None)),
    ('pauli_z', pauli_z_matrix(), TextIcon(target='|Z|', control=None)),
    ('hadamard', hadamard_matrix(), TextIcon(target='|H|', control=None)),
    ('phase', phase_matrix(np.pi / 2), TextIcon(target='|S|', control=None)),
    ('t_gate', phase_matrix(np.pi / 4), TextIcon(target='|T|', control=None)),
    ('not', not_matrix(), TextIcon(target='|+|', control=None)),
    ('swap', swap_matrix(), TextIcon(target='-X-', control='-X-')),
    ('cnot', cnot_matrix(), TextIcon(target=f'-{UNICODE_CIRCLE_X}-', control=f'-{UNICODE_BULLET}-'))
]


class QuantumGate:
    def __init__(self, name, matrix, icon):
        self.name = name
        self.matrix = matrix
        self.icon = icon

    def is_two_qubit_gate(self):
        return not (self.icon.control is None)


def get_quantum_gate_list():
    return [QuantumGate(gate[0], gate[1], gate[2]) for gate in QUANTUM_GATES]
