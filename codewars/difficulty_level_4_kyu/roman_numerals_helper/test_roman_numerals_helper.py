
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_roman_numerals_helper import RomanNumerals


class TestSolution(unittest.TestCase):

    def test_to_roman(self):
        self.assertEqual(RomanNumerals.to_roman(1000), 'M')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')
        self.assertEqual(RomanNumerals.to_roman(4), 'IV')
        self.assertEqual(RomanNumerals.to_roman(1), 'I')
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII')

    def test_from_roman(self):
        self.assertEqual(RomanNumerals.from_roman('XXI'), 21)
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008)
        self.assertEqual(RomanNumerals.from_roman('I'), 1)
        self.assertEqual(RomanNumerals.from_roman('IV'), 4)
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
