from typing import List, Tuple
from random import choice

from src.constants import Operation
from src.hex_var import HexVar

class Equation:
    def __init__(self, operations: List[Operation] = [*Operation]):
        self.possible_operations = operations
        self._generate_operands()
        self._choose_operation()

    def _generate_operands(self):
        self.operands = (HexVar(), HexVar())

    def _choose_operation(self):
        self.operation = choice(self.possible_operations)
