from src.constants import Operator
from src.hex_var import HexVar

class Solution:
    def __init__(self, a: str, b: str, op: str):
        self.a = HexVar.from_hex_str(a)
        self.b = HexVar.from_hex_str(b)
        self.op = Operator[op]
        self._get_result()
            
    def _get_result(self):
        self.result = eval(f"{self.a.int_val}{self.op.value}{self.b.int_val}")
    
    def check_answer(self, answer: int):
        return answer == self.result
