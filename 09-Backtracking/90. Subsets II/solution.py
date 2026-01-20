# Time: O(n * 2^n)
# Space: O(n)
# Concept: Sort + Skip duplicates during the "Exclude" branch (or while loop strategy) to ensure unique subsets.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur, res = [], []
        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # Include
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            # Exclude (Skip duplicates)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1)
        dfs(0)
        return res
