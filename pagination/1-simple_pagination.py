#!/usr/bin/env python3
"""simple func for pagination"""
from typing import Tuple
import csv
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for the given page and page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for the
               range of items to be retrieved.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """method retrieves page from dataset"""
        assert isinstance(page, int) and page > 0, \
            "Page have to be positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive number."

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        return dataset[start:end]