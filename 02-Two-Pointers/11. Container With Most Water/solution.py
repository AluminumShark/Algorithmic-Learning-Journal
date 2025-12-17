from typing import List

class Solution:
    """
    Container With Most Water
    Find two lines that together with the x-axis forms a container 
    that holds the most water using two pointers.
    """
    
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        L, R = 0, n - 1
        
        while L < R:
            # Calculate water = width × min(height)
            h = min(height[L], height[R])
            width = R - L
            water = width * h
            ans = max(ans, water)
            
            # Move the pointer with smaller height
            # (Moving the taller one can only decrease area)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        
        return ans

