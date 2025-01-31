from typing import List
from random import choice

from src.constants import Operator
from src.hex_var import HexVar

class Equation:
    def __init__(self):
        self.possible_operators = [*Operator]

    @classmethod
    def generate(cls, operators: List[Operator] = [*Operator]):
        equation = cls()
        equation.possible_operators = operators
        equation._generate_operands()
        equation._choose_operator()
        equation._get_answer()
        return equation

    @classmethod
    def build_from_terms(cls, operand_1: str, operand_2: str, operator: str):
        equation = cls()
        equation.operands = (HexVar.from_hex_str(operand_1), HexVar.from_hex_str(operand_2))
        equation.operator = Operator[operator]
        equation._get_answer()
        return equation

    def _set_possible_operators(self, operators: List[Operator]):
        self.possible_operators = operators

    def _generate_operands(self):
        self.operands = (HexVar(), HexVar())

    def _choose_operator(self):
        self.operator = choice(self.possible_operators)

    def _get_answer(self):
        self.answer = eval(f"{self.operands[0].int_val}{self.operator.value}{self.operands[1].int_val}")

    def to_str(self):
        return f"{self.operands[0].to_str()} {self.operator.value} {self.operands[1].to_str()}"
    
    def check_answer(self, answer):
        return answer == self.answer
