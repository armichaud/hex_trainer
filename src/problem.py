from typing import List, Tuple
from random import choice

from src.constants import Operation
from src.hex_var import HexVar

class Problem:
    def __init__(self, operations: List[Operation] = [*Operation]):
        self.operations = operations
        self._generate_problem()

    def _generate_problem(self) -> Tuple[HexVar, HexVar, Operation]:
        return (HexVar(), HexVar(), choice(self.operations))
