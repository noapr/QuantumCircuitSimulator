from one_qubit_quantum_gates import *
from two_qubits_quantum_gates import *

UNICODE_CIRCLE_X = '\u29BB'
UNICODE_BULLET = '\u2022'

# name, matrix and icon
QUANTUM_GATES = [
    ('identity', identity_matrix, '|I|'),
    ('pauli_x', pauli_x_matrix, '|X|'),
    ('pauli_y', pauli_y_matrix, '|Y|'),
    ('pauli_z', pauli_z_matrix, '|Z|'),
    ('hadamard', hadamard_matrix, '|H|'),
    ('phase', phase_matrix, '|S|'),
    ('not', not_matrix, '|S|'),
    ('swap', swap_matrix, 'X\n|\nX'),
    ('cnot', swap_matrix, f'{UNICODE_BULLET}\n|\n{UNICODE_CIRCLE_X}')
]


class QuantumGate:
    def __init__(self, name, operation, icon):
        self.name = name
        self.operation = operation
        self.icon = icon


def get_quantum_gate_list():
    return [QuantumGate(gate[0], gate[1], gate[2]) for gate in QUANTUM_GATES]
