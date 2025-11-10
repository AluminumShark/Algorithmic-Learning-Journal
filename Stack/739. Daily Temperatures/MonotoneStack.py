class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0 for _ in range(n)]
        
        for i in range(n):
            while stack and  temperatures[i] > temperatures[stack[-1]]:
                 index = stack.pop()
                 ans[index] = i - index
            stack.append(i)
        
        return ans