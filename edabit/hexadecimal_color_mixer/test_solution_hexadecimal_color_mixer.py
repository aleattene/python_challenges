import unittest
from solution_hexadecimal_color_mixer import hex_color_mixer


class HexadecimalColor(unittest.TestCase):
    def test_hex_color_mixer(self):
        self.assertEqual(hex_color_mixer(["#FFFF00", "#FF0000"]), "#FF8000")
        self.assertEqual(hex_color_mixer(["#FFFF00", "#0000FF"]), "#808080")
        self.assertEqual(hex_color_mixer(["#B60E73", "#0EAEB6"]), "#625E95")
        self.assertEqual(hex_color_mixer(["#FF0000", "#00FF00", "#0000FF"]), "#555555")
        self.assertEqual(hex_color_mixer(["#99CC00", "#663399", "#1A8191"]), "#5E8063")
        self.assertEqual(hex_color_mixer(["#918381", "#D53B21", "#A54C83", "#DEFACF"]), "#BA817D")
        self.assertEqual(hex_color_mixer(["#140A23", "#46B31E", "#CFDF08", "#263534", "#EAD1FB", "#235E02"]), "#65803F")
        self.assertEqual(hex_color_mixer(["#FFFFFF", "#000000", "#000000", "#FFFFFF"]), "#808080")
        self.assertEqual(hex_color_mixer(["#CCCCCC"]), "#CCCCCC")


if __name__ == '__main__':
    unittest.main()
