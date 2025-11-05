import random
from typing import List

class Solution:
    """
    Quick Sort (classic two-pointer partition)
    NOTE: This in-place version may TLE on LC 912 due to bad splits
          (e.g., many duplicate values or nearly sorted arrays).
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, arr: List[int], start: int, end: int) -> List[int]:
        # Base case: subarray of length 0 or 1 is already sorted
        if start >= end:
            return arr

        # 1) Choose a random pivot to mitigate ordered-input worst cases
        pivot_idx = random.randint(start, end)
        pivot_val = arr[pivot_idx]

        # 2) Move pivot to the front
        arr[start], arr[pivot_idx] = arr[pivot_idx], arr[start]

        # 3) Two-pointer scan to partition elements around the pivot
        left = start + 1
        right = end

        # Hoare-style partition with two cursors
        while True:
            # Move left forward while elements <= pivot
            while left <= right and arr[left] <= pivot_val:
                left += 1
            # Move right backward while elements >= pivot
            while left <= right and arr[right] >= pivot_val:
                right -= 1

            # If pointers cross, stop scanning
            if left > right:
                break

            # Swap mis-ordered pair
            arr[left], arr[right] = arr[right], arr[left]

        # 4) Place pivot into its final position
        arr[start], arr[right] = arr[right], arr[start]

        # 5) Recursively sort the two partitions
        self.quickSort(arr, start, right - 1)
        self.quickSort(arr, right + 1, end)

        return arr
