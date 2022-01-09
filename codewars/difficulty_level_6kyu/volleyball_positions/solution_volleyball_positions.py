"""
Python solution for challenge: "Volleyball Positions"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def volleyball_positions(formation, k):
    # Every six rotations the team returns to the same position
    rotations = k % 6
    # performing backwards rotations
    while True:
        if rotations == 0:
            break
        player_zone_one = formation[3][2]
        player_zone_two = formation[1][2]
        player_zone_three = formation[0][1]
        player_zone_four = formation[1][0]
        player_zone_five = formation[3][0]
        player_zone_six = formation[2][1]
        formation[3][2] = player_zone_six
        formation[1][2] = player_zone_one
        formation[0][1] = player_zone_two
        formation[1][0] = player_zone_three
        formation[3][0] = player_zone_four
        formation[2][1] = player_zone_five
        rotations -= 1
    # Return the initial formation
    return formation



