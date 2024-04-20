# INFOTC 4320, Module 13, Challenge: Unit Tests in Python

import unittest

class TestProject3Inputs(unittest.TestCase):
    # symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        symbol = "AAPL"
        self.assertEqual(symbol, symbol.upper())
        self.assertRegex(symbol, r'^[A-Z]{1,7}$')

    # chart type: 1 numeric character, 1 or 2
    def test_chart_type(self):
        chart_type = "1"
        self.assertIn(chart_type, ["1", "2"])

    # time series: 1 numeric character, 1 - 4
    def test_time_series(self):
        time_series = "3"
        self.assertRegex(time_series, r'^[1-4]{1}$')

    # start date: date type YYYY-MM-DD
    def test_start_date(self):
        start_date = "2019-12-01"
        self.assertRegex(start_date, r'^\d{4}-\d{2}-\d{2}$')

    # end date: date type YYYY-MM-DD
    def test_end_date(self):
        end_date = "2020-01-25"
        self.assertRegex(end_date, r'^\d{4}-\d{2}-\d{2}$')

if __name__ == '__main__':
    unittest.main()

# unit test results:

# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# OK