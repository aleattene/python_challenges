
""" To start the tests, type from CLI: python test_solution_sum_of_missing_numbers.py """

import unittest
from solution_password_check_binary_to_string import decode_pass


class TestSolution(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(decode_pass(['password123', 'admin', 'admin1'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 '
                                     '01100100 00110001 00110010 00110011'), 'password123')

        self.assertEqual(decode_pass(['password321', 'admin', 'admin1'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 '
                                     '00110001 00110010 00110011'), False)

        self.assertEqual(decode_pass(['password123', 'admin', 'admin1'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 '
                                     '00110010 00110011'), 'password123')

        self.assertEqual(decode_pass(['password321', 'admin', 'admin1'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 '
                                     '00110010 00110011'), False)

        self.assertEqual(decode_pass(['password456', 'pass1', 'test12'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 '
                                     '00110010 00110011'), False)

        self.assertEqual(decode_pass(['password123', 'admin', 'admin1'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 '
                                     '00110010 00110011'), 'password123')

        self.assertEqual(decode_pass(['password', 'admin', 'admin1'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 '
                                     '00110010 00110011'), False)

        self.assertEqual(decode_pass(['password', 'pass', 'test'],
                                     '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 '
                                     '00110010 00110011'), False)

        self.assertEqual(decode_pass(['password123', 'admin123'],
                                     '01100001 01100100 01101101 01101001 01101110 00110001 00110010 '
                                     '00110011'), 'admin123')

        self.assertEqual(decode_pass(['password123', 'admin1', 'login'],
                                     '01100001 01100100 01101101 01101001 01101110 00110001 00110010 '
                                     '00110011'), False)

        self.assertEqual(decode_pass(['password123', 'admin321'],
                                     '01100001 01100100 01101101 01101001 01101110 00110001 00110010 '
                                     '00110011'), False)

        self.assertEqual(decode_pass(['password123', 'admin123', 'a'],
                                     '01100001'), 'a')

        self.assertEqual(decode_pass(['password123', 'admin123', 'b'],
                                     '01100001'), False)

        self.assertEqual(decode_pass(['password123', 'admin123', 'c'],
                                     '01100001'), False)

    def test_advanced_cases(self):
        self.assertEqual(decode_pass(['dAf2Ul', 'EqNgXy23U98xuuuZ', 'wpobt'],
                                     '01101101 01010111 01111000 01001011 01111000 01101111 01010000 01001100 01001001 '
                                     '01100001 01101001 01010101 00111000 01111010 01001001 01000100'), False)

        self.assertEqual(decode_pass(['BstnrnLs', 'wfsJNH', 'nYYurCFjJ', '0D5hxLGiYs', '0E8roSvB7PbI',
                                      'zKzdND9NoMwghLkOgJa', 'MGwrqSKjjFNBroG', '65Fri', 'ZNNfhByrC2c',
                                      '1op6bLvEbtQUNVbaN'],
                                     '01110111 01100110 01110011 01001010 01001110 01001000'), 'wfsJNH')

        self.assertEqual(decode_pass(['ic5ZZ2COoKpZ5', 'SeUbpnCurEzkhpuZy', 'kuBhB5z6Im8DljbCjo', 'SRYMBbLT9',
                                      'cMAUFt6D3NpXOKHiYQvm', '94fZsmyof7EDAhf'],
                                     '01101000 01110011 01101111 01111001 01001101 01000111 00110110 01011000 '
                                     '01001100 00110101 01001110'), False)

        self.assertEqual(decode_pass(['F51nxFoAofj3etJS', 'T3OyULMczR0zWx', 'e9xzl2Wk', 'ebBgY9d9', '9mfsItB9',
                                      'f9x7rIPUORgClzD1oo9', '2LhmVOVbt7NYVuG7KZ', 'qzUVZGT8Ptuv'],
                                     '00110010 01001100 01101000 01101101 01010110 01001111 01010110 01100010 '
                                     '01110100 00110111 01001110 01011001 01010110 01110101 01000111 00110111 '
                                     '01001011 01011010'), '2LhmVOVbt7NYVuG7KZ')

        self.assertEqual(decode_pass(['TUdEabAbgObHwKrzor', 'fJgbjV2q', '8P9G3ogAM5bPoU', 'KWZow1le7MiKPdThX',
                                      'LOok2YogvVzZ', '4ChuSAFzgYTB'],
                                     '01001101 01010011 01000100 01100111 01110001 00110011 01110000 01100111 '
                                     '00110011 01000001 01101010 01010010 01110010 01101000'), False)

        self.assertEqual(decode_pass(['yliv2zl3', '1FxkIK', 'gOMBt95y4Ao', '2Ohhyp1OHUbKGvNa', 'bVHw6I06tw', 'foAYa',
                                      'Py11sFsv86tuG', 'oIQSJaJqWIq1PXfeiM', 'e5xIhyQ'],
                                     '00110010 01001111 01101000 01101000 01111001 01110000 00110001 01001111 01001000 '
                                     '01010101 01100010 01001011 01000111 01110110 01001110 '
                                     '01100001'), '2Ohhyp1OHUbKGvNa')

        self.assertEqual(decode_pass(['wNUDM0', 'i44Ya', 'Df5kvoG5gd03Y4eNwCo', 'TYNj1ghzP7', 'SsykeAo7JMgvn1bopzd',
                                      '33LCIPSqTrFCM'],
                                     '01100111 01101010 01010100 01101001 01101111 01010101 01110111 01000101 01101000 '
                                     '01001100 01010001 01100101 01001101 00110111 00110110'), False)

        self.assertEqual(decode_pass(['4W55im7OvrIVe', '8fpIvI', 'k9cTsTzUTye', 'ILR1a3U', 'y5NLKmtX48r',
                                      'OB7WrYyt9bpNHH7', 'NMaQwuozS2J', '4Nub99dFzzuH1tNYYS', 'h2RgDsedz50'],
                                     '01011000 01000111 01000111 01110101 01010110 01101111 01110001 01001001 '
                                     '01010100 00111000'), False)

        self.assertEqual(decode_pass(['VrsEX', 'Gm3A0faPvj', 'bB7FuzkodKFin', 'mKEQ4sf9ikIZYLUCX7',
                                      'ZJhcMVJifWMEt1SNLK'],
                                     '01000111 01101101 00110011 01000001 00110000 01100110 01100001 01010000 '
                                     '01110110 01101010'), 'Gm3A0faPvj')

        self.assertEqual(decode_pass(['p1t9ALx9se3SvdAZBQC', 'pVPwQfz', '6H5F1cWiZY9'],
                                     '00110110 01001000 00110101 01000110 00110001 01100011 01010111 01101001 01011010 '
                                     '01011001 00111001'), '6H5F1cWiZY9')

        self.assertEqual(decode_pass(['Ihzw17B1OVuVLS', 'mTbH0zMeX6Z17crjJc', 'pr5h15RdddjsnI', '2jKf9alqklAB',
                                      '0lz6ABeOEmy', 'gBfX9dMDFPye', 'ljieH'],
                                     '01110110 00110001 01001011 01100010 01110110 01101111 01001010 '
                                     '00110100'), False)

        self.assertEqual(decode_pass(['ov872laNOMsmpG', 'qPP5dg9dQijMOZ9Y6ROJ', 'sHOtw5PKiDvv', 'FyagxMZqn', '6qe5PwD'],
                                     '01101111 01110110 00111000 00110111 00110010 01101100 01100001 01001110 01001111 '
                                     '01001101 01110011 01101101 01110000 01000111'), 'ov872laNOMsmpG')

        self.assertEqual(decode_pass(['WdSSRPJRo6buDQO', 'zQYTrBp7nIn', 'dtlFSmZD', 'CTO0KuSP', '6YwlSXe4v1qnj4Z9Js',
                                      'aNdYZz9uoL8RkP60eB', 'bclj2BEU79xhfJskZAFR', 'zG775l007', 'x9i3t7ehdl2uz'],
                                     '01111010 01010001 01011001 01010100 01110010 01000010 01110000 00110111 01101110 '
                                     '01001001 01101110'), 'zQYTrBp7nIn')

        self.assertEqual(decode_pass(['wfOyaLVlERjq9yvRiA', 'N6FreYyMhTP3XUEzIt', '1uHOr92fpQKw6',
                                      'wL2r3NYooM7kvfXR1nYa', 'rA8SW6BOkePo', 'V3GEW9vAjF8q', 'W88o8I8xjqnGEW5wdK0W'],
                                     '00110001 01110101 01001000 01001111 01110010 00111001 00110010 01100110 01110000 '
                                     '01010001 01001011 01110111 00110110'), '1uHOr92fpQKw6')

        self.assertEqual(decode_pass(['jSPtNebOMmsgvZ', 'CFwEhPU', '2yIyEA0u0xpEskyDbHL9', 'XC4EfiT4mRDExPDg6roi',
                                      'g1MZI7jncKDiVoL0M3Z'],
                                     '00110010 01001110 01010010 01000010 00110110 01101000 01000110 '
                                     '01000110'), False)

        self.assertEqual(decode_pass(['OuM4ac', 'rjGpkfyhHmgk', 'h3IrxkoA8NbVhnGqNgV', 'jW5DUKYEEdfLK7',
                                      'AE4kruGQeauD9QRu', 'gwOfUK6y1i10', 'msUtH'],
                                     '01110010 01101010 01000111 01110000 01101011 01100110 01111001 01101000 '
                                     '01001000 01101101 01100111 01101011'), 'rjGpkfyhHmgk')

        self.assertEqual(decode_pass(['LXJgrUhb0IhWItMeRmLq', 'j8TKwK', 'Vn6duxypz6g38vg71qy9', 'Mm7wNJ7InGMME',
                                      'yMxIBa9T', 'dSlvOMfQ1hLIDhVDhR', 'VMEaUh', 'f0F1pT6YzcJ',
                                      '1YnIa9MXABu7vUXiSEDO'],
                                     '01101101 01101010 01001100 01000010 01110001 01110000 01101110 01101110 01101111 '
                                     '00110110 01000100 01111001 01001011 01000100 01010111'), False)

        self.assertEqual(decode_pass(['YTX2Z4zX', 'SxA45sih1XQnw3E2Co', '7Zxa6LapZXrp'],
                                     '01000110 01011000 00110111 00110011 01000110 01010011 00110110 01011001 '
                                     '01000100 01000100 01001001 00110010'), False)

        self.assertEqual(decode_pass(['TcZ7QeBsdCuw3tbV9K', 'kMZi5V', 'WwcfRjSUXTmmUnHph'],
                                     '01000110 01000111 01001110 01010001 01101010 01000110 00110110 '
                                     '01010111'), False)

        self.assertEqual(decode_pass(['l6bXj6RBVnvCYFo', 'TguLIimqio0c1GWkG3', 'f9L6I', 'jTNoHjmSRJoNpZo',
                                      'dW55ruxiKGind', 'FXIgk', '92jP5USzYdiskt', 'lKMzgQwvpgEmCB',
                                      'zsyx369tzpKMLBXq2V', '8FF3XsmrUT3qM'],
                                     '00111000 01110110 01110110 01000111 01110010 01100011 01000101 01101111 '
                                     '00110010 01110111 01010110 01000001 01001000'), False)

        self.assertEqual(decode_pass(['wMHgItNnZY45u', '2BYQXC', 'e8ZqcVmh', '1KUytV', 'PhGKri4Oh69c1iVWzgj',
                                      'cHulaTCuFnvkdS4jdkg', 'Io4rf', 'SUurq3ItghM'],
                                     '00110001 01001011 01010101 01111001 01110100 01010110'), '1KUytV')

        self.assertEqual(decode_pass(['1kRPqpondmOtJwT', 'bpkMyfji9JiONS43vVLD', '3Y8YuJ8JfkgQDPpNk', 'o28k5cTarGu',
                                      'wDnVfZbkqEoJBveDn', 'QrXsCxXjxlS', 'S2UBWj', 'N1c0HVImgQcYNZhHG'],
                                     '01101111 01001110 01011000 00110001 01101100'), False)

        self.assertEqual(decode_pass(['HZmoviANFB', '7Cnz5J04SwKied', 'axgNV', 'UwC1R1vb6jrA', 'rEYhSRgOs4'],
                                     '00110111 01000011 01101110 01111010 00110101 01001010 00110000 00110100 01010011 '
                                     '01110111 01001011 01101001 01100101 01100100'), '7Cnz5J04SwKied')

        self.assertEqual(decode_pass(['W824bDbhbH6', 'uuPQP1Nak7', '2DFfG6OKwajG67g4CM', 'DP37HL', 'wkUqiz1wVhlI',
                                      'lm3HA6F6ozY2B', 'STHaxPFl42dr3G1g', 'QXDl1e5bBl', 'sTKa534c', 'XQJCQlysPHJaTP'],
                                     '01100010 00110000 01000100 01001000 01101100'), False)

        self.assertEqual(decode_pass(['TWWwtgK', '35ajpx2u3P9', 'vZeEeTlR2NHfIwxW5U', '2oZPPbnLzcEN',
                                      'b13x2MBGMwuTrMi5x5LE'],
                                     '01010011 01110011 01010100 01000101 01000110 01110001 01111000 01000001 01001101 '
                                     '01101011 01010000 01100101'), False)

        self.assertEqual(decode_pass(['SPGwNoI27ei', 'Ca8Tb', 'VKBRCEWkV2', '8GO2dlMFwi', 'qf20tEajOnQ',
                                      '4xBlSsVlNqTUa', 'SO9LeyP', 'Nh8V2SmioPMsWMz2', 'n2mXy'],
                                     '00110101 01110110 01111010 01001011 01101001'), False)

        self.assertEqual(decode_pass(['3fggzVYX', 'eJh30f', 'OhVx05KkQOrCcu0ds3n', 'AKRkDsOh', 'QCMUuOcuBkRSCC',
                                      '9rI2UavTn9'],
                                     '01010001 01000011 01001101 01010101 01110101 01001111 01100011 01110101 01000010 '
                                     '01101011 01010010 01010011 01000011 01000011'), 'QCMUuOcuBkRSCC')

        self.assertEqual(decode_pass(['w8pOBFcvTUTYZY', 'TFfiqWVqpBcGFI2', 'FFgc865dnUczOe6', 'Cpsbg9qbyHsKGv7nESm',
                                      'BATwPAYXb', 'fK8I22gev', 'yxlnb6f0uIIw0', 'z1ETsA0C', 'DZhX0zn5ygF',
                                      'qWSPAQSUmoJk'],
                                     '01000111 01110010 01101100 01111000 01111000 01000100 01011001 01110011 01001010 '
                                     '01010000 01011010'), False)

        self.assertEqual(decode_pass(['Y3PQkFjDE3WOJjX1xxkl', 'EyuJTKIm9V3', 'SXUzJqHtV3fiuh', 'js9LTr4VSu',
                                      'KemfHc3wb'],
                                     '01000101 01111001 01110101 01001010 01010100 01001011 01001001 01101101 '
                                     '00111001 01010110 00110011'), 'EyuJTKIm9V3')

        self.assertEqual(decode_pass(['WaWBbUEplCSt2jRrS', 'yaZuAK0U', 'eA1vteTch7BxcFEurK', 'w09ANY',
                                      'irbFz5h2icowaQ6', 'BRAwY9q4mcoM4qfwp', 'mDAgEuWE', 'Yx6TB7qu8BmKg'],
                                     '01010010 01100100 01101010 01101110 01000111 01011000 01010001 01001111 01101111 '
                                     '01110000 01110001'), False)

        self.assertEqual(decode_pass(['tuKkAv5G', 'TRa7fp', 'fVzEsKt0iH7rc27l', 'TU0CqDLXNi', 'xwnSDQvJUET',
                                      'nw1Vy8xS5pPlAgWNW', 'rwJ1J9KkQX2iwolT', 'Hz45R5SI1', 'jgIf6U30'],
                                     '01110010 01110111 01001010 00110001 01001010 00111001 01001011 01101011 01010001 '
                                     '01011000 00110010 01101001 01110111 01101111 01101100 '
                                     '01010100'), 'rwJ1J9KkQX2iwolT')

        self.assertEqual(decode_pass(['gMEaKDHiF6', 'bfsWi', 'Zy0EYhG6PuQ', 'dRg6O1Q', 'Bc1ij9IXzf2AQC1L', 'SRHlz',
                                      'JomVFeWQh'], '01010011 01010010 01001000 01101100 01111010'), 'SRHlz')

        self.assertEqual(decode_pass(['34qii2t', 'V0BIyuPRyRMYP', 'uww2At6fvE', 'yTPAP6tB', 'oyyjIA3cm', 'roZe22Pe',
                                      '9yoBs4jexcINPka', '5jSyu1TRuYpP'],
                                     '01011010 01010110 01100111 00111000 01001100 01001101 00111001 01010110 01011000 '
                                     '01101101 00110110 01000111 01000101 01110010 01111001 01100101 01010101 '
                                     '01100100 01000110'), False)

        self.assertEqual(decode_pass(['UZKOeMso', 'oayETYQqykyP', 'yZSngg3aXv9gajK', 'XrN5pChRIozs4t', 'Ow0IgZGz7U6',
                                      '3cCVvq', 'zYwQXVzm8tFxz', 'kOz75QebCY0A', 'SqQTA1W7FXUw4GFATm5J',
                                      '7bXA5z6eU1Mu6R4fbVBU'],
                                     '01100001 01011010 00110001 01111001 01110110 01000101 01010010 01111010 01110001 '
                                     '01000111 01111010'), False)

        self.assertEqual(decode_pass(['YsGviJXU0zjcNQ0QOmV', '4rzAyMUb', 'pIhVrF', '3iWix6HMyVTU',
                                      'JAeF05iPtVNbIHP8W', 'kVsIoOytezzPDa', 'HToNMiOIj8', 'KaBp1xbKYr',
                                      'xRBxeeDlI1x0L'],
                                     '01101010 01000111 01001100 01010010 01110001 01110000 01110011 00110011 01000001 '
                                     '01001011 01001111 01001101 01010010 01001000 01100100 00111001 '
                                     '01101111'), False)

        self.assertEqual(decode_pass(['tgPpl49cumvjfli0FHko', '3ssGKx', 'KHrDHKb4mQY07', 'BAomQns5agJhG', 'qxjGen',
                                      'MiAzQN5ZgL', 'rpfzV3IL', '4JK8qOSTLiDQR3N8SqTv', '7517x94HAnU17'],
                                     '01100110 01010001 01100110 01001100 01101010 01000001 01101110 00110111 01101000 '
                                     '01100111 01001001 01001101 01000110 01110010 01111000 00110010 01000111 '
                                     '01010100 01111000 01100011'), False)

        self.assertEqual(decode_pass(['3HuOP0anHrXd', 'MypqgbbaN', 'xnAlnkHvjx6MEhJwG', 'Wr1qhKRmhQhMJaC', '11uESt',
                                      '6cl6XYG6', 'zmdCvQUbrpT', '3XrGcY1bXtO3rtVO18uq', 'LIu1GoY'],
                                     '01111010 01101101 01100100 01000011 01110110 01010001 01010101 01100010 '
                                     '01110010 01110000 01010100'), 'zmdCvQUbrpT')

        self.assertEqual(decode_pass(['5iZUM7', 'lA6D2RULP1qSwDwMsj', 'fbyT7vr8a9g0'],
                                     '01010111 00110000 01000101 01000011 01110011 01001100 00110111 01100110 01111001 '
                                     '01110100 01101100 01101011 01110000 01100011 01100010 01110100 01100001 01101111 '
                                     '01000011 00110110'), False)

        self.assertEqual(decode_pass(['r2d9SVl81krDCsqdkpd', '7pTxCR5', 'o7uCYrVNDPiqSLci4ql4', 'cBJFPuki1'],
                                     '01110101 01111000 01101110 01101000 01100100'), False)

        self.assertEqual(decode_pass(['iLfkcIf9vn4', 'HbccWEbhM4z7NZNQ', '1z8JBMmpkNsDfa56', 'RrzJ0LNJArlBwI',
                                      'cQQFLFBu4ANfd', 'pTJq6FHhUJD98tvM8zM', 'TNk5Iq1'],
                                     '01100001 01011000 01101010 00110010 01000001 00111001 01010010 00111000 01010000 '
                                     '01001110 01110100 01101001 01001101 00110000 01110011 01110111'), False)

        self.assertEqual(decode_pass(['VYN1s', 'dd1j1X', 'QW6mRo'],
                                     '01010110 01011001 01001110 00110001 01110011'), 'VYN1s')

        self.assertEqual(decode_pass(['IKDmgyOD87JRLe', 'Aqhyepxynrk', 'vjU7bS5ljm1D4EmE', '327zc47m4EjGX'],
                                     '01000001 01110001 01101000 01111001 01100101 01110000 01111000 01111001 01101110 '
                                     '01110010 01101011'), 'Aqhyepxynrk')

        self.assertEqual(decode_pass(['DY1Axrwsf', 'P5kv8zdjnVpzJUh', 'tSH20Aud5', 'uNfDWELKbNtHvE',
                                      'fJ2U5Q09nTAR33HWymF', 'BPDcd'],
                                     '01000100 01011001 00110001 01000001 01111000 01110010 01110111 01110011 '
                                     '01100110'), 'DY1Axrwsf')

        self.assertEqual(decode_pass(['R0tAP2', 'gem1CYOtcXyiUa4BQnC', 'MlRj2IqNkG52oMfQzZ', 'vzL900HoWvgEoO5doh'],
                                     '01110110 01111010 01001100 00111001 00110000 00110000 01001000 01101111 01010111 '
                                     '01110110 01100111 01000101 01101111 01001111 00110101 01100100 01101111 '
                                     '01101000'), 'vzL900HoWvgEoO5doh')

        self.assertEqual(decode_pass(['2srTI4uqseCnmQd', 'd3Nh7jbY2f', 'jk7LVFRsI55G', 'agYBI5P0n', 'ZOF18TNj'],
                                     '01011010 01001111 01000110 00110001 00111000 01010100 01001110 '
                                     '01101010'), 'ZOF18TNj')

        self.assertEqual(decode_pass(['K4lm3', 'K6lqykwz1Q', '1eSdxf6v8', 'qvH5QRJXvBz', '5tIqm8m9sRWn8c4m6Q',
                                      'VQv3h0HDi824G9j3', 'K5YO91fKeadH'],
                                     '01001011 00110101 01011001 01001111 00111001 00110001 01100110 01001011 '
                                     '01100101 01100001 01100100 01001000'), 'K5YO91fKeadH')

        self.assertEqual(decode_pass(['dL9edvjqMbvHOsEPl1p', 'qYsD1VrdXq3oRggekHXu', 'XUDCzo', 'lkbm39jY9',
                                      'O8AFXaq', 'CdvEFjcEA', 'zuiC6Gu1Vclw', 'TTpy3T8LJrFBf0Vu',
                                      'j0vELBLJB2ljP74J6Gc'],
                                     '01001111 00111000 01000001 01000110 01011000 01100001 01110001'), 'O8AFXaq')

        self.assertEqual(decode_pass(['SYYXOMFy', '2DvnNhdVWUVE9t', 'PxuCaSOHv1aKik9R8ky', 'bWEhXu', 'oAMuUEA9wi',
                                      'NlzZgbMVFoPLVE', 'vE7xnBvVkjV', 'Ta817e57kA5QTwUz'],
                                     '00110010 01000100 01110110 01101110 01001110 01101000 01100100 01010110 '
                                     '01010111 01010101 01010110 01000101 00111001 01110100'), '2DvnNhdVWUVE9t')

        self.assertEqual(decode_pass(['pXpEDv0AVlE', 'cpMMNamk2jQh', 'QlTPkdilB6X6', 'mXmYJqPN1qQCz',
                                      'S4JPVu2seEVq6ogN1Cu', 'NZCN9GR', 'CaHOadrUM', '8RaBx6TVXMli3iu'],
                                     '01010001 00110100 01000011 01010000 01101001 01000111 01011001 01101111 '
                                     '01100111 01110011 01110100 01001101 01101101'), False)

        self.assertEqual(decode_pass(['Cu2qSIqfMjmeSwfuZg5', 'estQIjE8LtAh', 'T1SEevlUb6Vf', '4uHudXECsZh',
                                      '1wfuDTJ', 'Jwpr7RPthV9SRes1', 'LkBBX', 'jrpG2HKtNenHTC', 'vI5IzvP6XiVAZpIIqij',
                                      'DlVhXsEdqAq'],
                                     '00110001 01110111 01100110 01110101 01000100 01010100 01001010'), '1wfuDTJ')

        self.assertEqual(decode_pass(['mmxnSDp8', 'i4L2CM', 'EfFy2ko', 'xnlV30Ao'],
                                     '01100101 00110010 01100001 01110100 01001000 01111000 01001111 00110100 01000110 '
                                     '01010011 01101110 01000111 01000101 01110111 01100111 01001101 '
                                     '01111010'), False)

        self.assertEqual(decode_pass(['Bu2XqD', '4jMqC55Ric', 'pefuNjBhq', 'X5MXzzf6Esc6XCRR', 'GUqlKXzIk',
                                      'JtqXZSbU4q', 'a4RdW'],
                                     '01111001 00110110 01101001 01010101 01110101 00110001 01010110 01011010 01110101 '
                                     '00110100 01101000 01001110 01110100 00111000 01101000 01010011 01010111 '
                                     '01100111'), False)

        self.assertEqual(decode_pass(['CTv5hlM9bSF', 'JrEaHyrId8S8EVPFT2d', 'kZxhaXq4U6', 'oFNTJhuzxvK'],
                                     '00110011 01101100 01101110 01101111 00110010 01101000 01100011 01100100 '
                                     '01101011 01100010 01100100 01010111 01011000 01110111 01000111 01101000 '
                                     '01100110 00110110 01000001 01100100'), False)

        self.assertEqual(decode_pass(['xpB62Jcsqg36fJp', 'RjTU7gyzRA421', 'd5iPM'],
                                     '01010010 01101010 01010100 01010101 00110111 01100111 01111001 01111010 '
                                     '01010010 01000001 00110100 00110010 00110001'), 'RjTU7gyzRA421')

        self.assertEqual(decode_pass(['hwRBij74', '86VKmp', 'yHKs8YuYC3ZlvFe8r', 'iNvp6ZubxSQIcoYvM', 'RtAE5fTS'],
                                     '00111000 00110110 01010110 01001011 01101101 01110000'), '86VKmp')

        self.assertEqual(decode_pass(['t4paRT9R', 'MgfecwajMZy', 'KvK84Ko4jC3jmRqw5Z8A', 'VNQqHolXq1vBf',
                                      'LAclPrjA3GS2iceYdInO', 'g9Isinj', 'H5jB2', 'tCEQaFKmEGBc', 'e01x2bwqs2BHfZ'],
                                     '01101010 01000010 01000110 00110100 01000001 01000100 01001101 01100101 '
                                     '01101000 01110110 01101000 01010101 00110011 01000111 00110001 01001000 '
                                     '01100101'), False)

        self.assertEqual(decode_pass(['hL3QI1bc408', 'aOl7XSBwjWI8KxEzY', 'wQa2CbXl'],
                                     '01110111 01010001 01100001 00110010 01000011 01100010 01011000 '
                                     '01101100'), 'wQa2CbXl')

        self.assertEqual(decode_pass(['czjWzfJL9A4', 'RjB7ZlbRx', 'lNWjwlX8S'],
                                     '01101100 01001110 01010111 01101010 01110111 01101100 01011000 00111000 '
                                     '01010011'), 'lNWjwlX8S')

        self.assertEqual(decode_pass(['ZyXMiatX5nxEL', 'X3oiMk5wyHSDJiml', 'VimNB', '6K16W', 'ttL0dfChc'],
                                     '01011010 01111001 01011000 01001101 01101001 01100001 01110100 01011000 '
                                     '00110101 01101110 01111000 01000101 01001100'), 'ZyXMiatX5nxEL')

        self.assertEqual(decode_pass(['Hf20ujE5fS', 'NztskaPCWqS', 'ZGwmuNl'],
                                     '01000001 00110000 01001100 00110101 01111001 01001011 01101100 01101101 '
                                     '01100110 00110100 01110100 01110000 01001010 01110001 01001101 00111001 '
                                     '01000011'), False)

        self.assertEqual(decode_pass(['95RfoSqiQuejQDC1', 'ZCMfH7P27Jx', 'FkGMTPGZGCC3WQ', 'aIhT2yADhA4G1ts8x2W'],
                                     '01100001 01001001 01101000 01010100 00110010 01111001 01000001 01000100 '
                                     '01101000 01000001 00110100 01000111 00110001 01110100 01110011 00111000 '
                                     '01111000 00110010 01010111'), 'aIhT2yADhA4G1ts8x2W')

        self.assertEqual(decode_pass(['LTbFw2q75', 'WZMU3YZptBH1rk9LRox', 'r3yhnOBO7tY728naehp', '7ZPGgJ',
                                      'wNkopGn64VnVZERtUPOU', 'qTs3iSSFi4C', '2MFt6Q'],
                                     '01001001 01101011 01111000 01100111 01010110 01010010 01101011'), False)

        self.assertEqual(decode_pass(['X995cMyh7cnFiXSfqxpD', '5S5Kwx3DcyrKJh', 'a6rwnu', 'rkiZ86koeOu9Sw9YX'],
                                     '01110010 01101011 01101001 01011010 00111000 00110110 01101011 01101111 '
                                     '01100101 01001111 01110101 00111001 01010011 01110111 00111001 01011001 '
                                     '01011000'), 'rkiZ86koeOu9Sw9YX')

        self.assertEqual(decode_pass(['kSvISJKFz4Gyi', 'gemRHRv', 'dv3ve6kNeHwgm', '147eW3b0l8', 'ysHTbZaWL0m0RgkVGn',
                                      'JWZRP6'],
                                     '00110001 00110100 00110111 01100101 01010111 00110011 01100010 00110000 '
                                     '01101100 00111000'), '147eW3b0l8')

        self.assertEqual(decode_pass(['uxUZPlu', 'GGQ2sEesW59EFHMA', 'd4nJWboV0W1OOmwFUd', 'suOyZYANWr', 'GNcuwrk',
                                      'XDg7vG7P1iISIyzfgN', 'rQL7egZHevC4mdHfW9P', 'f3864hoDgNLvzDM',
                                      '8SZ6S2fNfQdzqzTp9'],
                                     '00110001 01000110 01100010 01010000 01001101 01010011 01010100 00110101 '
                                     '01101100 01000111 01111010 01100101 01001010'), False)

        self.assertEqual(decode_pass(['Ut6T0SP1dNq44U', 'JglnR4bH', 'QclSiCxhgG2jWY'],
                                     '00110001 00110101 01100010 01010011 01111001 01100111 01101101'), False)

        self.assertEqual(decode_pass(['NQwQAuv4qT2', 'mcLRguk0xnL', 'o2P2zrpBjvRMX6', 'iwLqd', 'KlcaUmDg1S1BSWQexYz'],
                                     '01100010 01101000 01110000 01000111 01001000 00111000 01010011 01100010 '
                                     '01000110'), False)

        self.assertEqual(decode_pass(['XcPqQteljcLj79tdKCT', 'V1i7B25deYzHvLI4MI', '7zfrIf', 'UbEmTungHwRlL',
                                      '6vMjTn68XSR', 'jXmmyAelVUFJgSZ0V1Ik', 'WamHXSCZfJL5rpf', 'AC3a24J',
                                      'PqVEkVEiXp6aHO'],
                                     '01101010 01010000 01000100 01000111 01101001 01110101 01011001 01011010 '
                                     '01001011 01010110 01000101 01000101 00110010 01010110'), False)

        self.assertEqual(decode_pass(['zMmj1Aw', 'vn5jm', 'PR7zTmayFrWPOJPr4B', 'OUUMglS', '7AnEPSYAu',
                                      'xmlNwufatlDWxJpkd6Pt'],
                                     '00110010 01101111 01101100 00110101 01101010 01001100 01010101 01010001 '
                                     '01110000 01101001 01100011'), False)

        self.assertEqual(decode_pass(['jAlxXA6', 'YhNmwqijkwLT', 'Y2jz1', 'pszxjB', '4pZzsKivbC6gAs2', 'Ntu82t9Mh7',
                                      'VTDXruYSTKoal3QBroLr', 'xGqD9U', 'ZirgJJDpr7I3zconf9FL'],
                                     '01011001 00110010 01101010 01111010 00110001'), 'Y2jz1')

        self.assertEqual(decode_pass(['RE37nGsVDpMF2F2OHcyS', 'Okqsq0mO2lq51uCjO88D', 'ayJKnJ5o', 'G6AUMIrIDJzG3t',
                                      'wV9qrp'],
                                     '01101010 01100100 01110111 01000101 00110101 01100010 01100001 01110111 '
                                     '01110110 00110101 01101110 00110111 01101101 01101000 01100100 01000010 '
                                     '01000111 01110010 01101011'), False)

        self.assertEqual(decode_pass(['6RjF5JPR5QA0PI1U', 'tWS5EDXNGuLYlygmob', '39CrAOZY8IWlfJdg3', 'lbHr3ld',
                                      'dBgLWWGBflRfsJA4s'],
                                     '01010011 01000111 01101111 00110110 01010010'), False)

        self.assertEqual(decode_pass(['hcZDlwVOpZ4', '9GvYdT2F4L4Ne0D5t4u', 'jz2l00Lb', 'B02J52Qh5cR3glaDV2',
                                      'iZjdLuqd', 'jK5Z1PCTbfo', 'q72TBqTWRsh7Heq', '8dk7h12YMuALBF'],
                                     '01010111 01011001 01100100 01100110 01001001 01001110 01010011 01010100 '
                                     '01101111 01010000 01111000 01010010 01110100 01000111'), False)

        self.assertEqual(decode_pass(['aJal9', 'qO2JEDqsh3ygF', 'cAKSimZ22N00', 'YNFkNL76XrnD', 'TEx8b', 'JEYogrW',
                                      'YnOkssEFny', '5A8KY', 'MZRFflSp49NzJd1uuUE'],
                                     '01100011 01000001 01001011 01010011 01101001 01101101 01011010 00110010 '
                                     '00110010 01001110 00110000 00110000'), 'cAKSimZ22N00')

        self.assertEqual(decode_pass(['iRhuEh0KEYixh0', '687inMbt51xzd', 'XcElWFrsA', 'lCLoQolINbbxc7ur'],
                                     '01101111 00111001 00110010 01110010 01010011 01000111 01010010 01101110 00110101 '
                                     '01100110 01001001 01000100 01110111 01000001 01110100 '
                                     '01001111'), False)

        self.assertEqual(decode_pass(['baOWmjfcT5tEdhF8mWn7', 'Z14gNw8UJHnDy', 'shgnDcuePcbLYkU2', 'UfOZsQ9GcAZ1Y7r',
                                      'okip2LX9wMvlnkb', 'npVrmDcwPN5s', '6TSdX4J3MLptL7CWB', 'MJVr59ceh',
                                      'XzOIWFtVa9f4O'],
                                     '01101111 01101011 01101001 01110000 00110010 01001100 01011000 00111001 01110111 '
                                     '01001101 01110110 01101100 01101110 01101011 01100010'), 'okip2LX9wMvlnkb')

        self.assertEqual(decode_pass(['NTBO4l4BqqPOObDqzcz', 'ImePxnH1wzA4nbjOEkXo', 'zkJSalr8W0sS2',
                                      'aIN88SYkPOfll7piyjL', 'AqTt5stbExKfF2iMxPT', 'Qe62rItvAHahEWtWuVD',
                                      'VL99fuFVufMNND0', 'iJnWhQyxNfSx', 'dKCjGkMquNipj0n8Ir'],
                                     '01101001 01001010 01101110 01010111 01101000 01010001 01111001 01111000 01001110 '
                                     '01100110 01010011 01111000'), 'iJnWhQyxNfSx')

        self.assertEqual(decode_pass(['J1sq8WgitNphqxEzAOn', 'wvBYiK59OvEdn3UxKQNX', '7rrZn4C'],
                                     '00110101 01101100 01101000 01110010 01001010 01111000 01100010'), False)

        self.assertEqual(decode_pass(['uvr9DBK', 'OaB5weP6ubHkpulYs', 'riTEzoZK6JTLI', '1zr3G5fbC', '6sxETN'],
                                     '01110101 01110110 01110010 00111001 01000100 01000010 01001011'), 'uvr9DBK')

        self.assertEqual(decode_pass(['Q0SO2TyS3AEHH4Ci4Wy', '5AN7OY51lRhLVQ8ohqk', 'qpwMzl0eJkelTu3EZ',
                                      'l6zqOMEKroMymVNgRpb', '0c1FACVk', 'OCmIivdCmvVMjy2EHn'],
                                     '00110000 01100011 00110001 01000110 01000001 01000011 01010110 '
                                     '01101011'), '0c1FACVk')

        self.assertEqual(decode_pass(['2W8DzsiF6ciwzFJCaki', 's0pZDJiOiBOn', 'U9kjwj0FvKkG4z', '9XIPVJDoIS3KYM',
                                      'IFsmgX5d', '9ourkQfV4bpvHWspiz', 'vJ0JSPl28x3'],
                                     '00111001 01101111 01110101 01110010 01101011 01010001 01100110 01010110 '
                                     '00110100 01100010 01110000 01110110 01001000 01010111 01110011 01110000 '
                                     '01101001 01111010'), '9ourkQfV4bpvHWspiz')

        self.assertEqual(decode_pass(['JfBFt2xIfDK', 'GW5MLDa', '2rNzh1VpJMis9VWu', 'gkLCxayt9p', 'dlh57YN7u',
                                      '3JcGnQ', '7hxOtjkrDa6Z8m'],
                                     '01001101 01010101 01011001 01110011 01110100 00110111'), False)

        self.assertEqual(decode_pass(['plusH', 'bgFrBHi7WEtxoKVC14Xq', 'SmqHX6sm5PjZ', 'lBIpF15', 'EAks9M41giwyB'],
                                     '01010111 01101111 01001010 00111000 00111001 01111001 01010110 00110110 01000010 '
                                     '01101000 01101111 01000111 01000010 01101110 00111001 01001000 01010100 00110011 '
                                     '01101110'), False)

        self.assertEqual(decode_pass(['Rn9g5UjwiO6PW0gg0EjC', 'uz65v815r', 'sXwyqPGV8pr3Vy', '5NGMn', 'BzreiPDO'],
                                     '01110101 01111010 00110110 00110101 01110110 00111000 00110001 00110101 '
                                     '01110010'), 'uz65v815r')

        self.assertEqual(decode_pass(['8AFlHem', 'QQVqj', 'AAhgcmEg0N', 'TQPSb78', 'YqcQUr5', 'aYGqmWpnyuisnoKzbiLK',
                                      'Cg10uLcL18SbqShN9R', '3UoX7EgNyDIDZhORR', 'fFwouiA'],
                                     '01001110 01010101 01110111 01000010 01110100 00110010 01001110 '
                                     '01101100'), False)

        self.assertEqual(decode_pass(['mw2rZG628kJSQReuEY', 'IR2Ev', 'IeZeGvW9IOY3OtjgB', 'Sizybd1zaSoL'],
                                     '01001111 01110000 01001101 01011001 01110101 01010110'), False)

        self.assertEqual(decode_pass(['S1OkFeP9YrnVPv', '1DlacjTUKuTcN3', 'uT3X8rvt8eDDsBoRZbW1', 'l9Z9NiQDfXX6',
                                      'i9hoBoG'],
                                     '00110001 01111001 00110001 01100110 01001111 00110001 00110000 01100111 '
                                     '01010110 00110100 01001101 01110101 01010000 01000001 01110001 '
                                     '01000010'), False)

        self.assertEqual(decode_pass(['d0PuHvV6w', 'Mno45zx8MhnPj9m3NhxM', 'sj6eDhO84w', 'wbds8zeoxnT5LZ',
                                      'Vy59tEh0VZPtPPN', '26d1JJ9TfUKj', '2YoYNVLBEOe', 'WQBuWGv', 'uwTqOL'],
                                     '01110101 01000001 01001101 00110001 01110111 01010001 01010100 01010000 01100100 '
                                     '01100011 01110011 01111001 01110100 01010011 01001101 00111001 01110110 01100011 '
                                     '01010110'), False)

        self.assertEqual(decode_pass(['OqT8FV31q6mCYwS1v', 'yOfXdwWWmU', 'DO1tkD8JMuR4gejcc', 'rrjX0'],
                                     '01110010 01110010 01101010 01011000 00110000'), 'rrjX0')

        self.assertEqual(decode_pass(['iSfli', 'mSyv6', 'K0AjVE2a5uN188Zq', 'y3CLuRG', 'AGK3cxaxQHyphcinC',
                                      'cuijFGSuVM6WRMhfK', 'PS1nF1l28', 'RoDMo0A4R2Jq', '2AoDb2jpSf',
                                      'a0uY57Iu8wIV'],
                                     '01010010 01101111 01000100 01001101 01101111 00110000 01000001 00110100 01010010 '
                                     '00110010 01001010 01110001'), 'RoDMo0A4R2Jq')

        self.assertEqual(decode_pass(['ntFlHOJuVLZ1', 'gzCtxoKXwhKg', 'sQwVqHzWIj43o9', 'ELRjbzQ3c9YGvi', 'TN35I'],
                                     '01101110 01110100 01000110 01101100 01001000 01001111 01001010 01110101 01010110 '
                                     '01001100 01011010 00110001'), 'ntFlHOJuVLZ1')

        self.assertEqual(decode_pass(['1ZxlJiPSBOLRgky', 'whVkOs2gsUCFD1', 'B8P3UTsQT8XWz6lIphNu', 'nTC6RT93YViK',
                                      'icVbrw3ZJ', '283fSII', '3rwOPhgF39epbPpuN', 'JwcEIsov0y5EeYShLmj',
                                      'bEDflGe2RtjSgRptVjxs', '2TtDs82RULNGZW3gxdFj'],
                                     '01101110 01010100 01000011 00110110 01010010 01010100 00111001 00110011 01011001 '
                                     '01010110 01101001 01001011'), 'nTC6RT93YViK')

        self.assertEqual(decode_pass(['3O3nIC', 'f6PM0CMkB', 'jBRV7', 'l7ZYnlBwIjAsl5S', 'OjfhJkVBea7RM2JQB'],
                                     '01101100 00110111 01011010 01011001 01101110 01101100 01000010 01110111 01001001 '
                                     '01101010 01000001 01110011 01101100 00110101 01010011'), 'l7ZYnlBwIjAsl5S')

        self.assertEqual(decode_pass(['P5GukAlQfaTOD7n1J', 'OAAcJtSz7', '7Vao7'],
                                     '01100110 01011001 01000010 01010010 01110010 01111000 01110111 01110101 01010100 '
                                     '01101110 01000010 01110000 01111001 00110100 00110000'), False)

        self.assertEqual(decode_pass(['Q8CCG72', 'mVaSqekVmcNVcY', 'K8oFfx', 'WTCx1ZbNAaWNQH9I', '7LGjBQIYBhHEowaP2s',
                                      'oiUn02YalucRPcnv', 'cp2gsRKv0S5wkJa'],
                                     '00110111 01001100 01000111 01101010 01000010 01010001 01001001 01011001 01000010 '
                                     '01101000 01001000 01000101 01101111 01110111 01100001 01010000 00110010 '
                                     '01110011'), '7LGjBQIYBhHEowaP2s')

        self.assertEqual(decode_pass(['ASVOXg7gVrE4QnJ', 'omWsFw', 'YB5EVO9aWtInrZpcJl', 'deOc3nx21M',
                                      'sGcP6xUmgpgh2fI', 'FZOXwM2r2gLCjupPV6p'],
                                     '01000110 01011010 01001111 01011000 01110111 01001101 00110010 01110010 00110010 '
                                     '01100111 01001100 01000011 01101010 01110101 01110000 01010000 01010110 00110110 '
                                     '01110000'), 'FZOXwM2r2gLCjupPV6p')

        self.assertEqual(decode_pass(['cmbsJoFSgg19tV', 'F7yfUuE', '96AQJvXiNtM4SXiH0BK5', 'vIRlYQOL47HEVISNuE',
                                      'Ng81YJHQW1Kmg3b5', 'dFNyiKKuLdzwqXS', '7DzFo0fI1g2NmAvSlU',
                                      'PdzjF10ZldJC2jgZlUn', 'JkkbGVnLdg4ZVg96fqhB'],
                                     '01101010 01001111 01000100 01001101 01010110'), False)

        self.assertEqual(decode_pass(['XNAMI5hUfiPGckb', 'Sov3GSuxomg09Y2ZuHeJ', 'miB0xzasns6j4FaOa'],
                                     '01010011 01101111 01110110 00110011 01000111 01010011 01110101 01111000 '
                                     '01101111 01101101 01100111 00110000 00111001 01011001 00110010 01011010 '
                                     '01110101 01001000 01100101 01001010'), 'Sov3GSuxomg09Y2ZuHeJ')

        self.assertEqual(decode_pass(['b46U1kgHg', '8rGFhpCifNUrJ9', '4kqzlCN3dFV2', 'SPuIZvCgvG99bgOtRv',
                                      'e1IcR0Ss', 'mJiAc1uK85ZHs', '4hn5h4KRVpoS9GOFNp', 'Y9b2LJLkYtDgYpGavW'],
                                     '00110100 01101000 01101110 00110101 01101000 00110100 01001011 01010010 '
                                     '01010110 01110000 01101111 01010011 00111001 01000111 01001111 01000110 '
                                     '01001110 01110000'), '4hn5h4KRVpoS9GOFNp')

        self.assertEqual(decode_pass(['zf8lZ8ek9apmoh9VWeeU', 'tIkBkqyMd9IaELzs', 'icHpUwTZWf'],
                                     '00110000 01111000 01011010 00110100 00110000 01101100 01101000 01100101 '
                                     '01000010'), False)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
