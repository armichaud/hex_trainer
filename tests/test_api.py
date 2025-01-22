import re
from fastapi.testclient import TestClient
from src.api import app
from src.constants import Operator

HEX_REGEX = "0x[0-9a-fA-F]+"
OPERATOR_NAMES = [op.name for op in [*Operator]]

client = TestClient(app=app)

def test_get_equation():
    response = client.get("/equation")
    assert response.status_code == 200
    data = response.json()
    assert re.match(HEX_REGEX, data.get("operand_1"))
    assert re.match(HEX_REGEX, data.get("operand_2"))
    assert data.get("operator") in OPERATOR_NAMES

    response = client.get("/equation?mod=1")
    assert response.status_code == 200
    data = response.json()
    assert data.get("operator") == Operator.MOD.name

    response = client.get("/equation?mod=true")
    assert response.status_code == 200
    data = response.json()
    assert data.get("operator") == Operator.MOD.name

    response = client.get("/equation?sub=1&mul=0")
    assert response.status_code == 200
    data = response.json()
    assert data.get("operator") == Operator.SUBTRACT.name
