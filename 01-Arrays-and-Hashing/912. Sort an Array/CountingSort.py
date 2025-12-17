from typing import List

class Solution:
    """
    Counting Sort (Linear-time integer sorting)
    Efficient for small integer ranges — Accepted on LeetCode 912
    """

    def countingSort(self, nums: List[int]) -> List[int]:
        # 1. Find min and max values to determine range of input
        numsMax, numsMin = max(nums), min(nums)
        size = numsMax - numsMin + 1

        # 2. Initialize the counting array (frequency of each value)
        counts = [0 for _ in range(size)]

        # 3. Count occurrences of each number
        for num in nums:
            counts[num - numsMin] += 1

        # 4. Accumulate counts — each position stores #elements <= current value
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        # 5. Build the sorted result (stable)
        result = [0 for _ in range(len(nums))]

        # Iterate backwards to maintain stability
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            result[counts[num - numsMin] - 1] = num
            counts[num - numsMin] -= 1
        
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.countingSort(nums)
