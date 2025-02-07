from click.testing import CliRunner
from hex_trainer import cli

def test_hex_to_int():
    runner = CliRunner()
    result = runner.invoke(cli, args=['hex-to-int'], input="256")
    assert "What is the decimal equivalent of " in result.output
    assert "Incorrect" in result.output

def test_int_to_hex():
    runner = CliRunner()
    result = runner.invoke(cli, args=['int-to-hex'], input="99\n0xFFF")
    assert "What is the hexadecimal equivalent of " in result.output
    assert "Incorrectly formatted answer." in result.output
    assert "Incorrect" in result.output

def test_solve_equation():
    runner = CliRunner()
    result = runner.invoke(cli, args=['solve-equation'], input="ADD,MULTIPLY\n0")
    assert "Possible values are ADD, SUBTRACT, MULTIPLY, DIVIDE, and MOD." in result.output
    assert "Your answer" in result.output
    assert "Incorrect" in result.output

def test_solve_equation_answer_in_hex():
    runner = CliRunner()
    result = runner.invoke(cli, args=['solve-equation', '--answer-in-hex'], input="ADD\n99\n0x99")
    assert "Incorrectly formatted answer." in result.output
    assert "Your answer" in result.output
    assert "Incorrect" in result.output
