"""
Unit tests for "timeout.TimeoutException" class
"""

import unittest

from timeout import TimeoutException


class TestTimeoutExceptionClass(unittest.TestCase):
    """
    Unit tests for "TimeoutException" class
    """
    def test_subclass_of_exception(self):
        """
        Tests that "TimeoutException" class
        is a subclass of "Exception"
        """
        ### Assertions ###

        self.assertIs(TimeoutException.__base__, Exception)


class TestTimeoutExceptionInstance(unittest.TestCase):
    """
    Unit tests for "TimeoutException" instance
    """
    def setUp(self) -> None:
        self.func_name = 'some function'
        self.duration = 123
        self.exception = TimeoutException(function_name=self.func_name, duration=self.duration)

    def test_instance_attrs(self):
        """
        Tests that "TimeoutException" instance
        attributes values
        """
        ### Assertions ###

        self.assertEqual(self.func_name, self.exception._function_name)
        self.assertEqual(self.duration, self.exception._duration)

    def test_str_method(self):
        """
        Tests that formatted string with
        function name and timeout duration
        is returned
        """
        expected = f'{self.func_name} - Timed out after {self.duration} seconds'

        self.assertEqual(expected, self.exception.__str__())
