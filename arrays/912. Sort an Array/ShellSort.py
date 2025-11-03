from typing import List

class Solution:
    """
    Shell Sort (Improved Insertion Sort — Accepted on LeetCode 912)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n // 2  # Initial gap size (half of array length)

        # Gradually reduce the gap until it becomes 0
        while gap > 0:
            # Perform gapped insertion sort for each gap value
            for i in range(gap, n):
                temp = nums[i]
                j = i

                # Shift earlier gap-sorted elements to make room for nums[i]
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap

                # Place the element in its correct gap-sorted position
                nums[j] = temp

            # Reduce the gap size (usually by half)
            gap //= 2

        return nums
