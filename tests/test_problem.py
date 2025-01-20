import pytest
from src.constants import Operation
from src.hex_var import HexVar
from src.problem import Problem

class TestProblem:

    def test_generate_problem_valid_operations(self):
        problem = Problem()

        a, b, op = problem._generate_problem()  

        assert isinstance(a, HexVar)
        a_hex = a.to_str()
        assert a_hex.startswith("0x")
        int(a_hex, 16)  # Try converting to int to ensure it's a valid hex

        assert isinstance(b, HexVar)
        b_hex = b.to_str()
        assert b_hex.startswith("0x")
        int(b_hex, 16)  # Try converting to int to ensure it's a valid hex

        assert op in [*Operation]
