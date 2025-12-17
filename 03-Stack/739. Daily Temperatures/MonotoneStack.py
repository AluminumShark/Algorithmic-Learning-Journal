from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []                       # Monotonic decreasing stack storing indices
        ans = [0 for _ in range(n)]      # Result array initialized with 0s
        
        for i in range(n):
            # While current temperature is higher than the temperature
            # at the index stored on top of the stack:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                # The difference in indices gives the number of days waited
                ans[index] = i - index
            # Push the current day's index onto the stack
            stack.append(i)
        
        return ans
