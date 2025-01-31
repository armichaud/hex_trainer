from random import randint


class HexVar:
    def __init__(self):
        self.int_val = randint(1, 255) 
        self._get_val()

    @classmethod
    def from_hex_str(cls, s: str):
        hex_var = cls()
        hex_var.int_val = HexVar.to_int(s)
        hex_var._get_val()
        return hex_var
    
    @staticmethod
    def to_int(s: str) -> int:
        # TODO add error handling
        return int(s.strip(), 16)
    
    def str_val(self) -> str:
        return self.val
    
    def _get_val(self) -> None:
        hex_raw = hex(self.int_val)
        self.val = hex_raw[:2] + hex_raw[2:].upper()
