import pytest

from src.hex_var import HexVar

class TestHexVar:

    def test_hex_to_int_valid(self):
        assert HexVar.to_int("1A") == 26
        assert HexVar.to_int("FF") == 255
        assert HexVar.to_int("0") == 0
        assert HexVar.to_int("1A ") == 26

    def test_hex_to_int_invalid(self):
        with pytest.raises(ValueError):
            HexVar.to_int("G")  # Invalid hex character
        with pytest.raises(AttributeError):
            HexVar.to_int(123)  # Incorrect input type
