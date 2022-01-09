
import unittest
from solution_ping_pong import ping_pong


class PingPong(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(ping_pong(["Ping!", "Ping!", "Ping!"], True),
                         ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"])
        self.assertEqual(ping_pong(["Ping!", "Ping!"], False), ["Ping!", "Pong!", "Ping!"])
        self.assertEqual(ping_pong(["Ping!"], True), ["Ping!", "Pong!"])


if __name__ == '__main__':
    unittest.main()
