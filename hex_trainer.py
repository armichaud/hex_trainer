import re
import click
import time

from src.constants import OPERATOR_NAMES, Operator
from src.equation import Equation
from src.hex_var import HexVar

@click.group()
def cli():
    pass

@click.command()
def hex_to_int():
    hex = HexVar()
    start_time = time.perf_counter()
    answer = click.prompt(f"What is the decimal equivalent of {hex.str_val()}?", type=int)
    elapsed_time = time.perf_counter() - start_time
    click.echo(f"Correct! You answered in {elapsed_time: .2f} seconds." if answer == hex.int_val else f"Incorrect. The answer was {hex.int_val}.")

@click.command()
def int_to_hex():
    hex = HexVar()
    start_time = time.perf_counter()
    answer = click.prompt(
        f"""
            What is the hexidecimal equivalent of {hex.int_val}?
            Type your answer like so: F6
            Do not include a prefix indicating a hexidecimal, e.g. 0xF6
        """, 
        type=str
    )
    correct_answer = hex.str_val()
    if not re.match("[0-9a-fA-F]+", answer):
        click.echo("Incorrectly formatted answer. The correct answer was {correct_answer}.")
    elif answer == correct_answer:
        elapsed_time = time.perf_counter() - start_time
        click.echo("Correct! You solved this in {elapsed_time: .2f} seconds.")
    else:
        click.echo(f"Incorrect. The answer was {hex.str_val()}.")


@click.command()
def solve_equation():
    operators = click.prompt(
        """
            Provide a comma-separated list of operators you'd like to be tested on. 
            Possible values are ADD, SUBTRACT, MULTIPLY, DIVIDE, and MOD.
            If the input is not properly formatted or contains no valid operators,
            all operators will be considered possible options.
        """, 
        type=str
    )
    ops = [Operator[op] for op in operators.split(",") if op in OPERATOR_NAMES]
    equation = Equation().generate() if not ops else Equation.generate(ops)
    click.echo(equation.to_str())
    start_time = time.perf_counter()
    answer = click.prompt("Your answer", type=int)
    elapsed_time = time.perf_counter() - start_time
    click.echo(f"Correct! You answered in {elapsed_time: .2f} seconds." if equation.check_answer(answer) else f"Incorrect. The answer was {equation.answer}.")

cli.add_command(solve_equation)
cli.add_command(hex_to_int)

if __name__ == '__main__':
    cli()
