import unittest
import calc



class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add_(1,2), 3)
        self.assertEqual(calc.add_(-1,2), 2)
        self.assertEqual(calc.add_(-1,-2), -3)
        
        
        
if __name__ == "__main__":
    unittest.main()
        