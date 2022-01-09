"""
Python solution for challenge: "Moving Zeros To The End"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def move_zeros(sequence):
    # Declaration of variables
    length = len(sequence) - 1
    i = 0
    while True:
        # Stop the cycle when the original sequence has been fully analyzed
        if i > length:
            break
        # If a zero is found it is placed at the end
        if not sequence[i]:
            sequence.pop(i)
            i -= 1
            sequence.append(0)
            length -= 1
        # The iteration continues
        i += 1
    # Returns the modified sequence
    return sequence
