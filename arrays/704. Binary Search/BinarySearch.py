from typing import List

class Solution:
    """
    Binary Search (Iterative implementation)
    Finds target in a sorted array in O(log n) time.
    """

    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers defining the current search range
        left, right = 0, len(nums) - 1

        # Continue until the range is empty
        while left <= right:
            # Compute the middle index — use (left + (right - left) // 2)
            # instead of (left + right) // 2 to avoid potential integer overflow
            mid = left + (right - left) // 2
            
            # Case 1: Found the target
            if nums[mid] == target:
                return mid
            # Case 2: Target is larger, search in the right half
            elif nums[mid] < target:
                left = mid + 1
            # Case 3: Target is smaller, search in the left half
            else:
                right = mid - 1

        # Target not found
        return -1
