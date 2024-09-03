#!/usr/bin/env python3
"""A class that inherits from BaseCaching"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """A LRU (Least Recently Used) caching system."""

    def __init__(self):
        """Initializes the cache and the order list to track insertion order"""
        super().__init__()
        self.cache = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using LRU replacement policy

        Args:
            key (str): The key to be added
            item (any): The value associated with the key.
        """
        if key or item is None:
            pass

        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = item

        if len(self.cache) > BaseCaching.MAX_ITEMS:
            least_key = self.cache.popitem(last=False)
            print(f"DISCARD: {least_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any : The value associated with the key,
            or None if the key does not exist.
        """
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]
