import numpy as np
from src.exceptions.vector_exception import NotBraVectorError, NotKetVectorError, VectorError


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


def is_entangled(bra):
    if not is_bra_vector(bra):
        raise NotBraVectorError()
    return not bra[0][0] * bra[0][3] == bra[0][1] * bra[0][2]
