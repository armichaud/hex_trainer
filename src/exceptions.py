# exceptions.py

class InvalidHexadecimalException(BaseException):
    def __init__(self, s: str):
        self.message = f"Attempted to process improperly formatted string as hexadecimal: {s}"
        super().__init__(self.message)
