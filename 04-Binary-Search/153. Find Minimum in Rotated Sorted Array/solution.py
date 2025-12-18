from typing import List

# Solution 1: Binary Search (Compare with Right Boundary)
# Time: O(log n)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            # Compare mid with Right to find the pivot direction
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[L]

