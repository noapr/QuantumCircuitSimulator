import numpy as np


def identity_matrix():
    return np.array([[1, 1], [1, -1]])


def pauli_x_matrix():
    return np.array([[0, 1], [1, 0]])


def pauli_y_matrix():
    return np.array([[0, -1j], [1j, 0]])


def pauli_z_matrix():
    return np.array([[1, 0], [0, -1]])


def hadamard_matrix():
    return (1 / np.sqrt(0.5)) * np.array([[1, 1], [1, -1]])


def not_matrix():
    return pauli_x_matrix()


def phase_matrix(phi):
    return np.array([[1, 0], [0, np.exp(1j * phi)]])
