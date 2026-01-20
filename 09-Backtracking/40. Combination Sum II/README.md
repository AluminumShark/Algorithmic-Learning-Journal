# 40. Combination Sum II

## Problem Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Example:**
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Solution: Sort + Skip Duplicates

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # CRITICAL: Sort first!
        cur, res = [], []
        def dfs(start, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > remain:
                    break  # Pruning (sorted, so all remaining are larger)
                cur.append(candidates[i])
                dfs(i + 1, remain - candidates[i])
                cur.pop()
        dfs(0, target)
        return res
```

**Complexity:**
- **Time:** O(n * 2^n)
- **Space:** O(n) - recursion depth

## Key Concepts

### Why Sorting is CRITICAL

Sorting groups duplicates together, making it easy to skip them:

```
Before sort: [10, 1, 2, 7, 6, 1, 5]
After sort:  [1, 1, 2, 5, 6, 7, 10]
              ^  ^
              duplicates are adjacent!
```

### The Skip Duplicates Logic

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

**Why `i > start`?**

- `i == start`: First element at this recursion level, always allowed
- `i > start`: Not the first, check if it's a duplicate

```
candidates = [1, 1, 2], target = 3

At start=0:
  i=0: pick first 1, recurse -> can find [1,2]
  i=1: second 1, but i > start and nums[1]==nums[0]
       SKIP! (otherwise we'd get duplicate [1,2])
  i=2: pick 2, recurse -> can find [2,...]
```

### Why Skip Works

```
[1, 1, 2], target = 3

Without skipping:
  Path 1: pick 1(index 0) -> pick 2 -> [1, 2]
  Path 2: pick 1(index 1) -> pick 2 -> [1, 2]  <- DUPLICATE!

With skipping:
  Path 1: pick 1(index 0) -> pick 2 -> [1, 2]
  Path 2: skip 1(index 1) because it equals previous
```

### The Pruning Optimization

```python
if candidates[i] > remain:
    break  # Not continue!
```

Because array is **sorted**, if current element exceeds remain, all following elements will too. We can `break` entirely, not just `continue`.

### Comparison: Combination Sum vs Combination Sum II

| Aspect | Combination Sum | Combination Sum II |
|--------|----------------|-------------------|
| Input | Distinct elements | May have duplicates |
| Reuse | Unlimited | Each element once |
| Sort needed | No | Yes |
| Skip duplicates | No | Yes |
| Recursion | `dfs(i, ...)` | `dfs(i + 1, ...)` |

### Visual: Why Both 1s Can Appear in Same Combination

```
candidates = [1, 1, 6], target = 8

Valid: [1, 1, 6] using both 1s in ONE path
       First 1 (index 0) -> Second 1 (index 1) -> 6

Invalid duplicate: Two separate paths both producing [1, 6]
       Path A: First 1 (index 0) -> 6
       Path B: Second 1 (index 1) -> 6  <- This is skipped!
```

The skip logic prevents starting new branches with duplicate values, but allows using duplicates **within the same branch**.

## Related Problems

- [39. Combination Sum](../39.%20Combination%20Sum/) - Unlimited reuse, no duplicates
- [90. Subsets II](../90.%20Subsets%20II/) - Same duplicate-handling technique
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/) - Permutations with duplicates
