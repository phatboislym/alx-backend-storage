#!/usr/bin/env python3

"""
module containing the following objects:
    1. class `Cache`
"""

import redis
from typing import Union
from uuid import uuid4


class Cache():
    """
    methods:
        __self__
        store
    """

    def __init__(self) -> None:
        """
        stores an instance of the Redis client as private variable `_redis`
        flushes the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random key using `uuid` and stores the input data in Redis
        args: data: Union[str, bytes, int, float])
        return: key: str
        """
        random_key: str = str(uuid4())
        self._redis.set(random_key, data)
        return (random_key)
