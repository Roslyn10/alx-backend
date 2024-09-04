#!/usr/bin/env python3
"""A LRU class that inherits from BaseCaching"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """A LRU (Least Recently Used) caching system."""

    def __init__(self):
        """Initializes the cache with an OrderedDict"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using LRU replacement policy

        Args:
            key (str): The key to be added
            item (any): The value associated with the key.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {least_key}")
        else:

            self.cache_data.pop(key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any : The value associated with the key,
            or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
