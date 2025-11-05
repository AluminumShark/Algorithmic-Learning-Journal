from typing import List
import random

class Solution:
    """
    Pythonic Quick Sort (non in-place, very readable)
    NOTE: Uses extra lists; easy to understand but creates many arrays,
          which increases time & memory and often TLE on LC 912.
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums)

    def quickSort(self, arr: List[int]) -> List[int]:
        # Base case
        if len(arr) <= 1:
            return arr

        # Randomized pivot to mitigate worst-case for ordered inputs
        pivot_idx = random.randint(0, len(arr) - 1)
        pivot_val = arr[pivot_idx]

        # Partition into three lists: < pivot, == pivot, > pivot
        less = [x for x in arr if x <  pivot_val]
        equal = [x for x in arr if x == pivot_val]
        greater = [x for x in arr if x >  pivot_val]

        # Recursively sort sublists and concatenate
        return self.quickSort(less) + equal + self.quickSort(greater)
