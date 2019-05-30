import unittest2 as unittest
import sys
sys.path.append("./src/")

class MainTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True,True)

if __name__ == '__main__':
    unittest.main()
