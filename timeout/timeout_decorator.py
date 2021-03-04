import multiprocessing
import typing


class TimeoutException(Exception):
    def __init__(self, function_name: str, duration: typing.Union[float, int]):
        self._function_name = function_name
        self._duration = duration

    def __str__(self) -> str:
        return f'{self._function_name} - Timed out after {self._duration} seconds'


class _FunctionProcess(multiprocessing.Process):
    def __init__(self, function: typing.Callable, *args, **kwargs):
        self._queue = multiprocessing.Queue(maxsize=1)
        self._func_name: str = function.__name__
        args = (function,) + args
        super().__init__(target=self._run_function, args=args, kwargs=kwargs)

    def _run_function(self, function: typing.Callable, *args, **kwargs):
        try:
            result = function(*args, **kwargs)
            self._queue.put((True, result))
        except Exception as e:
            self._queue.put((False, e))

    def done(self):
        return self._queue.full()

    def result(self):
        return self._queue.get()

    @property
    def function_name(self) -> str:
        return self._func_name


def timeout(duration: typing.Union[int, float], force_kill: bool = True):
    def wrapper(function: typing.Callable):
        def inner(*args, **kwargs):
            process = _FunctionProcess(function, *args, **kwargs)
            process.start()
            process.join(duration)
            if process.is_alive():
                if force_kill is True:
                    process.terminate()
                raise TimeoutException(function_name=process.function_name, duration=duration)
            assert process.done()
            success, result = process.result()
            if success:
                return result
            else:
                raise result

        return inner

    return wrapper
