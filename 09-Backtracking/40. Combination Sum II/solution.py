# Time: O(n * 2^n)
# Space: O(n)
# Concept: Sort to group duplicates. Skip duplicates in the loop to avoid repeating the same combination.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur, res = [], []
        def dfs(start, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue # Skip duplicates
                if candidates[i] > remain:
                    break # Pruning
                cur.append(candidates[i])
                dfs(i + 1, remain - candidates[i])
                cur.pop()
        dfs(0, target)
        return res
