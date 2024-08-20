#!/usr/bin/env python3
"""1. FIFO caching"""

from base_caching import BaseCaching


from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign an item to the dictionary self.cache_data
        check if the number of items in self.cache_data
        higher than that of BaseCaching.MAX_ITEMS
        """
        if key is not None or item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        Return the value of self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
