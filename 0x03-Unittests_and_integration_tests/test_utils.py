#!/usr/bin/env python3
"""Test suite for the utils module"""
from typing import Dict, Tuple, Union
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str, ...],
                               expected: Union[Dict, int]):
        """Test that access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str, ...],
                                         exception: Exception):
        """Test that access_nested_map raises the correct exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, expected_payload: Dict):
        """Test that get_json returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = expected_payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(url)
            self.assertEqual(result, expected_payload)
            mock_get.assert_called_once_with(url)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Test that the memoize decorator works as expected"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mocked_method:
            test_instance = TestClass()

            # Call the property twice
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)

            # Check that the underlying method was only called once
            mocked_method.assert_called_once()
