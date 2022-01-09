
import unittest
from solution_sum_of_missing_numbers import sum_missing_numbers


class SumMissingNumbers(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(sum_missing_numbers([1, 3, 5, 7, 10]), 29)
        self.assertEqual(sum_missing_numbers([10, 20, 30, 40, 50, 60]), 1575)
        self.assertEqual(sum_missing_numbers([7, 3, 8, 5, 12]), 40)
        self.assertEqual(sum_missing_numbers([99, 2, 45, 4, 17]), 4782)
        self.assertEqual(sum_missing_numbers([10, 7, 5, 3, 1]), 29)
        self.assertEqual(sum_missing_numbers([7, 8, 9, 10]), 0)


if __name__ == '__main__':
    unittest.main()
