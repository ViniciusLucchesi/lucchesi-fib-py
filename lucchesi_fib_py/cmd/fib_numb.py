import argparse

from lucchesi_fib_py.fib_calcs.fib_number import recurring_fibonacci_number


def fib_numb() -> None:
    parse = argparse.ArgumentParser(description='Calculate Fibonacci numbers')
    parse.add_argument('--number', action='store', type=int, required=True, help="Fibonaci number to be calculated")

    args = parse.parse_args()
    print(f"Your Fibonacci number is: {recurring_fibonacci_number(number=args.number)}")
