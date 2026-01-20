# 46. Permutations

## Problem Description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Solution: Backtracking with Used Array

```python
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
```

**Complexity:**
- **Time:** O(n * n!) - n! permutations, each takes O(n) to copy
- **Space:** O(n) - recursion depth + used array

## Key Concepts

### Why `used` Array?

In permutations, **order matters** and **each element appears exactly once**. We need to track which elements are already in the current permutation.

```python
used = [False] * len(nums)

# Before using element i
if used[i]:
    continue  # Already in current permutation

# Mark as used
used[i] = True

# After backtracking, unmark
used[i] = False
```

### Permutation vs Subset vs Combination

| Problem | Order Matters? | Reuse? | Result Count |
|---------|---------------|--------|--------------|
| Permutation | Yes | No | n! |
| Subset | No | No | 2^n |
| Combination | No | No | C(n,k) |

### Decision Tree for [1,2,3]

```
                        []
           /            |            \
         [1]          [2]           [3]
        /   \        /   \         /   \
     [1,2] [1,3]  [2,1] [2,3]   [3,1] [3,2]
       |     |      |     |       |     |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
```

At each level, we try **all unused elements**.

### Alternative: Swap-based Approach

```python
def permute(nums):
    res = []
    def backtrack(start):
        if start == len(nums):
            res.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return res
```

This approach swaps elements in place instead of using a `used` array.

### Alternative: Python's itertools

```python
from itertools import permutations
def permute(nums):
    return [list(p) for p in permutations(nums)]
```

### Why n! Permutations?

For n elements:
- First position: n choices
- Second position: n-1 choices
- Third position: n-2 choices
- ...
- Total: n * (n-1) * (n-2) * ... * 1 = n!

### Backtracking Template for Permutations

```python
def backtrack():
    if len(current) == len(nums):
        result.append(current.copy())
        return
    
    for i in range(len(nums)):
        if used[i]:
            continue
        
        # Choose
        current.append(nums[i])
        used[i] = True
        
        # Explore
        backtrack()
        
        # Unchoose
        current.pop()
        used[i] = False
```

## Related Problems

- [47. Permutations II](https://leetcode.com/problems/permutations-ii/) - With duplicates
- [78. Subsets](../78.%20Subsets/) - Subsets (order doesn't matter)
- [31. Next Permutation](https://leetcode.com/problems/next-permutation/) - Find next lexicographic permutation
