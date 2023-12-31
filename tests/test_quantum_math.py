import unittest
import numpy as np
from src.exceptions.vector_exception import NotBraVectorError, NotKetVectorError, VectorError
from src.utilities.quantum_constants import ONE_STATE_KET, ZERO_STATE_KET, TWO_QUBIT_SHARED_SPACE
from src.utilities.quantum_math import calculate_density_matrix, get_bra_vector, get_ket_vector, is_ket_vector, is_bra_vector, is_entangled, get_linear_dependence_on_basis_vectors, \
    get_qubit_states_from_shared_space, get_base_shared_space_from_two_qubit_states


class TestVectorOperations(unittest.TestCase):

    def test_get_bra_vector(self):
        ket_vector = np.array([[1], [2]])
        bra_vector = get_bra_vector(ket_vector)
        expected_result = np.array([[1, 2]])
        np.testing.assert_array_equal(bra_vector, expected_result)

        non_ket_vector = np.array([1, 2, 5, 6])
        with self.assertRaises(NotKetVectorError):
            get_bra_vector(non_ket_vector)

    def test_get_ket_vector(self):
        bra_vector = np.array([[1, 2]])
        ket_vector = get_ket_vector(bra_vector)
        expected_result = np.array([[1], [2]])
        np.testing.assert_array_equal(ket_vector, expected_result)

        non_bra_vector = np.array([[1], [2]])
        with self.assertRaises(NotBraVectorError):
            get_ket_vector(non_bra_vector)

    def test_calculate_density_matrix(self):
        ket = np.array([[1], [3], [1j]])
        density_matrix = calculate_density_matrix(ket)
        expected_result = np.array([[1, 3, -1j], [3, 9, -3j], [1j, 3j, 1]])
        np.testing.assert_array_equal(density_matrix, expected_result)

        bra = np.array([[1, 3, 1j]])
        expected_result = np.array([[1, 3, 1j], [3, 9, 3j], [-1j, -3j, 1]])
        density_matrix = calculate_density_matrix(bra)
        np.testing.assert_array_equal(density_matrix, expected_result)

        non_vector = np.array([[1, 6], [3, 4], [1j, 6]])
        with self.assertRaises(VectorError):
            calculate_density_matrix(non_vector)

    def test_is_ket_vector(self):
        ket_vector = np.array([[1], [3], [1j]])
        self.assertTrue(is_ket_vector(ket_vector))

        non_ket_vector = np.array([1, 2])
        self.assertFalse(is_ket_vector(non_ket_vector))

    def test_is_bra_vector(self):
        bra_vector = np.array([[1, 2]])
        self.assertTrue(is_bra_vector(bra_vector))

        non_bra_vector = np.array([[1], [2]])
        self.assertFalse(is_bra_vector(non_bra_vector))

    def test_is_entangled(self):
        with self.subTest('call function with entangled bra.'):
            entangled_bra = np.array([[1, 0, 0, 1]])  # Bell state 1/sqrt(2) * (|00⟩ + |11⟩)
            self.assertTrue(is_entangled(entangled_bra))

        with self.subTest('call function with non entangled bra.'):
            non_entangled_bra = np.array([[1, 0, 0, 0]])
            self.assertFalse(is_entangled(non_entangled_bra))

        with self.subTest('call function with entangled ket.'):
            entangled_ket = np.array([[1], [0], [0], [1]])  # Bell state 1/sqrt(2) * (|00⟩ + |11⟩)
            self.assertTrue(is_entangled(entangled_ket))

        with self.subTest('call function with non entangled ket.'):
            non_entangled_ket = np.array([[1], [0], [0], [0]])
            self.assertFalse(is_entangled(non_entangled_ket))

        with self.subTest('call function with non bra or ket vector)'):
            invalid_vector = np.array([[1, 6], [0, 5]])
            with self.assertRaises(VectorError):
                is_entangled(invalid_vector)

    def test_get_linear_dependence_on_basis_vectors(self):
        with self.subTest('call function with bra and normalize = False.'):
            bra_vector = np.array([[1, 1, 0, 1]])
            linear_dependence = get_linear_dependence_on_basis_vectors(bra_vector, False)
            self.assertListEqual(linear_dependence, [1, 1, 0, 1])

        with self.subTest('call function with complex bra and normalize = False.'):
            bra_vector = np.array([[1, 1j, 0, 1]])
            linear_dependence = get_linear_dependence_on_basis_vectors(bra_vector, False)
            self.assertListEqual(linear_dependence, [1, 1j, 0, 1])

        with self.subTest('call function with ket and normalize = False.'):
            ket_vector = np.array([[1], [1], [0], [1]])
            linear_dependence = get_linear_dependence_on_basis_vectors(ket_vector, False)
            self.assertListEqual(linear_dependence, [1, 1, 0, 1])

        with self.subTest('call function with complex ket and normalize = False.'):
            ket_vector = np.array([[1], [1j], [0], [1]])
            linear_dependence = get_linear_dependence_on_basis_vectors(ket_vector, False)
            self.assertListEqual(linear_dependence, [1, 1j, 0, 1])

        with self.subTest('call function with bra and normalize = True.'):
            bra_vector = np.array([[1, 0, 0, 1]])
            linear_dependence = get_linear_dependence_on_basis_vectors(bra_vector)
            expected_result = ((1 / np.sqrt(2)) * np.array([1, 0, 0, 1])).tolist()
            np.testing.assert_array_equal(linear_dependence, expected_result)

    def test_get_qubit_states_from_shared_space(self):
        shared_state = np.array([[0, 1, -1, 0]])  # Bell state 1/sqrt(2) * (|01⟩ - |10⟩)
        left_qubit, right_qubit = get_qubit_states_from_shared_space(shared_state)
        expected_left_qubit = (1 / np.sqrt(2)) * (ZERO_STATE_KET - ONE_STATE_KET)
        expected_right_qubit = (1 / np.sqrt(2)) * (ONE_STATE_KET - ZERO_STATE_KET)
        np.testing.assert_array_almost_equal(left_qubit, expected_left_qubit)
        np.testing.assert_array_almost_equal(right_qubit, expected_right_qubit)

    def test_get_base_shared_space_from_two_qubit_states(self):
        with self.subTest('call function with base qubits'):
            qubit_one_state = ONE_STATE_KET
            qubit_two_state = ONE_STATE_KET
            expected_result = TWO_QUBIT_SHARED_SPACE[3]
            result = get_base_shared_space_from_two_qubit_states(qubit_one_state, qubit_two_state)
            self.assertEqual(result, expected_result)

        with self.subTest('call function with mixed qubits'):
            qubit_one_state = (1 / np.sqrt(2)) * (ZERO_STATE_KET - ONE_STATE_KET)
            qubit_two_state = ONE_STATE_KET
            expected_result = None
            result = get_base_shared_space_from_two_qubit_states(qubit_one_state, qubit_two_state)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
