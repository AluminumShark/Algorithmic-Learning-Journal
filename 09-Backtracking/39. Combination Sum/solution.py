# Time: O((t/m) * 2^(t/m)) where t=target, m=min(candidates). Worst case exponential.
# Space: O(t/m) (Recursion depth)
# Concept: Unbounded Knapsack / Decision Tree. Reusing the same element means calling dfs(i) again after picking. Pruning when remain < 0.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur, res = [], []
        def dfs(i, remain):
            if remain == 0:
                res.append(cur.copy())
                return

            if remain < 0 or i == len(candidates):
                return
            
            cur.append(candidates[i])
            remain -= candidates[i]
            dfs(i, remain) # Stay at i (reuse)
            cur.pop()
            remain += candidates[i]

            dfs(i + 1, remain) # Move to next
        dfs(0, target)
        return res
