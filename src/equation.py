from typing import List, Tuple
from random import choice

from src.constants import Operator
from src.hex_var import HexVar

class Equation:
    def __init__(self, operations: List[Operator] = [*Operator]):
        self.possible_operations = operations
        self._generate_operands()
        self._choose_operation()
        self._get_answer()

    def _generate_operands(self):
        self.operands = (HexVar(), HexVar())

    def _choose_operation(self):
        self.operator = choice(self.possible_operations)

    def _get_answer(self):
        self.answer = eval(f"{self.operands[0].int_val}{self.operator.value}{self.operands[1].int_val}")

    def to_str(self):
        return f"{self.operands[0].to_str()} {self.operator.value} {self.operands[1].to_str()}"
    
    def check_answer(self, answer):
        return answer == self.answer
