from src.constants import Operator
from src.hex_var import HexVar

class Calculator:
    def __init__(self, a: str, b: str, op: Operator):
        self.a = HexVar.from_hex_str(a)
        self.b = HexVar.from_hex_str(b)
        self.op = op
        self.result = self._get_result()
            
    def _get_result(self):
        return eval(f"{self.a.int_val}{self.op.value}{self.b.int_val}")
    
    def check_result(self, answer: int):
        return answer == self.result

    def evaluate(self):
        return self.result
