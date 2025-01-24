import click

from src.constants import OPERATOR_NAMES, Operator
from src.equation import Equation
from src.hex_var import HexVar

@click.group()
def cli():
    pass

@click.command()
def hex_to_int():
    hex = HexVar()
    answer = click.prompt(f"What is the decimal equivalent of {hex.to_str()}?", type=int)
    click.echo("Correct!" if answer == hex.int_val else f"Incorrect. The answer was {hex.int_val}")

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
    equation = Equation() if not ops else Equation(ops)
    click.echo(equation.to_str())
    answer = click.prompt("Your answer: ", type=int)
    click.echo("Correct!" if equation.check_answer(answer) else f"Incorrect. The answer was {equation.answer}")

cli.add_command(solve_equation)
cli.add_command(hex_to_int)

if __name__ == '__main__':
    cli()
