from graphlib import TopologicalSorter
from enum import Enum, auto
from typing import NamedTuple, Union
from utils import get_input_path

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Operation(Enum):
    AND = auto()
    OR = auto()
    NOT = auto()
    RSHIFT = auto()
    LSHIFT = auto()
    NONE = auto()


class Instructions(NamedTuple):
    operation: Operation
    input1: Union[str, int]
    input2: Union[str, int]
    shift_distance: Union[int, None]


def main() -> None:
    file_path = get_input_path(__file__, '2015_7_input.txt')
    dependencies: dict[str, list[str]] = dict()
    instructions: dict[str, Instructions] = dict()
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
    for line in lines:
        parse_instructions(line, dependencies, instructions)
    print(instructions)
    print(dependencies)

    ts = TopologicalSorter(dependencies)
    wire_order = tuple(ts.static_order())
    print(wire_order)

    wire_signals = dict()
    for wire in wire_order:
        perform_operation(wire, instructions, wire_signals)
    print('Part one result:', wire_signals['a'])
    
    # Part two

    signal_a = wire_signals['a']
    wire_signals['b'] = signal_a
    for wire in wire_order:
        if wire != 'b':
            perform_operation(wire, instructions, wire_signals)
    print('Part two result:', wire_signals['a'])


def parse_instructions(line, dependencies, instructions):
    operation: Operation = Operation.NONE
    input1 = None
    input2 = None
    shift_distance: Union[int, None] = None

    step = line.split(' -> ')
    receiving_wire = step[1]
    original_instruction = step[0].split()
    match(len(original_instruction)):
        case 1:
            input1 = handle_instruction_input(receiving_wire, original_instruction[0], dependencies)
        case 2:
            operation = Operation.NOT
            input1 = handle_instruction_input(receiving_wire, original_instruction[1], dependencies)
        case 3:
            match(original_instruction[1]):
                case 'AND':
                    operation = Operation.AND
                    input1 = handle_instruction_input(receiving_wire, original_instruction[0], dependencies)
                    input2 = handle_instruction_input(receiving_wire, original_instruction[2], dependencies)
                case 'OR':
                    operation = Operation.OR
                    input1 = handle_instruction_input(receiving_wire, original_instruction[0], dependencies)
                    input2 = handle_instruction_input(receiving_wire, original_instruction[2], dependencies)
                case 'LSHIFT':
                    operation = Operation.LSHIFT
                    input1 = handle_instruction_input(receiving_wire, original_instruction[0], dependencies)
                    shift_distance = int(original_instruction[2])

                case 'RSHIFT':
                    operation = Operation.RSHIFT
                    input1 = handle_instruction_input(receiving_wire, original_instruction[0], dependencies)
                    shift_distance = int(original_instruction[2])
    instructions[receiving_wire] = Instructions(operation=operation,
                                                input1=input1, input2=input2, shift_distance=shift_distance)


def handle_instruction_input(wire: str, input_segment: str, dependencies: dict[str, list[str]]) -> Union[int, str]:
    if input_segment.isdigit():
        return int(input_segment)
    else:
        if wire in dependencies:
            dependencies[wire].append(input_segment)
        else:
            dependencies[wire] = [input_segment]
        return input_segment


def perform_operation(wire: str, instructions: dict[str, Instructions], wire_signals: dict[str, np.uint16]) -> None:
    current_instruction = instructions.get(wire)

    match current_instruction.operation:
        case Operation.NONE:
            signal_input = get_wire_signal(current_instruction.input1, wire_signals)
            wire_signals[wire] = signal_input
        case Operation.NOT:
            signal_input = get_wire_signal(current_instruction.input1, wire_signals)
            wire_signals[wire] = ~ signal_input
        case Operation.OR:
            signal_input1 = get_wire_signal(current_instruction.input1, wire_signals)
            signal_input2 = get_wire_signal(current_instruction.input2, wire_signals)
            wire_signals[wire] = signal_input1 | signal_input2
        case Operation.AND:
            signal_input1 = get_wire_signal(current_instruction.input1, wire_signals)
            signal_input2 = get_wire_signal(current_instruction.input2, wire_signals)
            wire_signals[wire] = signal_input1 & signal_input2
        case Operation.LSHIFT:
            signal_input = get_wire_signal(current_instruction.input1, wire_signals)
            wire_signals[wire] = signal_input << np.uint16(current_instruction.shift_distance)
        case Operation.RSHIFT:
            signal_input = get_wire_signal(current_instruction.input1, wire_signals)
            wire_signals[wire] = signal_input >> np.uint16(current_instruction.shift_distance)


def get_wire_signal(instruction_input: Union[str, int], wire_signals: dict[str, np.uint16]) -> np.uint16:
    if isinstance(instruction_input, int):
        return np.uint16(instruction_input)
    elif isinstance(instruction_input, str):
        return np.uint16(wire_signals[instruction_input])
    else:
        raise Exception('Incorrect input type!')


def plot_the_sorted_graph(dependencies, wire_order) -> None:
    graph = nx.DiGraph()
    for node, dependencies in dependencies.items():
        for dep in dependencies:
            graph.add_edge(dep, node)

    plt.figure(figsize=(50, 50))
    pos = nx.spring_layout(graph, k=7, iterations=1000)
    nx.draw(graph, pos, with_labels=False, node_color='skyblue', font_weight='bold', arrows=True, node_size=200)

    sorted_labels = {node: f"{idx+1}: {node}" for idx, node in enumerate(wire_order)}
    nx.draw_networkx_labels(graph, pos, labels=sorted_labels, font_size=4, font_color="black")

    plt.title("Topologically Sorted Graph")
    plt.show()


if __name__ == '__main__':
    main()
