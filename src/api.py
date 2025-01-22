from typing import Optional
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

from src.constants import Operator
from src.equation import Equation
from src.solution import Solution

app = FastAPI()

class Attempt(BaseModel):
    operand_1: str
    operand_2: str
    operator: str
    answer: int

@app.get("/equation")
def get_equation(
    add: Optional[bool] = None, 
    sub: Optional[bool] = None,
    mul: Optional[bool] = None,
    div: Optional[bool] = None,
    mod: Optional[bool] = None
):
    ops = [op for include, op in zip([add, sub, mul, div, mod], [*Operator]) if include]
    equation = Equation() if not ops else Equation(ops)
    a, b = equation.operands
    return {"operand_1": a.to_str(), "operand_2": b.to_str(), "operator": equation.operator.name}

@app.post("/evaluate")
def evaluate_solution(attempt: Attempt, response: Response):
    if Solution(a=attempt.operand_1, b=attempt.operand_2, op=attempt.operator).check_answer(attempt.answer):
        return {"answer": "correct"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"answer": "wrong"}
