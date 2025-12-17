# LeetCode 15: 3Sum

## Overview

Find all unique triplets in the array that sum to zero using sorting and two pointers.

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []
```

## Algorithm

### Solution 1: Brute Force with Set

**Key Steps:**
1. Sort the array
2. For each element as middle, use two pointers for left and right
3. Store results and remove duplicates using set

### Solution 2: Optimized Two Pointers

**Key Steps:**
1. Sort the array
2. Fix first element, use two pointers for remaining two
3. Skip duplicates at each level to avoid duplicate triplets
4. Return results directly (no post-processing needed)

## Complexity Analysis

### Solution 1: Set-Based
- **Time Complexity:** O(n²) - nested loops
- **Space Complexity:** O(n) - for storing results and set conversion

### Solution 2: Optimized
- **Time Complexity:** O(n²) - sorting O(n log n) + nested loops O(n²)
- **Space Complexity:** O(1) - excluding output array

## Key Concepts

- **Sorting**: Enables two-pointer technique
- **Two Pointers**: Efficient pair search in sorted array
- **Duplicate Skipping**: Avoid duplicate triplets inline

## Implementation Details

### Skip Duplicate Elements
```python
# Skip duplicate i values
if i > 0 and nums[i - 1] == nums[i]:
    continue

# Skip duplicate L and R values after finding a triplet
while L < R and nums[L - 1] == nums[L]:
    L += 1
while L < R and nums[R + 1] == nums[R]:
    R -= 1
```

### Two Pointer Logic
```
nums = [-4, -1, -1, 0, 1, 2]
i = 1 (value = -1)
L = 2, R = 5

-1 + -1 + 2 = 0 ✓
```

## Pattern Recognition

This problem demonstrates:
- Extension of Two Sum to three elements
- Duplicate handling in results
- Sorting for two-pointer technique

## Related Problems

- Two Sum (LeetCode 1)
- Two Sum II (LeetCode 167)
- 4Sum (LeetCode 18)
- 3Sum Closest (LeetCode 16)

## Edge Cases

- Array with less than 3 elements
- All zeros `[0, 0, 0]`
- No valid triplets
- Many duplicate values
- All negative or all positive numbers

## Files

- `solution.py`: Set-based and Optimized implementations

