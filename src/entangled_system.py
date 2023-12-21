from sympy import nsimplify, sqrt

from src.utilities.quantum_constants import TWO_QUBIT_SHARED_SPACE_BASE_STRING
from src.utilities.quantum_math import get_linear_dependence_on_basis_vectors


class EntangledSystem:
    def __init__(self, left_qubit, right_qubit, state):
        self.left_qubit = left_qubit
        self.right_qubit = right_qubit
        self.state = state

    def __str__(self):
        linear_dependence = [nsimplify(num, [sqrt(2), sqrt(3), sqrt(5), sqrt(7), sqrt(11)]) for num in get_linear_dependence_on_basis_vectors(self.state)]
        entangled_system_string = ''
        for i in range(len(linear_dependence)):
            if linear_dependence[i] != 0:
                entangled_system_string += f"{linear_dependence[i]} * {TWO_QUBIT_SHARED_SPACE_BASE_STRING[i]} +"
        entangled_system_string = entangled_system_string[:-2]
        return entangled_system_string
