"""
Python solution for challenge: "Pandemia"
To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py
"""


def infected(s):
    # From string to list using "X" separator (ocean)
    all_continents = s.split("X")
    people_total, people_infected = 0, 0
    for continent in all_continents:
        people_continent = len(continent)
        # Number of people on each continent
        people_total += people_continent
        if "1" in continent:
            # If there is an infected person on the continent, all the others become infected as well
            people_infected += 1 * people_continent
    return 0 if not people_total else (people_infected / people_total) * 100
