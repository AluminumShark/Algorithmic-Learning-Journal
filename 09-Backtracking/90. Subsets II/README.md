# 90. Subsets II

## Problem Description

Given an integer array `nums` that may contain **duplicates**, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example:**
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

## Solution: Sort + Skip Duplicates on Exclude

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # CRITICAL: Sort first!
        cur, res = [], []
        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # Include nums[i]
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            # Exclude nums[i] - Skip all duplicates!
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1)
        dfs(0)
        return res
```

**Complexity:**
- **Time:** O(n * 2^n)
- **Space:** O(n) - recursion depth

## Key Concepts

### Why Sorting is CRITICAL

Sorting groups duplicates together:

```
Before: [1, 2, 2]  (already sorted in this example)
After:  [1, 2, 2]
            ^--^ duplicates adjacent
```

### The Skip Logic on Exclude

When we **exclude** an element, we skip all its duplicates too:

```python
# Exclude current element AND all duplicates
while i + 1 < len(nums) and nums[i] == nums[i + 1]:
    i += 1
dfs(i + 1)
```

### Why Skip on Exclude, Not Include?

Consider `[2, 2]`:

```
Without skipping:
               []
            /      \
         [2]        []       <- First 2: include or exclude
        /   \      /   \
    [2,2]   [2]  [2]    []   <- Second 2: include or exclude
    
    Results: [2,2], [2], [2], []
                    ^----^ DUPLICATES!

With skipping on exclude:
               []
            /      \
         [2]        []       <- First 2: include or exclude
        /   \         \
    [2,2]   [2]        []    <- If excluded first 2, skip second 2 too
    
    Results: [2,2], [2], []
             No duplicates!
```

**Key insight:** If we exclude an element, we must exclude ALL its duplicates. Otherwise, different branches produce the same subset.

### Visual Decision Tree for [1, 2, 2]

```
                        [], i=0
                       /        \
                   [1]            []
                  i=1             i=1
                /     \          /    \
            [1,2]     [1]      [2]     []
             i=2     skip!      i=2   skip!
            /   \      |       /   \    |
       [1,2,2] [1,2]  [1]   [2,2]  [2]  []
       
Skip: When excluding 2, skip to i=3 (past all 2s)

Final: [1,2,2], [1,2], [1], [2,2], [2], []
```

### Alternative: Loop-based with Skip

```python
def subsetsWithDup(nums):
    nums.sort()
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue  # Skip duplicates
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res
```

This uses the same skip pattern as Combination Sum II.

### Comparison: Subsets vs Subsets II

| Aspect | Subsets | Subsets II |
|--------|---------|------------|
| Input | Unique elements | May have duplicates |
| Sort needed | No | Yes |
| Skip duplicates | No | Yes (on exclude branch) |

### The Include/Exclude Pattern Summary

```
For unique elements (Subsets):
- Include: add, recurse, pop
- Exclude: just recurse

For duplicates (Subsets II):
- Include: add, recurse, pop
- Exclude: skip all duplicates, THEN recurse
```

## Related Problems

- [78. Subsets](../78.%20Subsets/) - Without duplicates
- [40. Combination Sum II](../40.%20Combination%20Sum%20II/) - Same duplicate-handling technique
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/) - Permutations with duplicates
