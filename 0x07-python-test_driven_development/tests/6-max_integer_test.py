#!/usr/bin/python3

import unittest
from 6-max_integer import max_integer

class TestMaximumInteger(unittest.TestCase):
    def test_maximum_integer_with_none(self):
        result = max_integer(None)
        self.assertEqual(result)

    def test_maximum_integer_with_empty_list(self):
        result = max_integer([])
        self.assertEqual(result)

    def test_maximum_integer_with_list_of_integers(self):
        result = max_integer([1, 2, 3])
        self.assertEqual(result)
