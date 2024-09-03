#!/usr/bin/env python3
"""A FIFOCache that inherits from BaseChaching"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO (First In, First Out) caching system."""

    def __init__(self):
        """Initializes the cache and the order list to track insertion order"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO replacement policy

        Args:
            key (str): The key to be added
            item (any): The value associated with the key.
        """
        if key or item is None:
            pass

        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

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
