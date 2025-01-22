from typing import Optional
from fastapi import FastAPI

from src.constants import Operator
from src.equation import Equation

app = FastAPI()

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
    return {"operand_1": a.to_str(), "operand_2": b.to_str(), "operator": equation.operation.name}
