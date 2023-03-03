import unittest
import random

from sort import insertion_sort, merge_sort, merge


class TestInsertionSort(unittest.TestCase):
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_random_element_sort(self):
        arr = [1, 2, 3, 4, 5]
        random.shuffle(arr)
        insertion_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])


class TestMerge(unittest.TestCase):
    def test_1(self):
        arr = [1, 5, 2, 7]
        merge(arr, 0, 1, 3)
        self.assertListEqual(arr, [1, 2, 5, 7])

    def test_2(self):
        arr = [1, 3, 15, 12, 10, 16, 2, 9]
        merge(arr, 4, 5, 7)
        self.assertListEqual(arr, [1, 3, 15, 12, 2, 9, 10, 16])


class TestMergeSort(unittest.TestCase):
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        p = 0
        r = len(arr) - 1
        merge_sort(arr, p, r)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        p = 0
        r = len(arr) - 1
        merge_sort(arr, p, r)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_random_element_sort(self):
        arr = [1, 2, 3, 4, 5]
        p = 0
        r = len(arr) - 1
        random.shuffle(arr)
        merge_sort(arr, p, r)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])
