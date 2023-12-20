import numpy as np
from src.exceptions.vector_exception import NotBraVectorError, NotKetVectorError, VectorError
from src.utilities.quantum_constants import TWO_QUBIT_SHARED_SPACE


def calculate_density_matrix(vector):
    if is_ket_vector(vector):
        return np.outer(vector, get_bra_vector(vector))
    if is_bra_vector(vector):
        return np.outer(get_ket_vector(vector), vector)
    raise VectorError('Invalid vector input: Not a ket or bra vector.')


def get_bra_vector(ket):
    if not is_ket_vector(ket):
        raise NotKetVectorError()
    return np.conj(ket).T


def get_ket_vector(bra):
    if not is_bra_vector(bra):
        raise NotBraVectorError()
    return np.conj(bra).T


def is_ket_vector(vector):
    return vector.ndim == 2 and vector.shape[1] == 1


def is_bra_vector(vector):
    return vector.ndim == 2 and vector.shape[0] == 1


def is_valid_vector(vector):
    if not isinstance(vector, np.ndarray):
        return False

    if is_ket_vector(vector) or is_bra_vector(vector):
        return True

    return False


def is_entangled(vector):
    if is_bra_vector(vector):
        return not vector[0][0] * vector[0][3] == vector[0][1] * vector[0][2]
    if is_ket_vector(vector):
        return not vector[0][0] * vector[3][0] == vector[1][0] * vector[2][0]
    raise VectorError('Invalid vector input: Not a ket or bra vector.')


def get_linear_dependence_on_basis_vectors(vector, normalize=True):
    if not is_valid_vector(vector) and vector.shape not in [(4, 1), (1, 4)]:
        raise VectorError('Invalid vector input: Not a ket shape (4, 1) or bra vector shape (1, 4).')

    linear_dependence = []
    for shared_space_vector_tuple in TWO_QUBIT_SHARED_SPACE:
        if is_ket_vector(vector):
            val = np.dot(np.conj(shared_space_vector_tuple.base_vector).T, vector)[0][0]
            linear_dependence.append(val)
        if is_bra_vector(vector):
            val = np.conj(np.dot(np.conj(shared_space_vector_tuple.base_vector).T, np.conj(vector).T))[0][0]
            linear_dependence.append(val)

    if normalize:
        norm = np.linalg.norm(linear_dependence)
        linear_dependence = linear_dependence / norm
    return linear_dependence


def get_qubit_states_from_shared_space(shared_state):
    linear_dependence = get_linear_dependence_on_basis_vectors(shared_state)
    left_qubit = np.array([[0], [0]], dtype=np.float64)
    right_qubit = np.array([[0], [0]], dtype=np.float64)
    i = 0
    for shared_space_vector_tuple in TWO_QUBIT_SHARED_SPACE:
        coefficient = linear_dependence[i]
        left_qubit += shared_space_vector_tuple.left_qubit * coefficient
        right_qubit += shared_space_vector_tuple.right_qubit * coefficient
        i += 1

    return left_qubit / np.linalg.norm(left_qubit), right_qubit / np.linalg.norm(right_qubit)
