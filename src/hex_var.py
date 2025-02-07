from random import randint
import re

from src.constants import HEX_REGEX
from src.exceptions import InvalidHexadecimalException


class HexVar:
    def __init__(self):
        self._set_int_val()
        self._set_str_val()

    @classmethod
    def from_hex_str(cls, s: str):
        hex_var = cls()
        hex_var.int_val = HexVar.to_int(s)
        hex_var._set_str_val()
        return hex_var
    
    @classmethod
    def from_int(cls, n: int):
        hex_var = cls()
        hex_var.int_val = n
        hex_var._set_str_val()
        return hex_var
    
    @staticmethod
    def to_int(s: str) -> int:
        if not re.match(HEX_REGEX, s):
            raise InvalidHexadecimalException(s)
        return int(s.strip(), 16)

    def _set_int_val(self):
        self.int_val = randint(1, 255)
    
    def _set_str_val(self) -> None:
        # someday I may enable users to configure the number of digits
        self.str_val = "0x{:02X}".format(self.int_val)
