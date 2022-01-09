"""
Python solution for challenge: "Unique In Order"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def unique_in_order(iterable):
    items = []
    # Empty iterable
    if len(iterable) == 0:
        return items
    # The iterable is not empty
    i = 0
    items.append(iterable[0])
    # Check if the current item is a duplicate of the previous one
    for item in iterable[1:]:
        # If it is not a duplicate it is added to the list of items
        if item != items[i]:
            items.append(item)
            i += 1
    return items
