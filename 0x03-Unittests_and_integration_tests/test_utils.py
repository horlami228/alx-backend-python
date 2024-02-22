#!/usr/bin/env python3

"""nested map"""
import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unittest class"""

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test function to run"""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a"), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Test with an expection"""
        with self.assertRaises(KeyError) as error:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{exception}')", repr(error.exception))


if __name__ == "__main__":
    unittest.main()
