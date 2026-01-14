# LeetCode 33: Search in Rotated Sorted Array

## Overview

Search for a target value in a rotated sorted array using modified binary search that determines which half is sorted.

## Problem Description

There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not.

You must write an algorithm with O(log n) runtime complexity.

**Example:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
```

## Algorithm

**Modified Binary Search**: At each step, determine which half is sorted and decide search direction.

**Key Steps:**
1. Initialize `L = 0` and `R = len(nums) - 1`
2. While `L <= R`:
   - Calculate `mid = (L + R) // 2`
   - If `nums[mid] == target`, return `mid`
   - Determine which half is sorted:
     - If `nums[L] <= nums[mid]`: Left half is sorted
       - If target is in range `[nums[L], nums[mid])`, search left
       - Otherwise, search right
     - Else: Right half is sorted
       - If target is in range `(nums[mid], nums[R]]`, search right
       - Otherwise, search left
3. Return `-1` if not found

## Complexity Analysis

- **Time Complexity:** O(log n) - binary search halves search space each iteration
- **Space Complexity:** O(1) - only uses constant extra space

## Key Concepts

### Binary Search Partitioning

In a rotated sorted array, at least one half is always sorted:

```
[4, 5, 6, 7, 0, 1, 2]
 L        M        R
```

- Compare `nums[L]` with `nums[mid]`:
  - If `nums[L] <= nums[mid]`: Left half `[L, mid]` is sorted
  - Otherwise: Right half `[mid, R]` is sorted

### Decision Logic

Once we know which half is sorted, we can determine if target lies within that sorted range:

1. **Left half sorted** (`nums[L] <= nums[mid]`):
   - If `nums[L] <= target < nums[mid]`: Target must be in left half -> `R = mid - 1`
   - Otherwise: Target must be in right half -> `L = mid + 1`

2. **Right half sorted** (`nums[L] > nums[mid]`):
   - If `nums[mid] < target <= nums[R]`: Target must be in right half -> `L = mid + 1`
   - Otherwise: Target must be in left half -> `R = mid - 1`

## Implementation Details

- Uses `nums[L] <= nums[mid]` (not `<`) to handle edge case when `L == mid`
- Range checks use inclusive/exclusive bounds to avoid missing target
- Standard binary search termination condition `L <= R`

## Pattern Recognition

This problem demonstrates:
- Binary search on rotated arrays
- Identifying sorted segments in partially sorted data
- Combining range checks with binary search

## Related Problems

- Find Minimum in Rotated Sorted Array (LeetCode 153)
- Search in Rotated Sorted Array II (LeetCode 81) - with duplicates
- Binary search variations

## Files

- `solution.py`: Modified binary search for rotated sorted array

