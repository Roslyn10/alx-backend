#!/usr/bin/env python3
"""A Basic class that inherts from BaseCaching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A Class that Inherits from BAseCahching and is a caching system
    """
    def put(self, key, item):
        """
        Adds an item to the cache

        Args:
            key (str): The key under which the item will be stored
            item (any): The item to be stored in the cache
        """
        if key is not None and item is not None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache

        Args:
            key (str): The key of the item to retrive.

        Returns:
            any: The item associated with the key,
            or None if the key does not exist or is None.
        """
        if key is not None and key in self.cache_datakeys():
            return self.cache_data[key]
        else:
            return None
