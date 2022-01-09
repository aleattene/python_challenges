"""
Python solution for challenge: "Tennis Game Points"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def tennis_game_points(score):
    # From call to points
    call_points = {"love": 0, "15": 1, "30": 2, "40": 3}
    # From string to list (using the separator "-")
    calls = score.split("-")
    # First player points
    points = call_points[calls[0]]
    # Second player points
    if calls[1] in call_points:
        # different score
        points += call_points[calls[1]]
    else:
        # same score
        points *= 2
    # Total score
    return points
