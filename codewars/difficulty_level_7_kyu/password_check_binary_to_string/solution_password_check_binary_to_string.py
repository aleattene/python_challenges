"""
Python solution for challenge: "Password Check - Binary to String"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def decode_pass(pass_list, bits):
    # Construction of the password starting from a string (of binary numbers)
    pwd = "".join(chr(int(char, 2)) for char in bits.split(" "))
    # Return the password if correct or return false
    return pwd if pwd in pass_list else False
