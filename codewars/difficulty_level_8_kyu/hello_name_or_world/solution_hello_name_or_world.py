"""
Python solution for challenge: "Hello, Name or World!"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def hello(name=""):
    return f'Hello, {name.capitalize()}!' if name else "Hello, World!"
