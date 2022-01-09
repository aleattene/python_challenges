
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_football_yellow_and_red_cards import men_still_standing


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(men_still_standing([]), (11, 11))
        self.assertEqual(men_still_standing(["A4Y", "A4Y"]), (10, 11))
        self.assertEqual(men_still_standing(["A4Y", "A4R"]), (10, 11))
        self.assertEqual(men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"]), (9, 10))
        self.assertEqual(men_still_standing(["A4R", "A4R", "A4R"]), (10, 11))
        self.assertEqual(men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"]), (6, 11))
        pass

    def test_advanced_cases(self):
        self.assertEqual(men_still_standing(['A11R', 'A8Y', 'B1R', 'A10Y', 'A9Y']), (10, 10))
        self.assertEqual(men_still_standing(['A8Y', 'B5Y', 'A8Y', 'B9R', 'A6R', 'B6Y', 'B7R', 'B7R', 'A6Y', 'A11R',
                                             'B9R', 'A4R', 'A2Y', 'B10Y']), (7, 9))
        self.assertEqual(men_still_standing(['A5Y', 'A2Y', 'A10Y', 'A1R', 'A6Y', 'B2R', 'B6Y']), (10, 10))
        self.assertEqual(men_still_standing(['B7Y', 'A5Y', 'B1Y', 'B6Y', 'A1Y', 'A9R', 'A10R', 'B7Y', 'B1Y', 'A10R',
                                             'B7Y', 'A1Y', 'B2Y', 'A11R', 'A3Y', 'B3Y', 'A4Y', 'B10R', 'B1R',
                                             'B2Y']), (7, 7))
        self.assertEqual(men_still_standing(['A3Y', 'B3Y', 'B11Y', 'A2Y', 'A2Y', 'A1R', 'A7Y', 'A2R', 'B2Y', 'A9Y',
                                             'A10Y', 'A6R', 'A6R', 'A1R', 'B3R', 'A8Y', 'A11Y', 'B4Y', 'B6Y']), (8, 10))
        self.assertEqual(men_still_standing(['A4R', 'A8Y', 'A5Y', 'B5Y', 'A5Y', 'B1R', 'B2R', 'B8R', 'A9Y']), (9, 8))
        self.assertEqual(men_still_standing(['A1R', 'A11R', 'A5R', 'A2Y', 'A10Y', 'B8R', 'B4R', 'B10R', 'A6R', 'A7Y',
                                             'A1R', 'A8Y', 'A9R']), (6, 8))
        self.assertEqual(men_still_standing(['A11R', 'B1Y', 'A9Y', 'B7R', 'A8Y', 'A3Y', 'B1Y', 'B5Y', 'B8Y', 'B4R',
                                             'A2R', 'A11Y']), (9, 8))
        self.assertEqual(men_still_standing(['B3R', 'B2R', 'A3Y', 'B1Y', 'B1Y', 'B7R', 'B3Y', 'A11R']), (10, 7))
        self.assertEqual(men_still_standing(['A4Y', 'B11Y', 'A2R', 'B4R', 'A9Y', 'A4R', 'A9R', 'A11Y', 'B1Y', 'B4Y',
                                             'B8Y', 'A1Y', 'B11R', 'A4Y', 'A10Y', 'B8R', 'B8R']), (8, 8))
        self.assertEqual(men_still_standing(['A4Y', 'B11Y', 'A8Y', 'A10R', 'B7Y', 'A1Y', 'A11R', 'A2Y', 'A1R', 'A4Y',
                                             'A5R', 'A4Y', 'B3Y', 'B6R', 'A7Y']), (6, 11))
        self.assertEqual(men_still_standing(['B3Y', 'B7R', 'B1Y', 'B6Y', 'A11R', 'B6Y', 'B8Y', 'A4Y', 'B9Y', 'B11Y',
                                             'B8Y']), (10, 8))
        self.assertEqual(men_still_standing(['A1R', 'B5Y', 'B6Y', 'B9R', 'B1R', 'A11Y', 'B6Y', 'A4Y', 'B2Y', 'B9Y',
                                             'A10Y', 'A11R', 'B5Y', 'B8R', 'A11R']), (9, 6))
        self.assertEqual(men_still_standing(['A5Y', 'A1R', 'A3R', 'A10R', 'B6Y', 'B5Y', 'B8Y', 'B2Y', 'B11R', 'B7Y',
                                             'A10Y']), (8, 10))
        self.assertEqual(men_still_standing(['B2Y', 'A8Y', 'A6Y', 'B11Y', 'A1Y', 'A5Y', 'A6Y', 'A9R', 'A11Y', 'A1Y',
                                             'A1R', 'A10R', 'B3Y', 'B8Y', 'A8Y']), (6, 11))
        self.assertEqual(men_still_standing(['B5Y', 'A9Y', 'A5R', 'B8Y', 'A11Y', 'B9Y', 'A6Y', 'B8Y']), (10, 10))
        self.assertEqual(men_still_standing(['A9R', 'B9R', 'B7Y', 'B9Y', 'A3R', 'B1Y', 'A3Y', 'A9R', 'A4Y', 'B7Y',
                                             'B4Y', 'B8Y', 'A9Y', 'A8R', 'B7Y', 'B6Y', 'B10Y', 'A10Y', 'A5Y', 'A10R',
                                             'B2Y', 'B10Y', 'A8Y']), (7, 8))
        self.assertEqual(men_still_standing(['A9Y', 'B10R', 'A5Y', 'A1Y', 'B1R', 'A4R']), (10, 9))
        self.assertEqual(men_still_standing(['B11R', 'B3R', 'A10Y', 'B1Y', 'A9Y', 'B11Y', 'B4Y', 'A6Y', 'A11Y', 'B1R',
                                             'A9Y', 'B3R', 'A3Y', 'A2Y', 'B2Y', 'B4R']), (10, 7))
        self.assertEqual(men_still_standing(['B4Y', 'B4Y', 'B4Y', 'A1Y', 'A9Y', 'B3Y', 'B1Y', 'A9Y', 'A11R', 'A1R',
                                             'B7Y', 'B5R', 'B7Y', 'B1Y']), (8, 7))
        self.assertEqual(men_still_standing(['A2R', 'A2Y', 'B9Y', 'B6Y']), (10, 11))
        self.assertEqual(men_still_standing(['B6R', 'B6R', 'A9Y', 'B4R', 'A5Y', 'A9R', 'A10R', 'A9Y', 'A11Y', 'A2R',
                                             'B2Y', 'A3R', 'B11Y', 'B4Y', 'A7Y', 'A3Y']), (7, 9))
        self.assertEqual(men_still_standing(['B2Y', 'B2Y', 'A10R', 'A8R', 'A8Y', 'B11R', 'A11Y', 'A5R', 'A8R', 'A10R',
                                             'B8R']), (8, 8))
        self.assertEqual(men_still_standing(['B7R', 'B10Y', 'B6Y', 'A3Y']), (11, 10))
        self.assertEqual(men_still_standing(['A10Y', 'A9R', 'A2R', 'B5Y', 'A8Y', 'B8R', 'A11R', 'B3Y', 'B5Y', 'A6R',
                                             'B3Y', 'B7Y', 'B1Y', 'A6R', 'A6Y', 'A9R', 'B3Y']), (7, 8))
        self.assertEqual(men_still_standing(['B6R', 'B7Y', 'A2Y', 'B2Y', 'A11Y', 'B11R', 'B10Y', 'B7R', 'A1Y', 'B7Y',
                                             'B7Y', 'A3Y', 'A4Y', 'B5Y', 'B3R', 'B4R', 'A2Y', 'A2R', 'A2R', 'A3Y',
                                             'A4R', 'A3Y', 'A5Y']), (11, 6))
        self.assertEqual(men_still_standing(['B9R', 'B9Y', 'B7Y', 'B11Y', 'B6R', 'A1Y', 'B6R', 'B6Y', 'A8Y', 'B8Y',
                                             'B11Y', 'B10R', 'A9Y', 'B10R', 'A2Y', 'A9R', 'B10Y']), (10, 7))
        self.assertEqual(men_still_standing(['B5Y', 'B6Y', 'B4R', 'A3Y', 'A3Y', 'A3Y', 'A11R', 'B6Y', 'B9Y',
                                             'B8Y']), (9, 9))
        self.assertEqual(men_still_standing(['A5R', 'A4R', 'B8Y', 'A6Y', 'A8R', 'B7R', 'B9Y', 'B6Y', 'B4Y', 'A5Y',
                                             'A1Y', 'A10Y', 'B6Y', 'B1R', 'B8R', 'B8R', 'B7R', 'A2Y', 'B6R', 'A2Y',
                                             'B11Y', 'B10Y', 'B8R']), (7, 7))
        self.assertEqual(men_still_standing(['A9Y', 'A11Y', 'A10Y', 'A3Y']), (11, 11))
        self.assertEqual(men_still_standing(['B5R', 'A6Y', 'B2Y', 'A2Y', 'A5R', 'A6Y']), (9, 10))
        self.assertEqual(men_still_standing(['A9R', 'B5Y', 'A11R', 'B11Y', 'A11R', 'A6Y', 'B5R', 'A10Y', 'B6Y', 'A9Y',
                                             'B7R', 'A5R', 'B10R', 'B7Y', 'B11Y', 'B4Y', 'B7Y', 'A6Y', 'A10Y', 'B7Y',
                                             'A11Y', 'A11Y', 'B10R', 'A2Y']), (6, 7))
        self.assertEqual(men_still_standing(['B2Y', 'A4Y', 'A10Y', 'B10Y', 'A3Y', 'B3Y', 'A7R', 'A10Y', 'A5Y', 'A2R',
                                             'A11Y', 'B5Y', 'A7Y', 'B1R', 'B1Y', 'B6Y', 'B9Y', 'A8R', 'B1Y', 'B1Y',
                                             'A5Y']), (6, 10))
        self.assertEqual(men_still_standing(['B4R']), (11, 10))
        self.assertEqual(men_still_standing(['B10R']), (11, 10))
        self.assertEqual(men_still_standing(['A5Y', 'A7Y']), (11, 11))
        self.assertEqual(men_still_standing(['B10Y', 'B9Y', 'A8Y', 'A8Y', 'A3R', 'A8Y', 'A6Y', 'B11Y', 'A6Y', 'A3Y',
                                             'A8R', 'B5Y', 'B5Y', 'B1Y', 'B10R', 'A2Y', 'A8R', 'A1Y', 'B7Y',
                                             'B11R']), (8, 8))
        self.assertEqual(men_still_standing(['B2Y', 'A3R', 'A2R', 'B5R', 'B2Y', 'B5Y', 'A8Y', 'B5Y', 'B8Y', 'B3Y',
                                             'B11R', 'B11Y']), (9, 8))
        self.assertEqual(men_still_standing(['B9Y', 'A9R', 'A9Y', 'B8R', 'A8R', 'A9R', 'A8R', 'B10R', 'B9R', 'A3R',
                                             'B7Y', 'A7R', 'B9Y', 'B2R', 'A5Y', 'A7Y', 'B3R', 'A10Y', 'B1R', 'A10Y',
                                             'B4Y', 'A11Y', 'A10R']), (7, 6))
        self.assertEqual(men_still_standing(['A10R']), (10, 11))
        self.assertEqual(men_still_standing(['A6Y', 'B2R', 'B8Y', 'A3R', 'A5Y', 'B6Y', 'B3Y', 'B6Y', 'A4Y', 'B9Y',
                                             'A9Y', 'A6Y']), (9, 9))
        self.assertEqual(men_still_standing(['A5Y', 'B4R', 'A7Y', 'A4Y', 'B11Y', 'B8Y', 'A11Y', 'A5R', 'A3Y', 'A8Y',
                                             'B6Y', 'B5Y', 'A10R', 'A1R', 'B6R', 'A2R', 'B2R', 'B8R', 'B2R', 'A5Y',
                                             'A8Y', 'A9R', 'B8Y', 'B5Y']), (6, 7))
        self.assertEqual(men_still_standing(['B7Y', 'B8Y', 'B11R', 'B4R', 'B8Y', 'A11Y', 'B10Y', 'B2Y', 'B1Y', 'B3Y',
                                             'B6R', 'A8R', 'B5Y', 'A6Y', 'B11Y', 'B2Y', 'A3R', 'A5Y', 'A10Y']), (10, 6))
        self.assertEqual(men_still_standing(['B10Y', 'A7Y', 'A8Y', 'B5R', 'A2R', 'A2R', 'B1Y', 'A8R', 'A5Y', 'A9Y',
                                             'B4Y', 'B5Y', 'A4Y']), (9, 10))
        self.assertEqual(men_still_standing(['A5Y', 'B7Y', 'B8Y', 'B3R', 'A7R', 'B8Y', 'B7Y', 'B6Y', 'B1R', 'A5R',
                                             'B4Y', 'B3Y', 'B1Y', 'B11R']), (9, 6))
        self.assertEqual(men_still_standing(['A3Y', 'A3Y', 'A6Y', 'B11R', 'B3Y', 'A4Y', 'B3Y', 'B8Y', 'B9R', 'A10Y',
                                             'A6Y', 'A8R', 'B4Y', 'A11Y']), (8, 8))
        self.assertEqual(men_still_standing(['B5R', 'B6Y', 'A2R', 'B7Y', 'A7Y', 'A4Y', 'A4R', 'B9Y', 'A6Y', 'A5Y',
                                             'B4Y', 'A10R', 'B9Y', 'B9Y', 'B7R', 'A9R', 'A10Y']), (7, 8))
        self.assertEqual(men_still_standing(['A2Y', 'B6Y', 'B5R', 'B9R', 'B6Y', 'B9Y', 'B2Y', 'B2R', 'A7R', 'B5R',
                                             'A2Y', 'A3R', 'A6Y', 'B4Y', 'A4Y', 'B5Y', 'A4R', 'B2Y', 'B3R']), (7, 6))
        self.assertEqual(men_still_standing(['B7R', 'A8R', 'A3Y', 'B8Y', 'A3R', 'A8R', 'B6Y', 'B11R', 'B3Y', 'A2Y',
                                             'A9R']), (8, 9))
        self.assertEqual(men_still_standing(['A3Y', 'B6Y', 'A5Y', 'A3R', 'A11Y', 'B10Y', 'B6Y', 'A9Y', 'B1R', 'A7Y',
                                             'A11Y', 'A8Y', 'B6Y', 'A7Y', 'B10Y', 'A4Y', 'B9R', 'B4Y', 'A4Y', 'B10Y',
                                             'B11R', 'A3Y']), (7, 6))
        self.assertEqual(men_still_standing(['A5Y', 'B2Y', 'B5R', 'B5R', 'A4R', 'B3Y', 'B4Y', 'A3Y', 'B4Y', 'B5R',
                                             'B2Y', 'B2R', 'B1Y', 'B9Y', 'A8R', 'A4Y', 'A2R']), (8, 8))
        self.assertEqual(men_still_standing(['B1Y', 'B1Y']), (11, 10))
        self.assertEqual(men_still_standing(['A1R', 'B11Y', 'A8Y', 'B6Y', 'B8Y', 'A11R', 'A2Y', 'B3R', 'B2Y', 'A9Y',
                                             'B2R', 'A9Y']), (8, 9))
        self.assertEqual(men_still_standing(['A9Y', 'A3Y', 'A6Y', 'B6Y', 'A8Y', 'B4Y', 'A7Y', 'A2Y', 'A4R', 'B9Y',
                                             'B6Y', 'B6R', 'A10R']), (9, 10))
        self.assertEqual(men_still_standing(['B9Y', 'B4R', 'B3Y', 'A8Y', 'B6Y']), (11, 10))
        self.assertEqual(men_still_standing(['B6R', 'B2Y', 'A5Y', 'B11Y', 'B7Y', 'A5Y', 'A3R', 'B10Y', 'B2Y',
                                             'A4R']), (8, 9))
        self.assertEqual(men_still_standing(['A7Y', 'B2Y', 'A6R', 'B5R', 'B5Y', 'B3R', 'B4Y', 'B11Y', 'A6Y', 'A9Y',
                                             'B5R', 'A10Y', 'B1Y', 'A3Y', 'A11Y', 'A6Y', 'A9R']), (9, 9))
        self.assertEqual(men_still_standing(['A10Y', 'A1Y', 'B8Y', 'A9Y', 'A4Y', 'B4Y', 'B2Y', 'A2Y',
                                             'B7R']), (11, 10))
        self.assertEqual(men_still_standing(['A7Y', 'B6Y', 'A1R', 'B8Y', 'B7R', 'B11Y', 'B2Y', 'A7R', 'A11Y', 'B3Y',
                                             'B9Y', 'A5Y', 'B11Y', 'B3Y', 'B8Y', 'A2Y', 'A4Y', 'A6R', 'A4Y', 'A7Y',
                                             'A2Y', 'A11Y', 'B3R', 'B1Y', 'A11Y']), (6, 7))
        self.assertEqual(men_still_standing(['B5Y', 'A6Y', 'B5R', 'B9R', 'A7R', 'A7Y', 'B6Y', 'A1R', 'B9Y', 'A8Y',
                                             'A5Y', 'B9Y', 'B6R', 'A11Y', 'A8Y', 'B2R', 'B6Y', 'A5Y', 'A10R', 'A11R',
                                             'B4Y', 'B4Y', 'A4Y']), (6, 7))
        self.assertEqual(men_still_standing(['B7R', 'A5Y', 'B10R', 'A2Y', 'B3R', 'A2Y', 'B6Y', 'B5R', 'B4R', 'B7Y',
                                             'B10R', 'A2R', 'A4R', 'B8Y', 'B8Y', 'B10Y', 'A10R']), (10, 6))
        self.assertEqual(men_still_standing(['B2Y', 'A8Y', 'B7Y', 'B8Y', 'A11Y', 'B10R', 'B2Y', 'B11Y', 'A4R', 'B3Y',
                                             'B1Y', 'B5R', 'B5Y', 'B3Y', 'B1Y']), (10, 6))
        self.assertEqual(men_still_standing(['B11R', 'A6R', 'A10Y', 'A3Y', 'A5R', 'A2Y', 'A10Y', 'B6Y', 'A11R', 'A9Y',
                                             'A7Y', 'A2R', 'A3Y', 'B10Y']), (6, 10))
        self.assertEqual(men_still_standing(['A1R', 'A7Y', 'A9Y', 'A2Y', 'B9Y', 'B1Y', 'A3R', 'A8Y']), (9, 11))
        self.assertEqual(men_still_standing(['A5Y', 'A3Y', 'A5R', 'B3Y', 'A1Y', 'B9Y', 'A1R', 'B5Y']), (9, 11))
        self.assertEqual(men_still_standing(['A4Y', 'B6R', 'A5R', 'A7Y', 'B7Y', 'B8Y', 'A9Y', 'B9Y', 'B1Y', 'B6Y',
                                             'B2Y']), (10, 10))
        self.assertEqual(men_still_standing(['A2Y', 'A10Y', 'A5Y', 'A2Y', 'B1Y', 'B4Y', 'B2Y', 'A10Y']), (9, 11))
        self.assertEqual(men_still_standing(['B2Y', 'A4Y', 'A2R', 'A6Y', 'A2Y', 'A10R', 'A8Y', 'A6Y', 'A10R', 'A10R',
                                             'B2Y', 'B2R', 'B10R', 'A3Y', 'A5Y', 'A1R', 'B5Y', 'B8R', 'A7Y', 'A2R',
                                             'B1Y']), (7, 8))
        self.assertEqual(men_still_standing(['A2R', 'B11Y', 'A9R', 'A9Y', 'A6Y', 'B4R', 'B3R', 'A7Y', 'B8Y', 'A4Y',
                                             'A6R', 'B3Y']), (8, 9))
        self.assertEqual(men_still_standing(['B10Y', 'B1R', 'A1Y', 'A10R', 'B10Y', 'A6R', 'A4Y', 'A2R', 'B9Y', 'A1Y',
                                             'B5Y', 'A7R', 'A1R', 'A2Y', 'B7R', 'B4R', 'B6R', 'A7Y', 'A4R', 'A2Y',
                                             'B2Y', 'A7R', 'B5Y', 'B7Y']), (6, 9))
        self.assertEqual(men_still_standing(['B3R', 'A10Y', 'A3R', 'B7Y', 'B11Y', 'B1Y', 'B3Y', 'B10R', 'A1Y', 'B9Y',
                                             'A4Y', 'A2Y', 'B2R']), (10, 8))
        self.assertEqual(men_still_standing(['A9Y', 'A8R', 'A3Y', 'B4R', 'A9Y', 'A7Y', 'A2R', 'A2R', 'B9Y', 'B7Y',
                                             'A10Y', 'B2Y', 'B9Y', 'A4R', 'A4Y', 'A1Y', 'A10R', 'A11R', 'B3Y', 'B3Y',
                                             'A4Y', 'B6Y']), (6, 9))
        self.assertEqual(men_still_standing(['B8Y', 'B1Y', 'A9R', 'A6Y', 'B2Y']), (10, 11))
        self.assertEqual(men_still_standing(['A6R', 'A4R', 'B11Y', 'A10R', 'B6Y', 'B6Y', 'A5Y', 'B10R', 'A1Y', 'A4Y',
                                             'A5Y', 'B2Y', 'B5Y', 'B4Y', 'B11Y', 'B11R', 'B6R', 'A6R', 'A9R', 'B11Y',
                                             'A9Y', 'A10Y', 'B8Y', 'A6Y']), (6, 8))
        self.assertEqual(men_still_standing(['A4R', 'A9Y', 'B3R', 'B5Y', 'A10R', 'B10Y', 'B6Y', 'A11Y', 'A7Y', 'B9R',
                                             'B3Y']), (9, 9))
        self.assertEqual(men_still_standing(['B9Y', 'B7Y', 'A4Y', 'A1Y', 'B8Y', 'A2R', 'B11Y', 'A1R', 'B11Y', 'A7Y',
                                             'A6R']), (8, 10))
        self.assertEqual(men_still_standing(['A11Y', 'B10Y', 'B7Y', 'A8R', 'B8R', 'A2Y', 'B7R', 'A9Y', 'B3R', 'A8Y',
                                             'B9R', 'B8Y', 'A6Y', 'A9Y', 'B9Y', 'A2Y', 'B6Y', 'A1Y', 'A8Y', 'B11R',
                                             'A5R', 'A11Y', 'A11Y', 'B8Y']), (8, 6))
        self.assertEqual(men_still_standing(['A2Y', 'A2Y', 'B5Y', 'A11Y', 'B9Y', 'A6Y', 'B8R', 'B10R', 'B9R', 'A2Y',
                                             'A10Y', 'A4Y', 'B10Y', 'B1Y', 'B3R']), (10, 7))
        self.assertEqual(men_still_standing(['A10R', 'B10Y', 'A3R', 'A9R', 'A2Y', 'B10Y', 'B8Y', 'B2R', 'A3R',
                                             'B7Y']), (8, 9))
        self.assertEqual(men_still_standing(['B9Y', 'B5Y', 'A8Y']), (11, 11))
        self.assertEqual(men_still_standing(['B10R', 'A10R', 'B7Y', 'B11Y', 'B11Y', 'B1R', 'A7Y', 'A6R']), (9, 8))
        self.assertEqual(men_still_standing(['B11Y', 'A6R', 'B11Y', 'A9R', 'A2Y', 'B11R', 'B11Y', 'B8R', 'B9Y',
                                             'B10Y', 'A6Y']), (9, 9))
        self.assertEqual(men_still_standing(['B10Y', 'A3R', 'B8R', 'B10Y', 'A6Y', 'A2R', 'A11R', 'B7R', 'B3Y', 'A7R',
                                             'B4Y', 'A5R', 'B8Y', 'A9Y', 'A11Y', 'A10Y', 'A6Y', 'A4R', 'A9R', 'B10R',
                                             'B3Y']), (6, 8))
        self.assertEqual(men_still_standing(['A1R', 'B7Y', 'A5Y', 'B10Y', 'A1Y', 'A7Y', 'B11Y', 'A3Y', 'B11Y', 'B1R',
                                             'A11R', 'B11Y', 'A10Y', 'A10Y', 'B4Y', 'B4R', 'A9R']), (7, 8))
        self.assertEqual(men_still_standing(['A9R', 'A11R', 'B5Y', 'A5Y']), (9, 11))
        self.assertEqual(men_still_standing(['A5Y', 'A3Y', 'B5Y', 'B5Y', 'A7Y', 'B7Y', 'A2R', 'A1Y', 'B2Y', 'B11Y',
                                             'A5R']), (9, 10))
        self.assertEqual(men_still_standing(['B7Y', 'A10Y', 'A4R', 'A7R', 'B1R', 'A5R', 'B5Y', 'A11Y', 'A10R', 'A11Y',
                                             'B3Y']), (6, 10))
        self.assertEqual(men_still_standing(['B8Y', 'B11Y', 'A9R', 'A5Y', 'B7R', 'A5Y', 'A10Y']), (9, 10))
        self.assertEqual(men_still_standing(['A9R', 'B9Y', 'A10Y', 'B8Y', 'A10Y', 'A10Y', 'A6Y', 'B2Y']), (9, 11))


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
