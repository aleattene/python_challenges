"""
Python solution for challenge: "Regex Password Validation"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""

import re


def check_password(password):
    r"""
    ^                                       Start anchor
    (?=.*[A-Z])                             Check that the string contains at least one uppercase letter
    (?!.*[.,;!\_\\\@#\/$&*\-\+\?\s])        Check that the string does not contain any special letter
    (?=.*[0-9])                             Check that the string contains at least one digit
    (?=.*[a-z])                             Check that the string contains at least one uppercase letter
    .{6,}                                   Check that the string is at least 6 characters long
    $                                       End anchor
    """
    match = re.search(r'^(?!.*[.,;!\_\\\@#\/$&*\-\+\?\s])(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{6,}$', password)
    return True if match else False
