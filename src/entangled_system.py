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
        return f"{linear_dependence[0]} * {TWO_QUBIT_SHARED_SPACE_BASE_STRING[0]} + " \
               f"{linear_dependence[1]} * {TWO_QUBIT_SHARED_SPACE_BASE_STRING[1]} + " \
               f"{linear_dependence[2]} * {TWO_QUBIT_SHARED_SPACE_BASE_STRING[2]} + " \
               f"{linear_dependence[3]} * {TWO_QUBIT_SHARED_SPACE_BASE_STRING[3]}"
