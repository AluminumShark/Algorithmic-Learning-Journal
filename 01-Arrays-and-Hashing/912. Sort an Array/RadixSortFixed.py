from typing import List

class Solution:
    """
    Radix Sort (handles both negative and non-negative integers)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        # Separate negatives and non-negatives
        negatives = [-num for num in nums if num < 0]
        non_negatives = [num for num in nums if num >= 0]

        # Sort both parts using radix sort
        sorted_neg = self.radixSort(negatives)
        sorted_nonneg = self.radixSort(non_negatives)

        # Reverse negatives (since -10 < -2)
        sorted_neg = [-num for num in reversed(sorted_neg)]

        # Combine negative and non-negative results
        return sorted_neg + sorted_nonneg

    def radixSort(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        max_val = max(nums)
        exp = 1  # Current digit place (1, 10, 100, ...)

        # Perform counting sort for each digit position
        while max_val // exp > 0:
            self.countingSortByDigit(nums, exp)
            exp *= 10

        return nums

    def countingSortByDigit(self, nums: List[int], exp: int) -> None:
        n = len(nums)
        output = [0] * n
        count = [0] * 10  # Base 10 digits (0-9)

        # Count occurrences of each digit
        for num in nums:
            index = (num // exp) % 10
            count[index] += 1

        # Prefix sum to make it cumulative
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array (stable)
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            output[count[index] - 1] = nums[i]
            count[index] -= 1

        # Copy back to nums
        for i in range(n):
            nums[i] = output[i]
