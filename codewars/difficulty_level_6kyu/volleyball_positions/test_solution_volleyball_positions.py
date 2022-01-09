
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_volleyball_positions import volleyball_positions


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        final_formation = [
            ["empty", "Player5", "empty"],
            ["Player4", "empty", "Player2"],
            ["empty", "Player3", "empty"],
            ["Player6", "empty", "Player1"]
        ]
        team_rotations = 2
        initial_formation = [
            ["empty", "Player1", "empty"],
            ["Player2", "empty", "Player3"],
            ["empty", "Player4", "empty"],
            ["Player5", "empty", "Player6"]
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"]
        ]
        team_rotations = 6
        initial_formation = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"]
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ["empty", "player 3", "empty"],
            ["player 3", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"]
        ]
        team_rotations = 1000000
        initial_formation = [
            ["empty", "5", "empty"],
            ["4", "empty", "player 3"],
            ["empty", "player", "empty"],
            ["42", "empty", "player 3"]
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ["empty", "player 3", "empty"],
            ["player 8", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"]
        ]
        team_rotations = 0
        initial_formation = [
            ["empty", "player 3", "empty"],
            ["player 8", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"]
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ["empty", "player 3", "empty"],
            ["player 8", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"]
        ]
        team_rotations = 1000000000
        initial_formation = [
            ["empty", "5", "empty"],
            ["4", "empty", "player 8"],
            ["empty", "player", "empty"],
            ["42", "empty", "player 3"]
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)

    def test_advanced_cases(self):
        final_formation = [
            ['empty', 'xh', 'empty'],
            ['bqgid', 'empty', 'gzmzr'],
            ['empty', 'kere', 'empty'],
            ['nhts', 'empty', 'echxb']
        ]
        team_rotations = 33488548
        initial_formation = [
            ['empty', 'nhts', 'empty'],
            ['kere', 'empty', 'bqgid'],
            ['empty', 'gzmzr', 'empty'],
            ['echxb', 'empty', 'xh']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'oqg', 'empty'],
            ['qnwgiu', 'empty', 'srcm'], ['empty', 'yzzluw', 'empty'],
            ['iizhrqb', 'empty', 'usss']
        ]
        team_rotations = 15441245
        initial_formation = [
            ['empty', 'qnwgiu', 'empty'],
            ['iizhrqb', 'empty', 'oqg'],
            ['empty', 'usss', 'empty'],
            ['yzzluw', 'empty', 'srcm']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'dbsmcn', 'empty'],
            ['kaavln', 'empty', 'rnwt'],
            ['empty', 'dnt', 'empty'],
            ['zulizll', 'empty', 'xz']
        ]
        team_rotations = 45651658
        initial_formation = [
            ['empty', 'zulizll', 'empty'],
            ['dnt', 'empty', 'kaavln'],
            ['empty', 'rnwt', 'empty'],
            ['xz', 'empty', 'dbsmcn']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'lf', 'empty'],
            ['cvrs', 'empty', 'xugqvr'],
            ['empty', 'fioxdav', 'empty'],
            ['supft', 'empty', 'dgj']
        ]
        team_rotations = 11241765
        initial_formation = [
            ['empty', 'fioxdav', 'empty'],
            ['dgj', 'empty', 'supft'],
            ['empty', 'lf', 'empty'],
            ['xugqvr', 'empty', 'cvrs']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)

        final_formation = [
            ['empty', 'dqt', 'empty'],
            ['rwwzia', 'empty', 'odlji'],
            ['empty', 'ggufcea', 'empty'],
            ['vtbgv', 'empty', 'bil']
        ]
        team_rotations = 99546635
        initial_formation = [
            ['empty', 'rwwzia', 'empty'],
            ['vtbgv', 'empty', 'dqt'],
            ['empty', 'bil', 'empty'],
            ['ggufcea', 'empty', 'odlji']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'blgdxu', 'empty'],
            ['yjec', 'empty', 'tmtdw'],
            ['empty', 'swic', 'empty'],
            ['nxj', 'empty', 'rlgu']
        ]
        team_rotations = 17307586
        initial_formation = [
            ['empty', 'nxj', 'empty'],
            ['swic', 'empty', 'yjec'],
            ['empty', 'tmtdw', 'empty'],
            ['rlgu', 'empty', 'blgdxu']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'varpek', 'empty'],
            ['vq', 'empty', 'qfw'],
            ['empty', 'pmhtnq', 'empty'],
            ['ifb', 'empty', 'exji']
        ]
        team_rotations = 31998691
        initial_formation = [
            ['empty', 'qfw', 'empty'],
            ['varpek', 'empty', 'exji'],
            ['empty', 'ifb', 'empty'],
            ['vq', 'empty', 'pmhtnq']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'ebrnsgg', 'empty'],
            ['emld', 'empty', 'yi'],
            ['empty', 'at', 'empty'],
            ['rkbtk', 'empty', 'yisdir']
        ]
        team_rotations = 85778536
        initial_formation = [
            ['empty', 'rkbtk', 'empty'],
            ['at', 'empty', 'emld'],
            ['empty', 'yi', 'empty'],
            ['yisdir', 'empty', 'ebrnsgg']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'tcqa', 'empty'],
            ['xqchidy', 'empty', 'vihlx'],
            ['empty', 'rbtc', 'empty'],
            ['ve', 'empty', 'aekpoww']
        ]
        team_rotations = 78235735
        initial_formation = [
            ['empty', 'vihlx', 'empty'],
            ['tcqa', 'empty', 'aekpoww'],
            ['empty', 've', 'empty'],
            ['xqchidy', 'empty', 'rbtc']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'bbwaabx', 'empty'],
            ['cee', 'empty', 'kvouwbs'],
            ['empty', 'miwj', 'empty'],
            ['ory', 'empty', 'meo']
        ]
        team_rotations = 78650347
        initial_formation = [
            ['empty', 'kvouwbs', 'empty'],
            ['bbwaabx', 'empty', 'meo'],
            ['empty', 'ory', 'empty'],
            ['cee', 'empty', 'miwj']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'yj', 'empty'],
            ['noyp', 'empty', 'xbprxta'],
            ['empty', 'jlk', 'empty'],
            ['fniocdk', 'empty', 'ixb']
        ]
        team_rotations = 59717877
        initial_formation = [
            ['empty', 'jlk', 'empty'],
            ['ixb', 'empty', 'fniocdk'],
            ['empty', 'yj', 'empty'],
            ['xbprxta', 'empty', 'noyp']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'wt', 'empty'],
            ['nqjewm', 'empty', 'svecabv'],
            ['empty', 'nqsg', 'empty'],
            ['kgd', 'empty', 'ayoyhof']
        ]
        team_rotations = 16590213
        initial_formation = [
            ['empty', 'nqsg', 'empty'],
            ['ayoyhof', 'empty', 'kgd'],
            ['empty', 'wt', 'empty'],
            ['svecabv', 'empty', 'nqjewm']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'po', 'empty'],
            ['ev', 'empty', 'jf'],
            ['empty', 'dpxs', 'empty'],
            ['owt', 'empty', 'hwmix']
        ]
        team_rotations = 23568850
        initial_formation = [
            ['empty', 'owt', 'empty'],
            ['dpxs', 'empty', 'ev'],
            ['empty', 'jf', 'empty'],
            ['hwmix', 'empty', 'po']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'hzjpny', 'empty'],
            ['om', 'empty', 'bwvzkq'],
            ['empty', 'swhv', 'empty'],
            ['nucx', 'empty', 'kgtwe']
        ]
        team_rotations = 13140823
        initial_formation = [
            ['empty', 'bwvzkq', 'empty'],
            ['hzjpny', 'empty', 'kgtwe'],
            ['empty', 'nucx', 'empty'],
            ['om', 'empty', 'swhv']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'aueoywk', 'empty'],
            ['cl', 'empty', 'pgpsqh'],
            ['empty', 'pht', 'empty'],
            ['lw', 'empty', 'njosrto']
        ]
        team_rotations = 84832643
        initial_formation = [
            ['empty', 'cl', 'empty'],
            ['lw', 'empty', 'aueoywk'],
            ['empty', 'njosrto', 'empty'],
            ['pht', 'empty', 'pgpsqh']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'gwnemdq', 'empty'],
            ['czpmfx', 'empty', 'bottava'],
            ['empty', 'wrktnd', 'empty'],
            ['bqcchf', 'empty', 'ig']
        ]
        team_rotations = 50822461
        initial_formation = [
            ['empty', 'bottava', 'empty'],
            ['gwnemdq', 'empty', 'ig'],
            ['empty', 'bqcchf', 'empty'],
            ['czpmfx', 'empty', 'wrktnd']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'vzxfiak', 'empty'],
            ['wus', 'empty', 'zhnrcmx'],
            ['empty', 'scuu', 'empty'],
            ['jvsdk', 'empty', 'mws']
        ]
        team_rotations = 82607366
        initial_formation = [
            ['empty', 'mws', 'empty'],
            ['zhnrcmx', 'empty', 'scuu'],
            ['empty', 'wus', 'empty'],
            ['vzxfiak', 'empty', 'jvsdk']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'peztgbi', 'empty'],
            ['pikb', 'empty', 'cciiatn'],
            ['empty', 'fxl', 'empty'],
            ['qqvi', 'empty', 'qnf']
        ]
        team_rotations = 27648765
        initial_formation = [
            ['empty', 'fxl', 'empty'],
            ['qnf', 'empty', 'qqvi'],
            ['empty', 'peztgbi', 'empty'],
            ['cciiatn', 'empty', 'pikb']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'ibkjurc', 'empty'],
            ['mmnvd', 'empty', 'fmwrdb'],
            ['empty', 'wqfbmr', 'empty'],
            ['igamhzi', 'empty', 'hcyg']
        ]
        team_rotations = 63530066
        initial_formation = [
            ['empty', 'hcyg', 'empty'],
            ['fmwrdb', 'empty', 'wqfbmr'],
            ['empty', 'mmnvd', 'empty'],
            ['ibkjurc', 'empty', 'igamhzi']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'js', 'empty'],
            ['it', 'empty', 'lbgokz'],
            ['empty', 'nuxuy', 'empty'],
            ['iojdnz', 'empty', 'akkscul']
        ]
        team_rotations = 95488355
        initial_formation = [
            ['empty', 'it', 'empty'],
            ['iojdnz', 'empty', 'js'],
            ['empty', 'akkscul', 'empty'],
            ['nuxuy', 'empty', 'lbgokz']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'cax', 'empty'],
            ['jqpjapt', 'empty', 'zn'],
            ['empty', 'jkc', 'empty'],
            ['iu', 'empty', 'uocedb']
        ]
        team_rotations = 54313541
        initial_formation = [
            ['empty', 'jqpjapt', 'empty'],
            ['iu', 'empty', 'cax'],
            ['empty', 'uocedb', 'empty'],
            ['jkc', 'empty', 'zn']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)

        final_formation = [
            ['empty', 'zo', 'empty'],
            ['zidcgb', 'empty', 'tlivaxw'],
            ['empty', 'peo', 'empty'],
            ['xkion', 'empty', 'aco']
        ]
        team_rotations = 97806883
        initial_formation = [
            ['empty', 'tlivaxw', 'empty'],
            ['zo', 'empty', 'aco'],
            ['empty', 'xkion', 'empty'],
            ['zidcgb', 'empty', 'peo']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)

        final_formation = [
            ['empty', 'sgxjop', 'empty'],
            ['mntirs', 'empty', 'uatocs'],
            ['empty', 'beqnvt', 'empty'],
            ['fog', 'empty', 'gtos']
        ]
        team_rotations = 62345729
        initial_formation = [
            ['empty', 'mntirs', 'empty'],
            ['fog', 'empty', 'sgxjop'],
            ['empty', 'gtos', 'empty'],
            ['beqnvt', 'empty', 'uatocs']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)

        final_formation = [
            ['empty', 'suukpv', 'empty'],
            ['khu', 'empty', 'grh'],
            ['empty', 'ng', 'empty'],
            ['wne', 'empty', 'rs']
        ]
        team_rotations = 23975825
        initial_formation = [
            ['empty', 'khu', 'empty'],
            ['wne', 'empty', 'suukpv'],
            ['empty', 'rs', 'empty'],
            ['ng', 'empty', 'grh']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'xrjsx', 'empty'],
            ['wvgm', 'empty', 'etvzg'],
            ['empty', 'vymjxeq', 'empty'],
            ['gjaoupr', 'empty', 'ckrov']
        ]
        team_rotations = 57276830
        initial_formation = [
            ['empty', 'ckrov', 'empty'],
            ['etvzg', 'empty', 'vymjxeq'],
            ['empty', 'wvgm', 'empty'],
            ['xrjsx', 'empty', 'gjaoupr']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'lrhxh', 'empty'],
            ['xxp', 'empty', 'rofx'],
            ['empty', 'uy', 'empty'],
            ['oqkxf', 'empty', 'ubzzkv']
        ]
        team_rotations = 63757723
        initial_formation = [
            ['empty', 'rofx', 'empty'],
            ['lrhxh', 'empty', 'ubzzkv'],
            ['empty', 'oqkxf', 'empty'],
            ['xxp', 'empty', 'uy']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'fzlrba', 'empty'],
            ['cmjgz', 'empty', 'fnbqu'],
            ['empty', 'tsf', 'empty'],
            ['gyw', 'empty', 'seuwcd']
        ]
        team_rotations = 68088882
        initial_formation = [
            ['empty', 'fzlrba', 'empty'],
            ['cmjgz', 'empty', 'fnbqu'],
            ['empty', 'tsf', 'empty'],
            ['gyw', 'empty', 'seuwcd']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'og', 'empty'],
            ['augfu', 'empty', 'xnj'],
            ['empty', 'jadgbjy', 'empty'],
            ['oikc', 'empty', 'qrmanjz']
        ]
        team_rotations = 47655718
        initial_formation = [
            ['empty', 'oikc', 'empty'],
            ['jadgbjy', 'empty', 'augfu'],
            ['empty', 'xnj', 'empty'],
            ['qrmanjz', 'empty', 'og']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'kzbipwk', 'empty'],
            ['bygon', 'empty', 'xbelgi'],
            ['empty', 'jciw', 'empty'],
            ['foutmwv', 'empty', 'mfwfma']
        ]
        team_rotations = 31910892
        initial_formation = [
            ['empty', 'kzbipwk', 'empty'],
            ['bygon', 'empty', 'xbelgi'],
            ['empty', 'jciw', 'empty'],
            ['foutmwv', 'empty', 'mfwfma']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'aigw', 'empty'],
            ['jy', 'empty', 'ys'],
            ['empty', 'nwvfefa', 'empty'],
            ['apdkwky', 'empty', 'fjt']
        ]
        team_rotations = 36415470
        initial_formation = [
            ['empty', 'aigw', 'empty'],
            ['jy', 'empty', 'ys'],
            ['empty', 'nwvfefa', 'empty'],
            ['apdkwky', 'empty', 'fjt']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)
        final_formation = [
            ['empty', 'kppcf', 'empty'],
            ['wyfmgyy', 'empty', 'gp'],
            ['empty', 'sgwraeg', 'empty'],
            ['fwldhc', 'empty', 'xgbouq']
        ]
        team_rotations = 8421477
        initial_formation = [
            ['empty', 'sgwraeg', 'empty'],
            ['xgbouq', 'empty', 'fwldhc'],
            ['empty', 'kppcf', 'empty'],
            ['gp', 'empty', 'wyfmgyy']
        ]
        self.assertEqual(volleyball_positions(final_formation, team_rotations), initial_formation)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
