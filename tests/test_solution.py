from src.solution import Solution

class TestSolution:

    def test_get_result_addition(self):
        solution = Solution("A", "B", "ADD")
        solution._get_result() 
        assert solution.result == 21

    def test_get_result_subtraction(self):
        solution = Solution("10", "5", "SUBTRACT")
        solution._get_result()
        assert solution.result == 11

    def test_get_result_multiplication(self):
        solution = Solution("2", "C", "MULTIPLY")
        solution._get_result() 
        assert solution.result == 24

    def test_get_result_division(self):
        solution = Solution("F", "3", "DIVIDE")
        solution._get_result()
        assert solution.result == 5

    def test_check_answer_correct(self):
        solution = Solution("A", "B", "ADD")
        assert solution.check_answer(21)

    def test_check_answer_incorrect(self):
        solution = Solution("A", "B", "ADD")
        assert not solution.check_answer(20)

    def test_check_answer_mod(self):
        solution = Solution("19", "A", "MOD")  # 25 mod 10
        assert solution.check_answer(5)
