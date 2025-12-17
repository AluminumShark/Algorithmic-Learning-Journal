from typing import List

class Solution:
    """
    Largest Rectangle in Histogram
    Find the largest rectangular area using monotonic stack.
    """
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append 0 to force all remaining bars to be processed
        heights.append(0)
        stack = []  # Stack stores indices
        ans = 0
        
        for i, cur in enumerate(heights):
            # While current bar is shorter than stack top
            while stack and heights[stack[-1]] > cur:
                # Pop and calculate area with popped bar as height
                h = heights[stack.pop()]
                
                # Left boundary is the new stack top (or -1 if empty)
                left = stack[-1] if stack else -1
                
                # Width: from (left + 1) to (i - 1)
                width = (i - 1) - (left + 1) + 1  # Simplifies to: i - left - 1
                
                ans = max(ans, h * width)
            
            stack.append(i)
        
        return ans

