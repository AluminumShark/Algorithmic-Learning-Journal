from typing import List

# Solution 1: Basic Hash Map (Two-Pass)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapping = {}
        for i in range(n):
            diff = target - nums[i]
            mapping[diff] = (i, nums[i])
        for i in range(n):
            if nums[i] in mapping:
                idx1, _ = mapping[nums[i]]
                idx2 = i
                if idx1 != idx2:
                    return sorted([idx1, idx2])


# Solution 2: Optimized One-Pass Hash Map
class SolutionOnePass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                return [i, mapping[diff]]
            mapping[n] = i

