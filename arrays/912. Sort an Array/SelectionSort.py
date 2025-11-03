class Solution:
    """
    Selection Sort (Demonstration Only — TLE on LeetCode 912)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Outer loop: iterate over each position in the array
        for i in range(n - 1):
            # Assume the current index has the minimum element
            min_idx = i

            # Inner loop: find the index of the smallest element in the remaining array
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j  # Update min index if a smaller element is found

            # Swap only if a smaller element was found
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]

        # Return the sorted array
        return nums
