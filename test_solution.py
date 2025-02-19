# test_solution.py
import unittest
from solution import Solution

class TestMinCostClimbingStairs(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        cost = [10, 15, 20]
        expected = 15
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, expected)

    def test_case_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected = 6
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, expected)

    def test_case_3(self):
        cost = [0, 0, 0, 0]
        expected = 0
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, expected)

    def test_case_4(self):
        cost = [10, 15, 20, 25]
        expected = 30
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
