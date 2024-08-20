#!/usr/bin/python3
"""0. Basic dictionary"""


class BaseCaching:
    """
    BaseCaching defines:
        - caching system methods for a caching system
        - data structure for caching (a dictionary called "cache data")
    """

    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache.
        """
        print("Current cache:")
        for key in self.cache_data.keys():
            print("{}: {}".format(key, self.cache_data[key]))


class BasicCache(BaseCaching):
    """
    BasicCache class that inherit fro the BaseCaching
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key
        if key or item is None, this method should
        not do anything
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        if key is None or if the key doesn't exist in self.cache_data,
        return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
