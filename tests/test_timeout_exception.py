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
        self.args = ('arg1', 'arg2')
        self.kwarg = {'key1': 'value1', 'key2': 'value2'}
        self.duration = 123
        self.exception = TimeoutException(function_name=self.func_name, call_args=self.args,
                                          call_kwargs=self.kwarg, duration=self.duration)

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
        args_str = ', '.join(self.args)
        kwargs_str = ', '.join(f'{k}={v}' for k, v in self.kwarg.items())
        expected = f'{self.func_name}({args_str}, {kwargs_str}) ' \
                   f'- Timed out after {self.duration} seconds'

        self.assertEqual(expected, self.exception.__str__())

