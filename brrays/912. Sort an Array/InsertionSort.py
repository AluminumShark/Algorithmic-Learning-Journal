from typing import List

class Solution:
    """
    Insertion Sort (Demonstration Only — TLE on LeetCode 912)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        # Start from the second element (index 1)
        for i in range(1, len(nums)):
            temp = nums[i]   # The element to be inserted
            j = i

            # Shift elements of the sorted portion that are greater than temp
            while j > 0 and nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1

            # Insert the element into its correct position
            nums[j] = temp

        return nums
