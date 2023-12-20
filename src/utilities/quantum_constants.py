from collections import namedtuple
import numpy as np

ZERO_STATE_KET = np.array([[1], [0]])  # state |0⟩
ONE_STATE_KET = np.array([[0], [1]])  # state |1⟩

ZERO_STATE_KET_STRING = '|0⟩'
ONE_STATE_KET_STRING = '|1⟩'

ZERO_STATE_BRA = np.array([[1, 0]])  # state ⟨0|
ONE_STATE_BRA = np.array([[0, 1]])  # state ⟨1|

SharedSpaceVectorTuple = namedtuple('SharedSpaceVectorTuple', ['base_vector', 'left_qubit', 'right_qubit'])

TWO_QUBIT_SHARED_SPACE = [SharedSpaceVectorTuple(base_vector=np.kron(ZERO_STATE_KET, ZERO_STATE_KET),  # state |00⟩
                                                 left_qubit=ZERO_STATE_KET,
                                                 right_qubit=ZERO_STATE_KET),
                          SharedSpaceVectorTuple(base_vector=np.kron(ZERO_STATE_KET, ONE_STATE_KET),  # state |01⟩
                                                 left_qubit=ZERO_STATE_KET,
                                                 right_qubit=ONE_STATE_KET),
                          SharedSpaceVectorTuple(base_vector=np.kron(ONE_STATE_KET, ZERO_STATE_KET),  # state |10⟩
                                                 left_qubit=ONE_STATE_KET,
                                                 right_qubit=ZERO_STATE_KET),
                          SharedSpaceVectorTuple(base_vector=np.kron(ONE_STATE_KET, ONE_STATE_KET),  # state |11⟩
                                                 left_qubit=ONE_STATE_KET,
                                                 right_qubit=ONE_STATE_KET)]

TWO_QUBIT_SHARED_SPACE_BASE_STRING = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
