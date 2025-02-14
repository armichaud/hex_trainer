import re
from fastapi.testclient import TestClient
from src.api import app
from src.constants import HEX_REGEX, OPERATOR_NAMES, Operator

client = TestClient(app=app)

def test_get_hex():
    response = client.get("/hex")
    data = response.json()
    assert re.match(HEX_REGEX, data.get("hex"))

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

def test_post_solution():
    correct_attempt = {
        "operand_1": "0x1F",
        "operand_2": "0x08",
        "operator": "ADD",
        "answer": 39
    }
    response = client.post(
        "/evaluate",
        json=correct_attempt
    )
    assert response.json() == {"result": "correct"}
    assert response.status_code == 200

    incorrect_attempt = {**correct_attempt, "answer": 40}
    response = client.post(
        "/evaluate",
        json=incorrect_attempt
    )
    assert response.json() == {"result": "incorrect"} 
    assert response.status_code == 400

    correct_hex_answer = {**correct_attempt, "answer": "0x27"}
    response = client.post(
        "/evaluate?answer_in_hex=1",
        json=correct_hex_answer
    )
    assert response.json() == {"result": "correct"}
    assert response.status_code == 200


    incorrect_hex_answer = {**correct_attempt, "answer": "0x26"}
    response = client.post(
        "/evaluate?answer_in_hex=1",
        json=incorrect_hex_answer
    )
    assert response.json() == {"result": "incorrect"}
    assert response.status_code == 400

def test_check_hex_conversion():
    correct_conversion = {
        "hex": "0x1F",
        "answer": 31
    }
    response = client.post(
        "/check_hex_conversion",
        json=correct_conversion
    )
    assert response.json() == {"result": "correct"}
    assert response.status_code == 200

    incorrect_conversion = {
        "hex": "0x1F",
        "answer": 30
    }
    response = client.post(
        "/check_hex_conversion",
        json=incorrect_conversion
    )
    assert response.json() == {"result": "incorrect"}
    assert response.status_code == 400 

def test_check_int_conversion():
    correct_conversion = {
        "answer": "0x1F",
        "n": 31
    }
    response = client.post(
        "/check_int_conversion",
        json=correct_conversion
    )
    assert response.json() == {"result": "correct"}
    assert response.status_code == 200

    incorrect_conversion = {
        "answer": "0x1F",
        "n": 30
    }
    response = client.post(
        "/check_int_conversion",
        json=incorrect_conversion
    )
    assert response.json() == {"result": "incorrect"}
    assert response.status_code == 400
