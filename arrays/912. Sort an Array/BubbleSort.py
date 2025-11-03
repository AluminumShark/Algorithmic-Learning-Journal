class Solution:
    """
    Bubble Sort (Demonstration Only — TLE on LeetCode 912)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Outer loop: run n times (each pass places one element in correct position)
        for i in range(n):
            swapped = False  # Track whether any swap happened in this pass

            # Inner loop: compare adjacent elements up to the unsorted part
            for j in range(0, n - i - 1):
                # If current element is greater than the next one, swap them
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True  # A swap occurred

            # Optimization: if no swaps were made, array is already sorted
            if not swapped:
                break

        # Return the sorted array
        return nums
