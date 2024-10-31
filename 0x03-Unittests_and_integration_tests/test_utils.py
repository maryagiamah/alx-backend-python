#!/usr/bin/env python3
"""write the first unit test for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test Access_Map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """AsserIfEqual"""
        self.assertEqual(access_nested_map(nested_map, path), result)
