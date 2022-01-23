import unittest
from solution_alphabet_clash_battle_ascii_values import alphabet_clash


class AlphabetClash(unittest.TestCase):
    def test_alphabet_clash(self):
        self.assertEqual(alphabet_clash(
            "MZNHUVIOEPTWFJCBXKALSDQGYR",
            [1, 3, 2, 8, 10, 12, 9, 7, 4, 22],
            "YFTUCSQOMGKPXNDWHIVJRABZEL",
            [21, 24, 25, 3, 4, 1, 8, 9, 10, 17]
        ),
            {'A': 64, 'Z': 96}
        )

        self.assertEqual(alphabet_clash(
            "OZLICHFRKYBVUDSPWXJNGTQAEM",
            [8, 6, 4, 2, 0, 10, 12, 14, 16, 18],
            "WKJVUNXHRFDIOBTCSLZMPYGQAE",
            [7, 5, 3, 1, 9, 11, 13, 15, 17, 19]
        ),
            {'A': 77, 'Z': 63}
        )

        self.assertEqual(alphabet_clash(
            "IBXOWMUSGYPADJCLVKETQRZHFN",
            [23, 19, 21, 22, 2, 4, 6, 1, 0, 12],
            "TOLFIYHGKWAXRBDQMVNJSPCUZE",
            [15, 8, 2, 1, 0, 25, 12, 13, 16, 14]
        ),
            {'A': 75, 'Z': 50}
        )

        self.assertEqual(alphabet_clash(
            "IBXOWMUSGYPADJCLVKETQRZHFN",
            [15, 8, 2, 1, 0, 25, 12, 13, 16, 14],
            "IBXOWMUSGYPADJCLVKETQRZHFN",
            [15, 8, 2, 1, 0, 25, 12, 13, 16, 14]
        ),
            {'A': 0, 'Z': 0}
        )


if __name__ == '__main__':
    unittest.main()
