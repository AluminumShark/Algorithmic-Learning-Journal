from typing import List

class Solution:
    """
    Radix Sort (base-10, only works for non-negative integers)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.radixSort(nums)

    def radixSort(self, nums: List[int]) -> List[int]:
        # Find the number of digits in the maximum value
        size = len(str(max(nums)))

        # Process digits from least significant (i=0) to most significant
        for i in range(size):
            # Create 10 buckets (for digits 0-9)
            buckets = [[] for _ in range(10)]

            # Group numbers based on the current digit
            for num in nums:
                digit = (num // (10 ** i)) % 10
                buckets[digit].append(num)

            # Recombine buckets into nums
            nums.clear()
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)

        return nums
