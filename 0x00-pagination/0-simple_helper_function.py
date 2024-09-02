#!/usr/bin/env python3
"""Paginate data using lists"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a subset of items corresponding to the specified page"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
