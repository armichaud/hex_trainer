from src.constants import Operator
from src.hex_var import HexVar
from src.equation import Equation

class TestProblem:

    def test_generate_problem_valid_operations(self):
        problem = Equation()

        problem._generate_operands()
        a, b = problem.operands

        assert isinstance(a, HexVar)
        a_hex = a.str_val
        assert a_hex.startswith("0x")
        int(a_hex, 16)  # Try converting to int to ensure it's a valid hex

        assert isinstance(b, HexVar)
        b_hex = b.str_val
        assert b_hex.startswith("0x")
        int(b_hex, 16)  # Try converting to int to ensure it's a valid hex

        problem._choose_operator()
        assert problem.operator in [*Operator]

    def test_get_answer_addition(self):
        equation = Equation.build_from_terms("0x0A", "0x0B", "ADD")
        equation._get_answer() 
        assert equation.answer == 21

    def test_get_answer_subtraction(self):
        equation = Equation.build_from_terms("0x10", "0x05", "SUBTRACT")
        equation._get_answer()
        assert equation.answer == 11

    def test_get_answer_multiplication(self):
        equation = Equation.build_from_terms("0x02", "0x0C", "MULTIPLY")
        equation._get_answer() 
        assert equation.answer == 24

    def test_get_answer_division(self):
        equation = Equation.build_from_terms("0x0F", "0x03", "DIVIDE")
        equation._get_answer()
        assert equation.answer == 5

    def test_check_answer_correct(self):
        equation = Equation.build_from_terms("0x0A", "0x0B", "ADD")
        assert equation.check_answer(21)

    def test_check_answer_incorrect(self):
        equation = Equation.build_from_terms("0x0A", "0x0B", "ADD")
        assert not equation.check_answer(20)

    def test_check_answer_mod(self):
        equation = Equation.build_from_terms("0x19", "0x0A", "MOD")  # 25 mod 10
        assert equation.check_answer(5)
