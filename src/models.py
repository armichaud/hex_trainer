from typing import Union
from pydantic import BaseModel


class HexConversion(BaseModel):
    hex: str
    answer: int

class IntConversion(BaseModel):
    n: int
    answer: str

class Solution(BaseModel):
    operand_1: str
    operand_2: str
    operator: str
    answer: Union[int, str]
    