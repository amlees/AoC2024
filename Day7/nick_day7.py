import numpy as np

from dataclasses import dataclass
from itertools import product
from typing import List


@dataclass
class CalibrationEquation:
    test_value: int
    numbers: List[int]

    def __post_init__(self):
        self.is_valid = False

    def test_equation(self, operations_dict: dict) -> int:
        operands_list = [operand for operand in product(operations_dict.keys(), repeat=len(self.numbers)-1)]
        for test_operand in operands_list:
            test_value = self.numbers[0]
            for ind, operand in enumerate(test_operand):
                test_value = operations_dict[operand](test_value, self.numbers[ind+1])
            if test_value == self.test_value:
                self.is_valid = True
                break

        return self.test_value if self.is_valid else 0

equation_list = []
with open("day7_input.txt", "r") as fptr:
    while line := fptr.readline().strip("\n"):
        test_value, numbers_str = line.split(": ")
        numbers = [int(x) for x in numbers_str.split(" ")]
        current_equation = CalibrationEquation(test_value=int(test_value), numbers=numbers)
        equation_list.append(current_equation)

operations_dict = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

total_calibration = sum([equation.test_equation(operations_dict) for equation in equation_list])
print(f"Part One Answer: {total_calibration}")

operations_dict = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "||": lambda x, y: int(str(x)+str(y))
}

total_calibration = sum([equation.test_equation(operations_dict) for equation in equation_list])
print(f"Part Two Answer: {total_calibration}")
