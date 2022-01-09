"""
Python solution for challenge: "Hex to Decimal"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def hex_to_dec(hex_number):
    """
    This function returns an integer (base = 10) from a hexadecimal number (base = 16).
    Returns 0 if no arguments are provided.
    """
    return int(hex_number, 16)
