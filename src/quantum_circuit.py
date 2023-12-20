from collections import namedtuple
from src.quantum_gates.quantum_gate import get_quantum_gate_list
from src.exceptions.quantum_circuit_exceptions import GateNotFoundError, InvalidGatePositionError, InvalidControlError, MissingControlError, QubitMismatchError

GateTargetControl = namedtuple('GateTargetControl', ['gate', 'target', 'control'])


class QuantumCircuit:
    def __init__(self, input_size):
        self.input_size = input_size
        self.__supported_gates_list = get_quantum_gate_list()
        self.__gates = []

    def __len__(self):
        return len(self.__gates)

    def add_gate(self, name, target, control=None):
        gate_obj = self.__get_gate_object(name)
        if gate_obj.is_two_qubit_gate() and control is None:
            raise MissingControlError(name)
        elif not gate_obj.is_two_qubit_gate() and control is not None:
            raise InvalidControlError(name)
        elif gate_obj.is_two_qubit_gate() and (target >= self.input_size or control >= self.input_size or target < 0 or control < 0):
            raise InvalidGatePositionError(target, control)
        self.__gates.append(GateTargetControl(gate_obj, target, control))

    def __get_gate_object(self, name):
        for gate in self.__supported_gates_list:
            if gate.name == name:
                return gate
        raise GateNotFoundError(name)

    def show(self):
        CONNECTION = '|'
        EMPTY = "-"
        circuit = [str(i) + ' ' + EMPTY for i in range(self.input_size)]
        gap_lines = ['  ' + EMPTY for i in range(self.input_size - 1)]

        for gate_tuple in self.__gates:

            for i in range(len(circuit)):
                if circuit[i][0] == str(gate_tuple.target):
                    circuit[i] += EMPTY + gate_tuple.gate.icon.target + EMPTY
                elif gate_tuple.control is not None:
                    if circuit[i][0] == str(gate_tuple.control):
                        circuit[i] += EMPTY + gate_tuple.gate.icon.control + EMPTY
                    elif max(gate_tuple.target, gate_tuple.control) > int(circuit[i][0]) > min(gate_tuple.target, gate_tuple.control):
                        circuit[i] += 2 * EMPTY + CONNECTION + 2 * EMPTY
                    else:
                        circuit[i] += 5 * EMPTY
                elif gate_tuple.control is None:
                    circuit[i] += 5 * EMPTY

            for i in range(len(gap_lines)):
                if gate_tuple.control is not None:
                    if max(gate_tuple.target, gate_tuple.control) > i >= min(gate_tuple.target, gate_tuple.control):
                        gap_lines[i] += 2 * EMPTY + CONNECTION + 2 * EMPTY
                    else:
                        gap_lines[i] += 5 * EMPTY
                else:
                    gap_lines[i] += 5 * EMPTY

        circuit.reverse()
        gap_lines.reverse()
        for i in range(len(circuit) - 1):
            print(circuit[i])
            print(gap_lines[i])
        print(circuit[-1])

    def apply_circuit(self, *qubits):
        if self.input_size != len(qubits):
            raise QubitMismatchError(expected_qubits=self.input_size, actual_qubits=len(qubits))
        for gate_tuple in self.__gates:
            qubits[gate_tuple['target']].aapply_gate(gate_tuple['gate'], gate_tuple['control'])
