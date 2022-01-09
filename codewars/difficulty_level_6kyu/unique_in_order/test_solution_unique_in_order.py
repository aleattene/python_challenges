
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_unique_in_order import unique_in_order


class TestSolution(unittest.TestCase):

    def test_string(self):
        # ONE ELEMENT
        self.assertEqual(unique_in_order("A"), ['A'])
        # REDUCE DUPLICATES
        self.assertEqual(unique_in_order("AA"), ['A'])
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order("AADD"), ['A', 'D'])
        self.assertEqual(unique_in_order("AAD"), ['A', 'D'])
        self.assertEqual(unique_in_order("ADD"), ['A', 'D'])
        # LOWERCASE AS DIFFERENT FROM UPPERCASE
        self.assertEqual(unique_in_order("ABBCcAD"), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_lists(self):
        # EMPTY LIST
        self.assertEqual(unique_in_order([]), [])
        # SOME LISTS
        self.assertEqual(unique_in_order([1, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(unique_in_order([1, 1, 2, 2, 3, 3, 1, 1 ]), [1, 2, 3, 1])
        self.assertEqual(unique_in_order(['A', 'B', 'C', 'c', 'A', 'D']), ['A', 'B', 'C', 'c', 'A', 'D'])
        self.assertEqual(unique_in_order(['a', 'b', 'b']), ['a', 'b'])


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
