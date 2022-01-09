
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_check_the_exam import check_exam


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
        self.assertEqual(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]), 7)
        self.assertEqual(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
        self.assertEqual(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]), 0)
        self.assertEqual(check_exam(["c", "c", "a", "c"], ["", "", "c", ""]), 0)
        self.assertEqual(check_exam(["a", "b", "c", "b", "c", "a"], ["b", "c", "c", "a", "b", ""]), 0)
        self.assertEqual(check_exam(["a", "c", "c", "c", "b", "b"], ["c", "", "", "", "b", "a"]), 2)
        self.assertEqual(check_exam(["c", "a", "b", "a", "b", "a", "b"], ["b", "b", "a", "b", "c", "b", "a"]), 0)
        self.assertEqual(check_exam(["b", "a", "b", "c"], ["", "b", "a", ""]), 0)
        self.assertEqual(check_exam(["a", "c", "a", "c", "a", "a", "b"], ["c", "a", "a", "b", "b", "", ""]), 0)
        self.assertEqual(check_exam(["a", "b", "c", "a", "c", "a", "a"], ["a", "b", "c", "", "b", "a", "b"]), 14)
        self.assertEqual(check_exam(["a", "c", "c", "b", "c", "a", "a"], ["c", "a", "b", "c", "b", "c", ""]), 0)
        self.assertEqual(check_exam(["b", "b", "c", "b", "a"], ["", "", "b", "a", ""]), 0)

    def test_advanced_cases(self):
        self.assertEqual(check_exam(["a", "b", "b", "c", "a", "b", "a", "b", "c", "c"],
                                    ["b", "", "a", "", "b", "b", "a", "b", "a", "c"]), 12)
        self.assertEqual(check_exam(["c", "a", "a", "b", "c", "c", "c", "b"],
                                    ["c", "", "a", "b", "c", "a", "a", "b"]), 18)
        self.assertEqual(check_exam(["b", "c", "a", "b", "a", "c", "c", "a", "b", "c", "b", "c", "a", "b", "c"],
                                    ["", "a", "", "a", "", "", "", "b", "", "a", "", "", "c", "c", "a"]), 0)
        self.assertEqual(check_exam(
            ["b", "a", "b", "a", "c", "a", "c", "b", "c", "c", "b", "b", "c", "c", "c", "a", "b", "b"],
            ["", "a", "c", "b", "", "c", "c", "", "a", "c", "", "b", "c", "c", "c", "a", "b", "a"]), 31)
        self.assertEqual(check_exam(["a", "a", "b", "c", "c", "c", "b", "a", "a", "a", "c", "b", "a", "a", "c"],
                                    ["c", "b", "", "b", "b", "c", "b", "c", "", "a", "", "b", "a", "c", ""]), 14)
        self.assertEqual(check_exam(["b", "c", "b", "b", "a", "b", "c", "c", "c", "a", "a", "c", "b", "c"],
                                    ["b", "a", "", "a", "a", "", "a", "c", "c", "a", "", "b", "a", "c"]), 19)
        self.assertEqual(check_exam(["c", "b", "a", "c", "c", "a", "c", "c", "c"],
                                    ["a", "b", "a", "b", "b", "c", "b", "c", "b"]), 6)
        self.assertEqual(check_exam(["a", "c", "a", "c", "b", "b", "a", "c", "a", "b", "c", "a", "c", "a", "a", "c"],
                                    ["", "b", "a", "", "b", "c", "b", "", "a", "", "", "b", "b", "a", "a", "c"]), 19)
        self.assertEqual(check_exam(
            ["c", "b", "a", "a", "a", "b", "c", "a", "a", "c", "c", "c", "a", "b", "b", "a", "b", "b"],
            ["b", "", "b", "", "c", "c", "c", "b", "", "c", "", "c", "a", "b", "", "", "b", "a"]), 18)
        self.assertEqual(check_exam(["a", "c", "a", "b", "b", "b", "c", "c", "a"],
                                    ["c", "b", "", "b", "", "c", "b", "", "a"]), 4)
        self.assertEqual(check_exam(
            ["c", "a", "b", "a", "a", "c", "b", "b", "c", "a", "a", "a", "c", "c", "a", "b", "b", "c"],
            ["a", "", "a", "a", "", "b", "", "b", "a", "", "c", "b", "a", "", "", "a", "b", "b"]), 3)
        self.assertEqual(check_exam(
            ["a", "c", "c", "c", "a", "a", "c", "c", "a", "c", "b", "a", "c", "c", "c", "c", "b"],
            ["c", "a", "a", "c", "a", "", "a", "c", "b", "", "", "c", "a", "a", "a", "b", "a"]), 1)
        self.assertEqual(check_exam(["c", "a", "c", "a", "a", "b", "b", "c", "b", "b", "b", "b", "b", "c"],
                                    ["c", "a", "a", "a", "c", "", "a", "b", "b", "a", "a", "", "", ""]), 10)
        self.assertEqual(check_exam(
            ["c", "b", "a", "b", "b", "c", "b", "c", "b", "c", "c", "a", "c", "a", "b", "c", "a", "c"],
            ["a", "c", "", "a", "c", "b", "b", "a", "b", "", "a", "a", "c", "a", "a", "a", "", ""]), 11)
        self.assertEqual(check_exam(
            ["a", "a", "b", "a", "b", "c", "a", "a", "b", "b", "b", "b", "b", "b", "a", "c", "a"],
            ["", "a", "c", "", "", "a", "a", "b", "c", "", "b", "b", "a", "a", "", "", "a"]), 14)
        self.assertEqual(check_exam(
            ["c", "a", "a", "c", "a", "a", "c", "c", "b", "c", "a", "b", "c", "a", "b", "b", "c", "a"],
            ["", "b", "", "a", "b", "c", "c", "c", "", "", "b", "c", "a", "a", "b", "c", "b", ""]), 7)
        self.assertEqual(check_exam(
            ["c", "a", "b", "a", "b", "b", "c", "b", "a", "a", "c", "a", "c", "b"],
            ["", "c", "a", "a", "b", "c", "a", "", "a", "c", "b", "a", "", "b"]), 14)
        self.assertEqual(check_exam(["b", "a", "c", "a", "c", "a", "a", "a", "b", "a", "a", "b", "c", "b"],
                                    ["a", "b", "c", "", "", "b", "c", "a", "b", "c", "a", "b", "a", ""]), 14)
        self.assertEqual(check_exam(["a", "a", "a", "b", "a", "a", "b", "a", "a", "b"],
                                    ["b", "b", "a", "c", "", "b", "", "a", "a", ""]), 8)
        self.assertEqual(check_exam(["b", "a", "a", "a", "a", "a", "c", "b", "a", "c"],
                                    ["a", "c", "a", "b", "a", "", "b", "a", "c", "a"]), 1)
        self.assertEqual(check_exam(["a", "a", "b", "b", "a", "c", "a", "c", "a", "b", "a", "a", "b", "c"],
                                    ["a", "", "b", "a", "", "", "b", "c", "c", "", "", "", "b", ""]), 13)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
