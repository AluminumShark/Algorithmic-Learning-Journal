from typing import List

# Time: O(log n)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1

