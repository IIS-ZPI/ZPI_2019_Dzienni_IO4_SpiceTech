import unittest
import sys
sys.path.append("./src/")
import read_currency

class MainTest(unittest.TestCase):


    def test_read_currency(self):
        a = ["USD", "GBP"]
        b = ["PL", "NIS"]

        for i in a:
            read_currency.input = lambda _: i
            self.assertEqual(read_currency.read_currency(a, b), (i, "A"))

        for i in b:
            read_currency.input = lambda _: i
            self.assertEqual(read_currency.read_currency(a, b), (i, "B"))


if __name__ == '__main__':
    unittest.main()
