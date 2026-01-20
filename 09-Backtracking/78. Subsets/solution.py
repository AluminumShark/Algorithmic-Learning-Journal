# Time: O(n * 2^n) (Since we copy the array at each of the 2^n leaves)
# Space: O(n)
# Concept: Choice Diagram (Include vs Exclude).
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # Include
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            # Exclude
            dfs(i + 1)
        dfs(0)
        return res
