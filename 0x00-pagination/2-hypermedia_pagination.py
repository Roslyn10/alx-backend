#!/usr/bin/env python3
"""Pagination script for Popular Baby Names Dataset"""


import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a subset of items corresponding to the specified page"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a subset of data corresponding to a specific page
        number and size

        Return:
            A list of lists representing the rows of the dataset for
            the specified page
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves paginated data with additional pagination megadata

        Returns:
            - Dict: A dictionary containing the following keys:
            - 'page_size': The number of items on the current page.
            - 'page': The current page number.
            - 'data': A list of items on the current page.
            - 'next_page': The next page number if there are more pages, otherwise None.
            - 'prev_page': The previous page number if the current page is not the first page, otherwise None.
            - 'total_pages': The total number of pages based on the dataset size and page size.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
                'page_size': len(page_data),
                'page': page,
                'data': page_data,
                'next_page': page + 1 if end < len(self.__dataset) else None,
                'prev_page': page - 1 if start > 0 else None,
                'total_pages': total_pages
                }
        return page_info
