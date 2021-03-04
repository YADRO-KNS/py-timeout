"""
Unit tests for "timeout.timeout" decorator function
"""
import time
import unittest

from timeout import timeout, TimeoutException


class TestTimeout(unittest.TestCase):

    @timeout(duration=0.5)
    def blocking_function(self):
        while True:
            time.sleep(1)

    @timeout(duration=0.5)
    def not_blocking_function(self, a, b):
        time.sleep(0.1)
        return a / b

    def test_terminates_blocking_function(self):
        """
        Tests that if some function does not return
        result before timeout is exceeded, process
        with the function is being terminated and
        TimeoutException is raised
        """

        expected_msg = 'blocking_function - Timed out after 0.5 seconds'

        with self.assertRaises(TimeoutException) as context:
            self.blocking_function()

        self.assertEqual(expected_msg, str(context.exception))

    def test_returns_function_execution_result(self):
        """
        Tests that result of wrapped function
        execution is returned
        """
        a = 100
        b = 25
        expected = a / b

        result = self.not_blocking_function(a, b=b)

        self.assertEqual(expected, result)

    def test_reraises_exception(self):
        """
        Tests that if exception happens in wrapped
        function it's being reraised
        """
        with self.assertRaises(ZeroDivisionError):
            self.not_blocking_function(1, 0)


