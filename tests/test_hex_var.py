import pytest

from src.exceptions import InvalidHexadecimalException
from src.hex_var import HexVar

class TestHexVar:

    def test_hex_to_int_valid(self):
        assert HexVar.to_int("0x1A") == 26
        assert HexVar.to_int("0xFF") == 255
        assert HexVar.to_int("0x0") == 0
        assert HexVar.to_int("0x1A ") == 26

    def test_hex_to_int_invalid(self):
        with pytest.raises(InvalidHexadecimalException):
            HexVar.to_int("G")  # Invalid hex character
        with pytest.raises(TypeError):
            HexVar.to_int(123)  # Incorrect input type
