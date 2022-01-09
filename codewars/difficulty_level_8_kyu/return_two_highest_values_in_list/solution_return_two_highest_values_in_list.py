"""
Python solution for challenge: "Return Two Highest Values in List"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def two_highest(arg1):
    # Empty list or with only one element
    if len(arg1) < 2:
        return arg1
    # List with two or more elements
    highest_values = []
    # Ascending order
    arg1.sort()
    # Descending order
    arg1.reverse()
    # The first element is certainly the largest
    highest_values.append(arg1[0])
    # If there is another element lower than the previous one, both are immediately (see break) returned
    for value in arg1[1:]:
        if value != highest_values[0]:
            highest_values.append(value)
            break
    return highest_values
