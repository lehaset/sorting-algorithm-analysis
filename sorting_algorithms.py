import sys
from abc import ABC, abstractmethod

# Increase recursion limit for large lists
sys.setrecursionlimit(50000)

class SortingAlgorithm(ABC):
    def __init__(self):
        self.comparisons = 0

    @abstractmethod
    def sort_timing(self, arr):
        pass

    @abstractmethod
    def sort_counting(self, arr):
        pass

    def reset_comparisons(self):
        self.comparisons = 0

class InsertionSort(SortingAlgorithm):
    name = "Insertion Sort"

    def sort_timing(self, arr):
        arr_copy = arr.copy()
        for i in range(1, len(arr_copy)):
            key = arr_copy[i]
            j = i - 1
            while j >= 0 and arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
            arr_copy[j + 1] = key
        return arr_copy

    def sort_counting(self, arr):
        arr_copy = arr.copy()
        self.comparisons = 0
        for i in range(1, len(arr_copy)):
            key = arr_copy[i]
            j = i - 1
            while j >= 0 and arr_copy[j] > key:
                self.comparisons += 1
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
            if j >= 0:
                self.comparisons += 1
            arr_copy[j + 1] = key
        return arr_copy

class QuickSort(SortingAlgorithm):
    name = "Quick Sort"

    def sort_timing(self, arr):
        arr_copy = arr.copy()
        self._quick_sort_timing(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    def sort_counting(self, arr):
        arr_copy = arr.copy()
        self.comparisons = 0
        self._quick_sort_counting(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    def _quick_sort_timing(self, arr, low, high):
        if low < high:
            pi = self._partition_timing(arr, low, high)
            self._quick_sort_timing(arr, low, pi - 1)
            self._quick_sort_timing(arr, pi + 1, high)

    def _partition_timing(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort_counting(self, arr, low, high):
        if low < high:
            pi = self._partition_counting(arr, low, high)
            self._quick_sort_counting(arr, low, pi - 1)
            self._quick_sort_counting(arr, pi + 1, high)

    def _partition_counting(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1  
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

class MergeSort(SortingAlgorithm):
    name = "Merge Sort"

    def sort_timing(self, arr):
        arr_copy = arr.copy()
        self._merge_sort_timing(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    def sort_counting(self, arr):
        arr_copy = arr.copy()
        self.comparisons = 0
        self._merge_sort_counting(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    def _merge_sort_timing(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort_timing(arr, left, mid)
            self._merge_sort_timing(arr, mid + 1, right)
            self._merge_timing(arr, left, mid, right)

    def _merge_timing(self, arr, left, mid, right):
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    def _merge_sort_counting(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort_counting(arr, left, mid)
            self._merge_sort_counting(arr, mid + 1, right)
            self._merge_counting(arr, left, mid, right)

    def _merge_counting(self, arr, left, mid, right):
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_half) and j < len(right_half):
            self.comparisons += 1
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1