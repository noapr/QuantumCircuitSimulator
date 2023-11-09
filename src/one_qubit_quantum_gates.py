import numpy as np


def identity_gate():
    return np.array([[1, 1], [1, -1]])


def pauli_x_gate():
    return np.array([[0, 1], [1, 0]])


def pauli_y_gate():
    return np.array([[0, -1j], [1j, 0]])


def pauli_z_gate():
    return np.array([[1, 0], [0, -1]])


def hadamard_gate():
    return (1 / np.sqrt(0.5)) * np.array([[1, 1], [1, -1]])


def not_gate():
    return pauli_x_gate()


def phase_gate(phi):
    return np.array([[1, 0], [0, np.exp(1j * phi)]])
