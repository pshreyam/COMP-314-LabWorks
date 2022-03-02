import unittest

from search import linear_search, binary_search


class TestCase(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear_search([1, 3, 2, 4, 5], 3)["result"], 1)
        self.assertEqual(linear_search([1, 3, 2, 4, 5], 4)["result"], 3)
        self.assertEqual(linear_search([1, 3, 2, 4, 5], 10)["result"], -1)
        self.assertEqual(linear_search([1, 3, 2, 4, 5], 10)["result"], -1)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3)["result"], 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5)["result"], 4)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 20)["result"], -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0)["result"], -1)
