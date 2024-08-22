#!/usr/bin/env python3
"""1. Simple pagination"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """return the appropiate page of the dataset"""
        assert isinstance(
            page, int) and page > 0, "Page must be a postive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be \
                                                a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index < len(dataset):
            return dataset[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        assert isinstance(
            page, int) and page > 0, "Page must be a postive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be \
                                                a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        if start_index < total_items:
            return dict(page_size=page_size,
                        page=page,
                        data=dataset[start_index:end_index],
                        next_page=next_page,
                        prev_page=prev_page,
                        total_pages=total_pages)
        else:
            page_size_value = page_size if page_size > len(dataset) else 0
            return dict(
                page_size=page_size_value,
                page=page,
                data=[],
                next_page=next_page,
                prev_page=prev_page,
                total_pages=total_pages)
