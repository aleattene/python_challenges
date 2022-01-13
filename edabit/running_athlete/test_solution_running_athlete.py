
import unittest
from solution_running_athlete import running_athlete


class RunningAthlete(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(running_athlete(["run", "jump", "run", "jump", "run"], "_|_|_"), "_|_|_")
        self.assertEqual(running_athlete(["run", "jump", "run", "run", "run"], "_|_|_"), "_|_/_")
        self.assertEqual(running_athlete(["run", "run", "run", "run", "run"], "_|_|_"), "_/_/_")
        self.assertEqual(running_athlete(["jump", "jump", "jump", "jump", "jump"], "_|_|_"), "x|x|x")
        self.assertEqual(running_athlete(["jump", "run", "jump", "run", "jump"], "_|_|_"), "x/x/x")
        self.assertEqual(
            running_athlete(["run", "run", "run", "run", "run", "run", "run", "run", "run", "run"], "||||||||||"),
            "//////////")
        self.assertEqual(
            running_athlete(["jump", "jump", "jump", "jump", "jump", "jump", "jump", "jump", "jump", "jump"],
                            "__________"), "xxxxxxxxxx")


if __name__ == '__main__':
    unittest.main()
