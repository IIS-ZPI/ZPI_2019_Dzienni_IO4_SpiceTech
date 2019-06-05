import unittest
import sys
sys.path.append("./src/")

import read_currency
import read_operation

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

    def test_read_operation(self):
        inp = [str(x) for x in range(0, 10)]
        res = [None, "1", "2", "3", "4", "5", "6", None, None, None]
        for i,r in zip(inp, res):
            read_operation.input = lambda _: i
            self.assertEqual(read_operation.read_operation(), r)

if __name__ == '__main__':
    unittest.main()
