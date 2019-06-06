import unittest
import sys
import datetime
sys.path.append("./src/")
import get_period_data

class MainTest(unittest.TestCase):

    def test_get_period_data(self):
        period = datetime.datetime.now().date()
        table_code = "A"
        currency_code = "USD"
        self.assertGreater(len(get_period_data.get_period_data(period, table_code, currency_code)), 0)

        table_code = "B"
        self.assertEqual(len(get_period_data.get_period_data(period, table_code, currency_code)), 0)


if __name__ == '__main__':
    unittest.main()
