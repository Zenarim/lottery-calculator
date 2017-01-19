import unittest
from check_lottery_tax import lottery_tax

"""
 2017 Federal Tax Bracket
 -------------------------------
 1. 0      to 9325         10%
 2. 9325   to 37950        15%
 3. 37950  to 91900        25%
 4. 91900  to 191650       28%
 5. 191650 to 416700       33%
 6. 416700 to 418400       35%
 7. 418400 to unlimited    39.6%
"""


class TestLotteryTaxCalc(unittest.TestCase):
    def setUp(self):
        self.winnings = {
            "loser": 0,
            "1st_bracket": 5000,
            "2nd_bracket": 19325,
            "3rd_bracket": 50000,
            "4th_bracket": 100000,
            "5th_bracket": 200000,
            "6th_bracket": 417000,
            "7th_bracket": 1000000,
        }

    def test_check_for_negative_winnings(self):
        self.assertRaises(ValueError, lottery_tax, -100)

    def test_first_bracket_zero_income_zero_tax(self):
        expected = 0
        actual = lottery_tax(self.winnings["loser"])
        self.assertEqual(expected, actual)

    def test_first_bracket_5000_income_500_tax(self):
        # 5000 * 0.10 = 500
        expected = 500
        actual = lottery_tax(self.winnings["1st_bracket"])
        self.assertEqual(expected, actual)

    def test_second_bracket_19325_income_2432_5_tax(self):
        # 9325 * 0.10           = 932.5
        # (19325 - 9325) * 0.15 = 1500
        # 932.5 + 1500          = 2432.5
        expected = 2432.5
        actual = lottery_tax(self.winnings["2nd_bracket"])
        self.assertEqual(expected, actual)

    def test_third_bracket_50000_income_9350_tax(self):
        # 9325 * 0.10              = 932.5
        # (37950 - 9325) * 0.15    = 4293.75
        # (50000 - 37950) * 0.25   = 3012.5
        # 932.5 + 4293.75 + 3012.5 = 8238.75
        expected = 8238.75
        actual = lottery_tax(self.winnings["3rd_bracket"])
        self.assertEqual(expected, actual)

    def test_fourth_bracket_100000_income_20981_75_tax(self):
        # 9325 * 0.10             = 932.5
        # (37950 - 9325) * 0.15   = 4293.75
        # (91900 - 37950) * 0.25  = 13487.5
        # (100000 - 91900) * 0.28 = 2268
        # 923.5 + 4293.75 + 13487.5 + 2268 = 20981.75
        expected = 20981.75
        actual = lottery_tax(self.winnings["4th_bracket"])
        self.assertEqual(expected, actual)

    def test_fifth_bracket_200000_income_49449_25_tax(self):
        # 9325 * 0.10              = 932.5
        # (37950 - 9325) * 0.15    = 4293.75
        # (91900 - 37950) * 0.25   = 13487.5
        # (191650 - 91900) * 0.28  = 27930
        # (200000 - 191650) * 0.33 = 2755.5
        # 923.5 + 4293.75 + 13487.5 + 27930 + 2755.5 = 49399.25
        expected = 49399.25
        actual = lottery_tax(self.winnings["5th_bracket"])
        self.assertEqual(expected, actual)

    def test_sixth_bracket_417000_income_121015_25_tax(self):
        # 9325 * 0.10              = 932.5
        # (37950 - 9325) * 0.15    = 4293.75
        # (91900 - 37950) * 0.25   = 13487.5
        # (191650 - 91900) * 0.28  = 27650
        # (416700 - 191650) * 0.33 = 74596.5
        # (417000 - 416700) * 0.35 = 105
        # 923.5 + 4293.75 + 13487.5 + 27930 + 74596.5 + 105 = 121345.25
        expected = 121015.25
        actual = lottery_tax(self.winnings["6th_bracket"])
        self.assertEqual(expected, actual)

    def test_seventh_bracket_1000000_income_tax(self):
        # (9325 * 0.10)                 = 932.5
        # ((37950 - 9325) * 0.15)       = 4293.75
        # ((91900 - 37950) * 0.25)      = 13487.5
        # ((191650 - 91900) * 0.28)     = 27930
        # ((416700 - 191650) * 0.33)    = 74266.5
        # ((418400 - 416700) * 0.35)    = 595
        # ((1000000 - 418400) * 0.396)  = 230313.6
        expected = 351818.85
        actual = lottery_tax(self.winnings["7th_bracket"])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestLotteryTaxCalc("test_sixth_bracket_417000_income_tax"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
