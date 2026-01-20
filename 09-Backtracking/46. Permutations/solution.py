# Time: O(n * n!)
# Space: O(n)
# Concept: Backtracking with a `used` array to track availability.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        used = [False] * len(nums)
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                cur.append(nums[i])
                used[i] = True
                dfs()
                cur.pop()
                used[i] = False
        dfs()
        return res
