#!/usr/bin/env python3
"""2. LRU caching"""

from base_caching import BaseCaching

from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign an item to the dictionary self.cache_data
        check if the number of items in self.cache_data
        higher than that of BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = next(iter(self.cache_data))
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Return the value of self.cache_data linked to key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
