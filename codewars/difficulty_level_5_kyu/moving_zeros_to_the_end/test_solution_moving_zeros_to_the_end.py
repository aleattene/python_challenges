
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_moving_zeros_to_the_end import move_zeros


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(move_zeros([]), [])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                         [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_advanced_cases(self):
        self.assertEqual(move_zeros([3, 6, 1, 8, 7, 2, 4]), [3, 6, 1, 8, 7, 2, 4])
        self.assertEqual(move_zeros([8, 0, 0, 0, 0, 0]), [8, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 0, 0, 0, 2, 0, 0]), [2, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([4, 7, 5, 8, 9, 7, 6, 8, 4]), [4, 7, 5, 8, 9, 7, 6, 8, 4])
        self.assertEqual(move_zeros([0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([7, 7, 1, 5, 4]), [7, 7, 1, 5, 4])
        self.assertEqual(move_zeros([4, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0]), [4, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 4, 4, 0, 0, 0, 0, 0]), [4, 4, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([2, 6, 0, 0, 9, 0, 0, 0, 0, 0, 9]), [2, 6, 9, 9, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 8, 5, 0, 0, 0, 0, 0, 1, 0, 0]), [8, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 0, 0, 5, 0, 0]), [5, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 2, 4, 2, 8, 0, 0, 0, 0, 0]), [2, 4, 2, 8, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 3, 0, 9, 0, 0, 9, 0, 0, 8, 0, 0]), [3, 9, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([6, 4, 4, 3, 9, 1, 4]), [6, 4, 4, 3, 9, 1, 4])
        self.assertEqual(move_zeros([5, 7, 0, 0, 0, 0, 0, 2, 0, 0]), [5, 7, 2, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 5, 0, 0, 0, 0, 8, 0]), [5, 8, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([8, 2, 4, 4, 3, 5, 9, 1, 7]), [8, 2, 4, 4, 3, 5, 9, 1, 7])
        self.assertEqual(move_zeros([6, 7, 4, 7, 6, 9, 5, 7]), [6, 7, 4, 7, 6, 9, 5, 7])
        self.assertEqual(move_zeros([0, 0, 0, 2, 0, 0, 0]), [2, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0]), [9, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([6, 0, 3, 0, 3, 0, 0, 0]), [6, 3, 3, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 9, 5, 0, 0, 0, 6]), [9, 5, 6, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 5, 0, 0, 3]), [5, 3, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 1, 0, 0, 9, 3, 3, 0, 0]), [1, 9, 3, 3, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([9, 7, 3, 2, 8, 3, 2, 7]), [9, 7, 3, 2, 8, 3, 2, 7])
        self.assertEqual(move_zeros([0, 0, 4, 0, 0, 0, 0, 0, 5]), [4, 5, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 4, 0, 6, 7, 3, 0, 0, 0, 0, 0]), [4, 6, 7, 3, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([6, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [6, 0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
