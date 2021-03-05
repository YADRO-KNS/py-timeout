"""
Unit tests for "timeout.timeout_decorator._FunctionProcess" class
"""

import multiprocessing
import unittest
from unittest.mock import Mock

from timeout.timeout_decorator import _FunctionProcess


class TestFunctionProcessClass(unittest.TestCase):
    """
    Unit tests for "_FunctionProcess" class
    """
    def test_subclass_of_process(self):
        """
        Tests that "_FunctionProcess" class is a subclass
        of "multiprocessing.Process"
        """
        ### Assertions ###

        self.assertIs(_FunctionProcess.__base__, multiprocessing.Process)


class TestFunctionProcess(unittest.TestCase):
    """
    Base class for "_FunctionProcess" tests
    """
    def setUp(self) -> None:
        self.function = Mock(__name__='some name')
        self.arg = 'some argument'
        self.kwargs = {'key1': 'value1', 'key2': 'value2'}
        self.function_process = _FunctionProcess(self.function, self.arg, **self.kwargs)


class TestInit(TestFunctionProcess):
    """
    Unit tests for "_FunctionProcess.__init__" method
    """
    def test_instance_attrs(self):
        """
        Tests instance attributes values
        """
        self.assertTrue(isinstance(self.function_process._queue, multiprocessing.queues.Queue))
        self.assertEqual(1, self.function_process._queue._maxsize)
        self.assertEqual(self.function.__name__, self.function_process._func_name)

    def test_superclass_init(self):
        """
        Tests attributes of superclass after initialization
        """
        self.assertEqual(self.function_process._run_function.__name__, self.function_process._target.__name__)
        self.assertEqual(self.function, self.function_process._args[0])
        self.assertEqual(self.arg, self.function_process._args[1])
        self.assertEqual(self.kwargs, self.function_process._kwargs)


class TestRunFunction(TestFunctionProcess):
    """
    Unit tests for "_FunctionProcess._run_function" method
    """
    def test_successful_execution(self):
        """
        Tests execution without exceptions
        """
        self.function_process._queue.put = Mock()
        args = ('args1', 'args2')
        kwargs = {'key1': 'value1', 'key2': 'value2'}
        function = Mock()

        self.function_process._run_function(function, *args, **kwargs)

        function.assert_called_once_with(*args, **kwargs)
        self.function_process._queue.put.assert_called_once_with((True, function.return_value))

    def test_failed_execution(self):
        """
        Tests execution with exception
        """
        class TestException(Exception):
            def __new__(cls):
                if not hasattr(cls, 'instance'):
                    cls.instance = super(TestException, cls).__new__(cls)
                return cls.instance

        self.function_process._queue.put = Mock()
        args = ('args1', 'args2')
        kwargs = {'key1': 'value1', 'key2': 'value2'}
        function = Mock(side_effect=TestException)

        self.function_process._run_function(function, *args, **kwargs)

        function.assert_called_once_with(*args, **kwargs)
        self.function_process._queue.put.assert_called_once_with((False, TestException()))


class TestDone(TestFunctionProcess):
    """
    Unit tests for "_FunctionProcess.done" method
    """
    def test_returns_true_if_queue_is_full(self):
        """
        Tests that if "_queue" is full
        True is returned
        """
        self.function_process._queue.put('something')

        result = self.function_process.done()

        self.assertIs(result, True)

    def test_returns_false_if_queue_is_empty(self):
        """
        Tests that if "_queue" is empty
        False is returned
        """
        self.assertTrue(self.function_process._queue.empty())

        result = self.function_process.done()

        self.assertIs(result, False)


class TestResult(TestFunctionProcess):
    """
    Unit tests for "_FunctionProcess.result" method
    """
    def test_returns_item_from_queue(self):
        """
        Tests that item that has been put
        in the queue is returned
        """
        item = 'item'
        self.function_process._queue.put(item)

        result = self.function_process.result()

        self.assertEqual(result, item)


class TestFunctionName(TestFunctionProcess):
    """
    Unit tests for "_FunctionProcess.function_name" method
    """
    def test_returns_function_name(self):
        """
        Tests that name of the function that
        has been passed during initialization
        is returned
        """
        result = self.function_process.function_name

        self.assertEqual(self.function.__name__, result)
