import random
from typing import List

class Solution:
    """
    Quick Sort (Hoare partition, may TLE on worst cases for LC 912)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums: List[int], low_index: int, high_index: int) -> List[int]:
        # Recursively sort subarrays defined by [low_index, high_index]
        if low_index < high_index:
            pivot_index = self.randomPartition(nums, low_index, high_index)
            # Recurse on left side
            self.quickSort(nums, low_index, pivot_index - 1)
            # Recurse on right side
            self.quickSort(nums, pivot_index + 1, high_index)
        return nums

    def randomPartition(self, nums: List[int], low_index: int, high_index: int) -> int:
        # Randomize pivot to reduce chance of worst-case on ordered inputs
        i = random.randint(low_index, high_index)
        nums[i], nums[low_index] = nums[low_index], nums[i]
        return self.partition(nums, low_index, high_index)

    def partition(self, nums: List[int], low_index: int, high_index: int) -> int:
        """
        Hoare partition scheme:
        - Choose pivot = nums[low_index]
        - Move two pointers toward each other and swap out-of-place elements
        - Return final pivot position
        NOTE: To avoid stalling on many duplicates, use STRICT comparisons inside loops:
              nums[left_index] < pivot   and   nums[right_index] > pivot
        """
        pivot = nums[low_index]
        left_index, right_index = low_index - 1, high_index + 1

        while True:
            # Move left_index rightward until element >= pivot is found
            # Using strict '< pivot' prevents infinite loops on duplicates
            left_index += 1
            while nums[left_index] < pivot:
                left_index += 1

            # Move right_index leftward until element <= pivot is found
            # Using strict '> pivot' prevents stalling on duplicates
            right_index -= 1
            while nums[right_index] > pivot:
                right_index -= 1

            if left_index >= right_index:
                # right_index is the final index where pivot can be considered placed
                return right_index

            # Swap out-of-place elements
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
