#!/usr/bin/env python3

"""
module containing the following objects:
    1. class `Cache`
    2. method `get`
    3. method `get_int`
    4. method `get_str`
    5. function `count calls`
"""

import redis
from functools import wraps
from typing import Any, Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    creates and returns a function that increments the count for that key
        every time the method is called and returns the value returned by
        the original method
    args:   method: Callable
    return: count_calls_wrapper: Callable
    """
    @wraps(method)
    def count_calls_wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        key: str = method.__qualname__
        self._redis.incr(key)
        wrap = method(self, *args, **kwargs)
        return (wrap)
    return count_calls_wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs for a particular function
        everytime the original function is called, it adds the input parameters
        to one list in redis, and store its output into another list
    args:   method: Callable
    return: count_calls_wrapper: Callable
    """
    @wraps(method)
    def call_history_wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        key: str = method.__qualname__
        input_key: str = f"{key}:inputs"
        output_key: str = f"{key}:outputs"
        self._redis.rpush(input_key, str(args))
        history = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(history))
        return (history)
    return (call_history_wrapper)


class Cache():
    """
    methods:
        __self__
        store
        get
        get_int
        get_str
    """

    def __init__(self) -> None:
        """
        stores an instance of the Redis client as private variable `_redis`
        flushes the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random key using `uuid` and stores the input data in Redis
        args:   data: Union[str, bytes, int, float])
        return: key: str
        """
        random_key: str = str(uuid4())
        self._redis.set(random_key, data)
        return (random_key)

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float, None]:
        """
        converts data to the desired format
        args:   key: str
                fn: Optional[Callable]
        return: value: Union[str, bytes, int, float, None]
        """
        value = self._redis.get(key)
        if (value):
            if (fn):
                value = fn(value)
            return (value)
        else:
            return (None)

    def get_int(self, value: bytes) -> int:
        """
        parametrizes Cache.get with the correct conversion function
        args:   value: bytes
        return: value_int: int
        """
        value_int: int = int(value.decode('utf-8'))
        return (value_int)

    def get_str(self, value: bytes) -> str:
        """
        parametrizes Cache.get with the correct conversion function
        args:   value: bytes
        return: value_str: str
        """
        value_str: str = value.decode('utf-8')
        return (value_str)
