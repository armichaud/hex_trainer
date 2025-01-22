import pytest
from src.constants import Operator
from src.calculator import Calculator

class TestCalculator:

    def test_get_result_addition(self):
        calc = Calculator("A", "B", Operator.ADD)
        assert calc._get_result() == 21

    def test_get_result_subtraction(self):
        calc = Calculator("10", "5", Operator.SUBTRACT)
        assert calc._get_result() == 11

    def test_get_result_multiplication(self):
        calc = Calculator("2", "C", Operator.MULTIPLY)
        assert calc._get_result() == 24

    def test_get_result_division(self):
        calc = Calculator("F", "3", Operator.DIVIDE)
        assert calc._get_result() == 5

    def test_check_result_correct(self):
        calc = Calculator("A", "B", Operator.ADD)
        assert calc.check_result(21) is True

    def test_check_result_incorrect(self):
        calc = Calculator("A", "B", Operator.ADD)
        assert calc.check_result(20) is False

    def test_evaluate(self):
        calc = Calculator("A", "B", Operator.ADD)
        assert calc.evaluate() == 21

    def test_evaluate_mod(self):
        calc = Calculator("19", "A", Operator.MOD)  # 25 mod 10
        assert calc.evaluate() == 5 
