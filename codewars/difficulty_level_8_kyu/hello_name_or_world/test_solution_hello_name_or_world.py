

""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_hello_name_or_world import hello


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        tests = (
            ("John", "Hello, John!"),
            ("aLIce", "Hello, Alice!"),
            ("", "Hello, World!"),
        )
        for name, result in tests:
            self.assertEqual(hello(name), result)
        self.assertEqual(hello(), "Hello, World!")

    def test_advanced_cases(self):
        tests = (
            ("sharon", "Hello, Sharon!"),
            ("patRicia", "Hello, Patricia!"),
            ("michElLe", "Hello, Michelle!"),
            ("mArk", "Hello, Mark!"),
            ("mary", "Hello, Mary!"),
            ("roBert", "Hello, Robert!"),
            ("maRk", "Hello, Mark!"),
            ("liSa", "Hello, Lisa!"),
            ("deborAH", "Hello, Deborah!"),
            ("Kenneth", "Hello, Kenneth!"),
            ("DOrotHy", "Hello, Dorothy!"),
            ("ShaRoN", "Hello, Sharon!"),
            ("kevin", "Hello, Kevin!"),
            ("mARy", "Hello, Mary!"),
            ("antHOny", "Hello, Anthony!"),
            ("CarOl", "Hello, Carol!"),
            ("DaViD", "Hello, David!"),
            ("KimbERLY", "Hello, Kimberly!"),
            ("dOnna", "Hello, Donna!"),
            ("dOnaLd", "Hello, Donald!"),
            ("dOnalD", "Hello, Donald!"),
            ("lIsa", "Hello, Lisa!"),
            ("LiSA", "Hello, Lisa!"),
            ("AnTHonY", "Hello, Anthony!"),
            ("miChaeL", "Hello, Michael!"),
            ("donna", "Hello, Donna!"),
            ("AnthoNY", "Hello, Anthony!"),
            ("ruTH", "Hello, Ruth!"),
            ("wIlliam", "Hello, William!"),
            ("cArol", "Hello, Carol!"),
            ("jOSEPh", "Hello, Joseph!"),
            ("LInda", "Hello, Linda!"),
            ("SaNdRA", "Hello, Sandra!"),
            ("sHARoN", "Hello, Sharon!"),
            ("Maria", "Hello, Maria!"),
            ("bEtty", "Hello, Betty!"),
            ("eLiZabEth", "Hello, Elizabeth!"),
            ("SArAh", "Hello, Sarah!"),
            ("briaN", "Hello, Brian!"),
            ("anthony", "Hello, Anthony!"),
            ("kennEth", "Hello, Kenneth!"),
            ("RicHaRd", "Hello, Richard!"),
            ("SUsan", "Hello, Susan!"),
            ("betty", "Hello, Betty!"),
            ("JOhn", "Hello, John!"),
            ("jaSON", "Hello, Jason!"),
            ("DOnAld", "Hello, Donald!"),
            ("jOSePh", "Hello, Joseph!"),
            ("KImbeRLY", "Hello, Kimberly!"),
            ("rOnAld", "Hello, Ronald!"),
            ("kiMBeRLY", "Hello, Kimberly!"),
            ("jOhn", "Hello, John!"),
            ("CaRol", "Hello, Carol!"),
            ("KarEN", "Hello, Karen!"),
            ("keviN", "Hello, Kevin!"),
            ("MarK", "Hello, Mark!"),
            ("jeFf", "Hello, Jeff!"),
            ("LinDa", "Hello, Linda!"),
            ("sanDra", "Hello, Sandra!"),
            ("robert", "Hello, Robert!"),
            ("JEff", "Hello, Jeff!"),
            ("saNdRa", "Hello, Sandra!"),
            ("ChRIstoPHer", "Hello, Christopher!"),
            ("WilLIAm", "Hello, William!"),
            ("georgE", "Hello, George!"),
            ("nAnCy", "Hello, Nancy!"),
            ("STeven", "Hello, Steven!"),
            ("eLizabEth", "Hello, Elizabeth!"),
            ("sTeveN", "Hello, Steven!"),
            ("roNALd", "Hello, Ronald!"),
            ("lisA", "Hello, Lisa!"),
            ("John", "Hello, John!"),
            ("marGaret", "Hello, Margaret!"),
            ("saNdrA", "Hello, Sandra!"),
            ("jeNnifer", "Hello, Jennifer!"),
            ("jOhn", "Hello, John!"),
            ("pAuL", "Hello, Paul!"),
            ("roberT", "Hello, Robert!"),
            ("elizAbETh", "Hello, Elizabeth!"),
            ("daniel", "Hello, Daniel!"),
            ("jason", "Hello, Jason!"),
            ("sarah", "Hello, Sarah!"),
            ("dOnNa", "Hello, Donna!"),
            ("sHaRON", "Hello, Sharon!"),
            ("GEoRGe", "Hello, George!"),
            ("Nancy", "Hello, Nancy!"),
            ("dAvId", "Hello, David!"),
            ("linda", "Hello, Linda!"),
            ("linDa", "Hello, Linda!"),
            ("dAviD", "Hello, David!"),
            ("thomAs", "Hello, Thomas!"),
            ("rONALd", "Hello, Ronald!"),
            ("DAnIeL", "Hello, Daniel!"),
            ("MARIA", "Hello, Maria!"),
            ("maRK", "Hello, Mark!"),
            ("Carol", "Hello, Carol!"),
            ("kevin", "Hello, Kevin!"),
            ("chArlEs", "Hello, Charles!"),
        )
        for name, result in tests:
            self.assertEqual(hello(name), result)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()