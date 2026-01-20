# 39. Combination Sum

## Problem Description

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

**Example:**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 + 2 + 3 = 7
7 = 7
```

## Solution: Unbounded Selection (Can Reuse)

```python
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
            dfs(i, remain)  # Stay at i (reuse allowed)
            cur.pop()
            remain += candidates[i]

            dfs(i + 1, remain)  # Move to next candidate
        dfs(0, target)
        return res
```

**Complexity:**
- **Time:** O((t/m) * 2^(t/m)) where t = target, m = min(candidates)
- **Space:** O(t/m) - maximum recursion depth

## Key Concepts

### The Key Difference: `dfs(i)` vs `dfs(i + 1)`

| Problem | After picking | Meaning |
|---------|--------------|---------|
| Subsets | `dfs(i + 1)` | Move on, can't reuse |
| Combination Sum | `dfs(i)` | Stay, can reuse same element |

```python
# Reuse current element (stay at index i)
dfs(i, remain)

# Don't use current element, move to next
dfs(i + 1, remain)
```

### Decision Tree Example

```
candidates = [2, 3], target = 5

                    remain=5, i=0
                   /              \
            pick 2                 skip 2
         remain=3, i=0          remain=5, i=1
         /        \                /        \
     pick 2      skip 2        pick 3     skip 3
   remain=1     remain=3     remain=2    remain=5
     /    \       i=1          i=1        i=2 (end)
  pick 2  skip   /    \        ...
 remain=-1  ... pick 3 skip
  (prune)     remain=0  ...
               FOUND!
               [2,2,3]
```

### Pruning Conditions

```python
if remain < 0:    # Exceeded target, stop
    return

if i == len(candidates):  # No more candidates
    return
```

### Why No Duplicates Without Sorting?

Unlike Combination Sum II, we don't need sorting here because:
1. Candidates are **distinct**
2. We only move **forward** (never go back to earlier candidates)
3. Each candidate can be used unlimited times **in sequence**

This naturally avoids duplicates like [2,3] and [3,2].

### Connection to Unbounded Knapsack

This problem is similar to the **Unbounded Knapsack** problem:
- Candidates = items (can use each infinitely)
- Target = knapsack capacity
- Finding all ways to fill exactly

### Alternative: Loop-based Approach

```python
def combinationSum(candidates, target):
    res = []
    def dfs(start, remain, path):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                continue
            path.append(candidates[i])
            dfs(i, remain - candidates[i], path)  # i, not i+1
            path.pop()
    dfs(0, target, [])
    return res
```

## Related Problems

- [40. Combination Sum II](../40.%20Combination%20Sum%20II/) - Each element used once, has duplicates
- [78. Subsets](../78.%20Subsets/) - No target sum
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) - Count permutations (order matters)
