from typing import List

# Solution 1: Dynamic Programming
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # left[i] = max height from left up to index i
        left = [0] * n
        # right[i] = max height from right up to index i
        right = [0] * n
        
        maxLeft, maxRight = height[0], height[n - 1]
        
        # Build left max array
        for L in range(1, n):
            maxLeft = max(maxLeft, height[L])
            water = maxLeft - height[L]
            left[L] = water
        
        # Build right max array
        for R in range(n - 2, -1, -1):
            maxRight = max(maxRight, height[R])
            water = maxRight - height[R]
            right[R] = water
        
        # Calculate total water
        ans = 0
        for i in range(n):
            ans += min(left[i], right[i])
        
        return ans


# Solution 2: Two Pointers (Space Optimized)
class SolutionTwoPointers:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L, R = 0, n - 1
        maxLeft, maxRight = 0, 0
        ans = 0
        
        while L < R:
            maxLeft = max(maxLeft, height[L])
            maxRight = max(maxRight, height[R])
            
            # Water level is determined by the lower max
            if maxLeft <= maxRight:
                ans += maxLeft - height[L]
                L += 1
            else:
                ans += maxRight - height[R]
                R -= 1
        
        return ans

