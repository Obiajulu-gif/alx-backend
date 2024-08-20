#!/usr/bin/python3
"""0. Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherit fro the BaseCaching.
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
