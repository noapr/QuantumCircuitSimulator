from collections import namedtuple
from src.quantum_gates.one_qubit_quantum_gates import *
from src.quantum_gates.two_qubits_quantum_gates import *

TextIcon = namedtuple('TextIcon', ['target', 'control'])

UNICODE_CIRCLE_X = '\u29BB'
UNICODE_BULLET = '\u25CF'

# name, matrix and icon
QUANTUM_GATES = [
    ('identity', identity_matrix, TextIcon(target='|I|', control=None)),
    ('pauli_x', pauli_x_matrix, TextIcon(target='|X|', control=None)),
    ('pauli_y', pauli_y_matrix, TextIcon(target='|Y|', control=None)),
    ('pauli_z', pauli_z_matrix, TextIcon(target='|Z|', control=None)),
    ('hadamard', hadamard_matrix, TextIcon(target='|H|', control=None)),
    ('phase', phase_matrix, TextIcon(target='|S|', control=None)),
    ('not', not_matrix, TextIcon(target='|+|', control=None)),
    ('swap', swap_matrix, TextIcon(target='-X-', control='-X-')),
    ('cnot', cnot_matrix, TextIcon(target=f'-{UNICODE_CIRCLE_X}-', control=f'-{UNICODE_BULLET}-'))
]


class QuantumGate:
    def __init__(self, name, operation, icon):
        self.name = name
        self.operation = operation
        self.icon = icon


def get_quantum_gate_list():
    return [QuantumGate(gate[0], gate[1], gate[2]) for gate in QUANTUM_GATES]
