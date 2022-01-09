
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_tennis_game_points import tennis_game_points


class TestSolution(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(tennis_game_points("15-love"), 1)
        self.assertEqual(tennis_game_points("love-15"), 1)
        self.assertEqual(tennis_game_points("30-love"), 2)
        self.assertEqual(tennis_game_points("15-all"), 2)
        self.assertEqual(tennis_game_points("love-30"), 2)
        self.assertEqual(tennis_game_points("30-15"), 3)
        self.assertEqual(tennis_game_points("15-30"), 3)
        self.assertEqual(tennis_game_points("40-love"), 3)
        self.assertEqual(tennis_game_points("love-40"), 3)
        self.assertEqual(tennis_game_points("40-15"), 4)
        self.assertEqual(tennis_game_points("30-all"), 4)
        self.assertEqual(tennis_game_points("15-40"), 4)
        self.assertEqual(tennis_game_points("40-30"), 5)
        self.assertEqual(tennis_game_points("30-40"), 5)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()