#!/usr/bin/env python3
"""write the first unit test for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import *
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Use the assertRaises context manager to test that a KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """implement the TestGetJson.test_get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Mocks get_json results"""
        mock_get.return_value.json.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """with a test_memoize method"""

    def test_memoize(self):
        """test memoize"""

        class TestClass:
            """memoize_test_class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """return a_method"""
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, 'a_method') as mock_obj:
            mock_obj.return_value = 42

            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mock_obj.assert_called_once()
