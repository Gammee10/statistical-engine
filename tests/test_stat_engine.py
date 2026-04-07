import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        data = [1, 2, 3]
        self.assertEqual(StatEngine(data).get_mean(), 2)

    def test_median_even(self):
        data = [1, 2, 3, 4]
        self.assertEqual(StatEngine(data).get_median(), 2.5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            StatEngine([])

if __name__ == "__main__":
    unittest.main()