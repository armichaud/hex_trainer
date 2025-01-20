from random import randint
from typing import Optional

class HexVar:
    def __init__(self, s: Optional[str] = None):
        self.int_val = randint(1, 255) if s is None else HexVar.to_int(s)
        self.val = hex(self.int_val)

    @classmethod
    def from_hex_str(cls, s: str):
        return cls(s)
    
    @staticmethod
    def to_int(s: str):
        return int(s.strip(), 16)
    
    def to_str(self) -> str:
        return self.val
