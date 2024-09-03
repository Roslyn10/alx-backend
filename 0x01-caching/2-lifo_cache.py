#!/usr/bin/env python3
"""A class that inherits from BaseCaching"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO (Last In, First Out) caching system."""

    def __init__(self):
        """Initializes the cache and the order list to track insertion order"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO replacement policy

        Args:
            key (str): The key to be added
            item (any): The value associated with the key.
        """
        if key or item is None:
            pass

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest_key = self.order.pop(-2)
            del self.cache_data[newest_key]
            print(f"DISCARD: {newest_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any : The value associated with the key,
            or None if the key does not exist.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
