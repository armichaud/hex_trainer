import re
import click
import time

from src.constants import HEX_REGEX, OPERATOR_NAMES, Operator
from src.equation import Equation
from src.hex_var import HexVar

def valid_hex_string(s: str):
    if re.match(HEX_REGEX, s):
        return True
    click.echo(f"Incorrectly formatted answer.")
    return False

@click.group()
def cli():
    pass

@click.command()
def hex_to_int():
    hex = HexVar()
    start_time = time.perf_counter()
    answer = click.prompt(text=f"What is the decimal equivalent of {hex.str_val}?\n", prompt_suffix=">", type=int)
    elapsed_time = time.perf_counter() - start_time
    click.echo(f"Correct! You answered in {elapsed_time: .2f} seconds." if answer == hex.int_val else f"Incorrect. The answer was {hex.int_val}.")

@click.command()
def int_to_hex():
    hex = HexVar()
    start_time = time.perf_counter()
    click.echo(f"What is the hexadecimal equivalent of {hex.int_val}?")
    answer = click.prompt("Your answer", type=str)
    while not valid_hex_string(answer):
        answer = click.prompt("Your answer", type=str)
    if HexVar.from_hex_str(answer).int_val == hex.int_val:
        elapsed_time = time.perf_counter() - start_time
        click.echo(f"Correct! You solved this in {elapsed_time: .2f} seconds.")
    else:
        click.echo(f"Incorrect. The answer was {hex.str_val}.")


@click.command()
@click.option("--answer-in-hex", is_flag=True, help="answer will be given as a hexadecimal")
def solve_equation(answer_in_hex: bool):
    operators = click.prompt(
        text="""
            Provide a comma-separated list of operators you'd like to be tested on. 
            Possible values are ADD, SUBTRACT, MULTIPLY, DIVIDE, and MOD.
            If the input is not properly formatted or contains no valid operators,
            all operators will be considered possible options.
        """,
        prompt_suffix=">",
        type=str
    )
    ops = [Operator[op] for op in operators.split(",") if op in OPERATOR_NAMES]
    equation = Equation().generate() if not ops else Equation.generate(ops)
    click.echo(equation.to_str())
    start_time = time.perf_counter()
    answer = click.prompt("Your answer", type=str if answer_in_hex else int)
    if answer_in_hex:
        while not valid_hex_string(answer):
            answer = click.prompt("Your answer", type=str)
    answer = HexVar.to_int(answer) if answer_in_hex else int(answer)
    elapsed_time = time.perf_counter() - start_time
    click.echo(f"Correct! You answered in {elapsed_time: .2f} seconds." if equation.check_answer(answer) else f"Incorrect. The answer was {HexVar.from_int(equation.answer).str_val if answer_in_hex else equation.answer}.")

cli.add_command(hex_to_int)
cli.add_command(int_to_hex)
cli.add_command(solve_equation)

if __name__ == '__main__':
    cli()
