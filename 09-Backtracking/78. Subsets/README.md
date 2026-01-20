# 78. Subsets

## Problem Description

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

## Solution: Include vs Exclude (Decision Tree)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # Include nums[i]
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            # Exclude nums[i]
            dfs(i + 1)
        dfs(0)
        return res
```

**Complexity:**
- **Time:** O(n * 2^n) - 2^n subsets, each takes O(n) to copy
- **Space:** O(n) - recursion depth

## Key Concepts

### The Decision Tree

For each element, we have exactly **two choices**: include it or exclude it.

```
nums = [1, 2, 3]

                    []
                 /      \
           [1]            []
          /    \        /    \
      [1,2]    [1]    [2]     []
      /  \    /  \   /  \    /  \
[1,2,3][1,2][1,3][1][2,3][2][3] []

Leaves (2^3 = 8 subsets): 
[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []
```

### Backtracking Pattern

```python
# Include
cur.append(nums[i])   # 1. Make choice
dfs(i + 1)            # 2. Explore
cur.pop()             # 3. Undo choice (backtrack)

# Exclude
dfs(i + 1)            # Just move forward without adding
```

The key insight: **after exploring with an element included, we "pop" it to restore state** before exploring the exclude branch.

### Why `cur.copy()`?

```python
res.append(cur.copy())  # NOT res.append(cur)
```

If we append `cur` directly, all entries in `res` would reference the **same list**, which keeps changing. We need a **snapshot** of the current state.

### Alternative: Iterative Approach

```python
def subsets(nums):
    result = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
    return result
```

Each number doubles the result set by adding itself to all existing subsets.

### Alternative: Bit Manipulation

```python
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):  # 0 to 2^n - 1
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result
```

Each bit pattern represents a subset (1 = include, 0 = exclude).

### Comparison of Approaches

| Approach | Time | Space | Pros |
|----------|------|-------|------|
| Backtracking | O(n * 2^n) | O(n) | Clear decision tree |
| Iterative | O(n * 2^n) | O(n * 2^n) | Simple logic |
| Bit Manipulation | O(n * 2^n) | O(n) | Compact code |

## Backtracking Template

```python
def backtrack(state, choices):
    if is_solution(state):
        result.append(state.copy())
        return
    
    for choice in choices:
        make_choice(state, choice)
        backtrack(state, remaining_choices)
        undo_choice(state, choice)  # Backtrack
```

## Related Problems

- [90. Subsets II](../90.%20Subsets%20II/) - With duplicates
- [39. Combination Sum](../39.%20Combination%20Sum/) - Sum to target
- [46. Permutations](../46.%20Permutations/) - Order matters
