from typing import Optional
from fastapi import FastAPI

from src.constants import Operation
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
    ops_zipped = zip([add, sub, mul, div, mod], [*Operation])
    ops = [op for include, op in ops_zipped if include]
    equation = Equation(ops)
    a, b = equation.operands
    return {"operand_1": a.to_str(), "operand_2": b.to_str(), "operation": equation.operation.name}
