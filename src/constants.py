from enum import Enum

class Operator(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "//"
    MOD = "%"

OPERATOR_NAMES = [op.name for op in [*Operator]]

HEX_REGEX = "0x[0-9a-fA-F]+"
