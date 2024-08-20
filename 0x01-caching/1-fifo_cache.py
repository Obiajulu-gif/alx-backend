#!/usr/bin/python3
"""1. FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO algorithm for cache
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign an item to the dictionary self.cache_data
        check if the number of items in self.cache_data
        higher than that of BaseCaching.MAX_ITEMS
        """
        if key is not None or item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.key_order.pop(0)
                    del self.cache_data[first_key]
                    print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
            if key not in self.key_order:
                self.key_order.append(key)

    def get(self, key):
        """
        Return the value of self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
