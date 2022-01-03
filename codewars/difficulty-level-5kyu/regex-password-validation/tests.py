
""" To start the tests, type from CLI: python tests.py """

import unittest
from solution import check_password


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(check_password('fjd3IR9'), True)
        self.assertEqual(check_password('dsF43'), False)
        self.assertEqual(check_password('4fdg5Fj3'), True)
        self.assertEqual(check_password('DHSJdhjsU'), False)
        self.assertEqual(check_password('fjd3IR9.;'), False)
        self.assertEqual(check_password('fjd3  IR9'), False)
        self.assertEqual(check_password('djI38D55'), True)
        self.assertEqual(check_password('a2.d412'), False)
        self.assertEqual(check_password('JHD5FJ53'), False)
        self.assertEqual(check_password('!fdjn345'), False)
        self.assertEqual(check_password('jfkdfj3j'), False)
        self.assertEqual(check_password('123'), False)
        self.assertEqual(check_password('abc'), False)
        self.assertEqual(check_password('123abcABC'), True)
        self.assertEqual(check_password('ABC123abc'), True)
        self.assertEqual(check_password('Password123'), True)

    def test_advanced_cases(self):
        self.assertEqual(check_password('I8WHjL+fkL5F8-TYr'), False)
        self.assertEqual(check_password('fR7'), False)
        self.assertEqual(check_password('Rb9W'), False)
        self.assertEqual(check_password('wXf- JEG7TGz7e'), False)
        self.assertEqual(check_password('yX6'), False)
        self.assertEqual(check_password('z74Z'), False)
        self.assertEqual(check_password('Hvg9'), False)
        self.assertEqual(check_password('92p0vGaK'), True)
        self.assertEqual(check_password('k8X'), False)
        self.assertEqual(check_password('QeLA1c4V8C'), True)
        self.assertEqual(check_password('I5YPfQjWr4DPv4'), True)
        self.assertEqual(check_password('QKRY\\kR2Npz3W'), False)
        self.assertEqual(check_password('DZTKSX3rd+nd5h'), False)
        self.assertEqual(check_password('Q9yT57'), True)
        self.assertEqual(check_password('70znBBzG?4bKw'), False)
        self.assertEqual(check_password('qXljUox/vmLakjG9I'), False)
        self.assertEqual(check_password('MgUq!sV62'), False)
        self.assertEqual(check_password('linSB8kUg'), True)
        self.assertEqual(check_password('KS53APYRijQpE'), True)
        self.assertEqual(check_password('P2mX3Z'), True)
        self.assertEqual(check_password('em1M3q5a1IxJ_GB'), False)
        self.assertEqual(check_password('!wlSuVV85PpwXM8F'), False)
        self.assertEqual(check_password('nE6uTcDCB_X'), False)
        self.assertEqual(check_password('A0eF'), False)
        self.assertEqual(check_password('mGurO-3GaAco5NhIo+'), False)
        self.assertEqual(check_password('+A8lvD'), False)
        self.assertEqual(check_password('g9qtW7-tRtzMt0'), False)
        self.assertEqual(check_password('5Q3V8d2?Q76m6'), False)
        self.assertEqual(check_password('4I9e8a9Y'), True)
        self.assertEqual(check_password('glvm2ZKtHWhbG!/0b'), False)
        self.assertEqual(check_password('E!3\\x25'), False)
        self.assertEqual(check_password('D6S5su!xru'), False)
        self.assertEqual(check_password('FEp6'), False)
        self.assertEqual(check_password('W8nL'), False)
        self.assertEqual(check_password('uZBZa9/T Qk8Yc2'), False)
        self.assertEqual(check_password('l!3WAHxLjbRElxyn'), False)
        self.assertEqual(check_password('TKj1Ud03PJ'), True)
        self.assertEqual(check_password('+3Mktt7ubUx/6 '), False)
        self.assertEqual(check_password(' 95YMiyuXmJK!pI'), False)
        self.assertEqual(check_password('zKBjF0I4! 9g'), False)
        self.assertEqual(check_password('k0CGa'), False)
        self.assertEqual(check_password('a7xjBL08GOpF/xNG'), False)
        self.assertEqual(check_password('Hhc76k-7v9xv\\PIJJn'), False)
        self.assertEqual(check_password('oe!8yO4b0U'), False)
        self.assertEqual(check_password('zrdP1W83!'), False)
        self.assertEqual(check_password('vk9NFpdgOX'), True)
        self.assertEqual(check_password('S5?yBucq 1hBMUCf'), False)
        self.assertEqual(check_password('YQ5s8Moalq22Hyk'), True)
        self.assertEqual(check_password('mrzt0e36VzS5tU37'), True)
        self.assertEqual(check_password('4CqD0ke'), True)
        self.assertEqual(check_password('q4kMTdYS2g4eG_z'), False)
        self.assertEqual(check_password('jOJj96T1M'), True)
        self.assertEqual(check_password('Kifir5t'), True)
        self.assertEqual(check_password('2Yf'), False)
        self.assertEqual(check_password('HOzUrZCgok8tB2'), True)
        self.assertEqual(check_password('+kC4'), False)
        self.assertEqual(check_password('2f7ppKl0ozCyce'), True)
        self.assertEqual(check_password('1f8qJLeBl4'), True)
        self.assertEqual(check_password('Ij4K'), False)
        self.assertEqual(check_password('4uoVVS4p'), True)
        self.assertEqual(check_password('iGV40ijA'), True)
        self.assertEqual(check_password('ZytiX a6XK'), False)
        self.assertEqual(check_password('YETzpbaS5h'), True)
        self.assertEqual(check_password('AlzndP7TWZBP-0AlQ'), False)
        self.assertEqual(check_password('W8eG'), False)
        self.assertEqual(check_password('xF99CIG'), True)
        self.assertEqual(check_password('QUtsEwsy0ZN1a3k'), True)
        self.assertEqual(check_password('mz21q7mQGfGTbQdoM'), True)
        self.assertEqual(check_password('L9kO-RZo8S8!2L44'), False)
        self.assertEqual(check_password('4uaI4A'), True)
        self.assertEqual(check_password('d7HWO V3BnWoSp'), False)
        self.assertEqual(check_password('j8x+sl4OT'), False)
        self.assertEqual(check_password('7/o0-Ng1xy'), False)
        self.assertEqual(check_password('7TpgIeJGvMua'), True)
        self.assertEqual(check_password('6q+vWGLO4'), False)
        self.assertEqual(check_password('u/C 7aLbB 90Py3n1n'), False)
        self.assertEqual(check_password('8ySYlys'), True)
        self.assertEqual(check_password('ch9O3KYJlIfQ'), True)
        self.assertEqual(check_password('t3GYQCvy2'), True)
        self.assertEqual(check_password('QHb42tESovya'), True)
        self.assertEqual(check_password('9\\Ih'), False)
        self.assertEqual(check_password('9oR17i'), True)
        self.assertEqual(check_password('tOUDKNooobd1yTW3Is'), True)
        self.assertEqual(check_password('9To8U'), False)
        self.assertEqual(check_password('u2Kmd_GXN9uC3f'), False)
        self.assertEqual(check_password('Czgq6Phk2H'), True)
        self.assertEqual(check_password('u86ducboLsHe'), True)
        self.assertEqual(check_password('D_df8ArN0fan'), False)
        self.assertEqual(check_password('2vSt'), False)
        self.assertEqual(check_password('A4y'), False)
        self.assertEqual(check_password('Oq98iZjj8kH27uTZ'), True)
        self.assertEqual(check_password('r_6UtD7y14_WBYAr'), False)
        self.assertEqual(check_password('pSZShZigc6'), True)
        self.assertEqual(check_password('2oY'), False)
        self.assertEqual(check_password('5Ks_'), False)
        self.assertEqual(check_password('aoElqi8f'), True)
        self.assertEqual(check_password('hu+S-U9HU'), False)
        self.assertEqual(check_password('DuWohOnQ67J'), True)
        self.assertEqual(check_password('3Q /E2P?6uK'), False)
        self.assertEqual(check_password('qNiDS8'), True)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()