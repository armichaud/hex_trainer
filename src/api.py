from typing import Optional
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

from src.constants import Operator
from src.equation import Equation
from src.hex_var import HexVar

app = FastAPI()

class Conversion(BaseModel):
    hex: str
    answer: int

class Solution(BaseModel):
    operand_1: str
    operand_2: str
    operator: str
    answer: int

@app.get("/hex")
def get_hex_value():
    return {"hex": HexVar().to_str()}

@app.get("/equation")
def get_equation(
    add: Optional[bool] = None, 
    sub: Optional[bool] = None,
    mul: Optional[bool] = None,
    div: Optional[bool] = None,
    mod: Optional[bool] = None
):
    ops = [op for include, op in zip([add, sub, mul, div, mod], [*Operator]) if include]
    equation = Equation.generate() if not ops else Equation.generate(ops)
    a, b = equation.operands
    return {"operand_1": a.to_str(), "operand_2": b.to_str(), "operator": equation.operator.name}

@app.post("/check_conversion")
def check_conversion(conversion: Conversion, response: Response):
    if HexVar.to_int(conversion.hex) == conversion.answer:
        return {"result": "correct"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"result": "incorrect"}


@app.post("/evaluate")
def evaluate_solution(solution: Solution, response: Response):
    equation = Equation.build_from_terms(
        operand_1=solution.operand_1, 
        operand_2=solution.operand_2, 
        operator=solution.operator
    )
    if equation.check_answer(solution.answer):
        return {"result": "correct"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"result": "incorrect"}
