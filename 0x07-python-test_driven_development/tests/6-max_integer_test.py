#!/usr/bin/python3

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_numbers(self):
        result = max_integer([1, 5, 3, 7, 2])
        self.assertEqual(result, 7)

    def test_negative_numbers(self):
        result = max_integer([-1, -5, -3, -7, -2])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 5, 3, -7, 2])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([3, 5, 3, 7, 2])
        self.assertEqual(result, 7)
