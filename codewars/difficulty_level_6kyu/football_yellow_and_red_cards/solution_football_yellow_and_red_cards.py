"""
Python solution for challenge: "Football Yellow and Red Cards"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def men_still_standing(cards):
    teams_cards = {"AY": [], "AR": [], "BY": [], "BR": []}
    for value in cards:
        team, card, player = value[0], value[-1], value[1:-1]
        # The player has already been sent off (red card)
        if player in teams_cards[team+"R"]:
            continue
        # The player has already been booked (yellow card)
        elif player in teams_cards[team+"Y"]:
            teams_cards[team+"Y"].remove(player)
            # the player is added to the expelled players
            teams_cards[team+"R"].append(player)
        # The player was neither cautioned nor sent off
        else:
            # the player is added to the booked players
            teams_cards[team+card].append(player)
        # Check if a team is left with less than 7 players
        if 11 - len(teams_cards["AR"]) < 7 or 11 - len(teams_cards["BR"]) < 7:
            break
    # Return a tuple with the number of players left in each team
    return 11 - len(teams_cards["AR"]), 11 - len(teams_cards["BR"])
