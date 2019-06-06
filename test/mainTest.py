import unittest
import sys
from dateutil.relativedelta import relativedelta
import datetime
sys.path.append("../src/")
import read_period

class MainTest(unittest.TestCase):

    def test_read_period(self):
        read_period.input = lambda _: "10"
        self.assertEqual(read_period.read_period(), None)
        read_period.input = lambda _: "1"

        rel = relativedelta(days=7)
        self.assertEqual(read_period.read_period(), datetime.datetime.now().date() - rel)
if __name__ == '__main__':
    unittest.main()
