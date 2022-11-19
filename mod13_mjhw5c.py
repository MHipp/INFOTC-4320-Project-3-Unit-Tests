# unit tests for stock visualizer

import datetime
import unittest

userSymbol = "AAPL"
chartType = 1
timeSeries = 1
startDate = "2000-01-01"
endDate = "2008-12-31"

class TestStockVisualizer(unittest.TestCase):
    def test_stock_visualizer_input1(self):
        # test that input 1 is a string
        self.assertEqual(type(userSymbol), str)
    def test_stock_visualizer_input2(self):
        # test that input 2 is an integer
        self.assertEqual(type(chartType), int)
    def test_stock_visualizer_input3(self):
        # test that input 3 is an integer
        self.assertEqual(type(timeSeries), int)
    def test_stock_visualizer_input4(self):
        # test that input 4 is a valid date
        try:
            # check that input 4 is a valid date
            checkStartDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        # if input 4 is not a valid date, fail the test
        except ValueError:
            self.fail("Incorrect date format, the format should be YYYY-MM-DD")
    def test_stock_visualizer_input5(self):
        # test that input 5 is a date later than input 4
        try:
            # check that input 4 is a valid date
            checkStartDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
            # check that input 5 is a valid date
            checkEndDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
            # check that input 5 is later than input 4
            if checkStartDate > checkEndDate:
                self.fail("The end date cannot begin before the start date")
        # if input 5 is not a valid date, fail the test
        except ValueError:
            self.fail("Incorrect date format, the format should be YYYY-MM-DD")

# run the unit tests
if __name__ == '__main__':
    unittest.main()

