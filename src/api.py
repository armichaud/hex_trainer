from typing import Optional
from fastapi import FastAPI, Response, status

from src.constants import Operator
from src.equation import Equation
from src.hex_var import HexVar
from src.models import HexConversion, IntConversion, Solution

app = FastAPI()

@app.get("/")
def health_check():
    return {}

@app.get("/hex")
def get_hex_value():
    return {"hex": HexVar().str_val}

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
    return {"operand_1": a.str_val, "operand_2": b.str_val, "operator": equation.operator.name}

@app.post("/check_hex_conversion")
def check_hex_conversion(conversion: HexConversion, response: Response):
    if HexVar.to_int(conversion.hex) == conversion.answer:
        return {"result": "correct"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"result": "incorrect"}


@app.post("/check_int_conversion")
def check_int_conversion(conversion: IntConversion, response: Response):
    if conversion.n == HexVar.from_hex_str(conversion.answer).int_val:
        return {"result": "correct"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"result": "incorrect"}


@app.post("/evaluate")
def evaluate_solution(
    solution: Solution,
    response: Response,
    answer_in_hex: Optional[bool] = None,
):
    equation = Equation.build_from_terms(
        operand_1=solution.operand_1, 
        operand_2=solution.operand_2, 
        operator=solution.operator
    )
    answer = HexVar.to_int(solution.answer) if answer_in_hex else solution.answer
    if equation.check_answer(answer):
        return {"result": "correct"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"result": "incorrect"}
