# LeetCode 26: Remove Duplicates from Sorted Array

## Overview

Remove duplicates from a sorted array in-place, returning the new length of the unique elements.

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result.

Return `k` after placing the final result in the first `k` slots of `nums`.

**Example:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

## Algorithm

**Two Pointers (Slow-Fast)**: Use a slow pointer to mark the end of unique section and a fast pointer to scan for next distinct element.

**Key Steps:**
1. Initialize `slow = 0` (marks end of unique section) and `fast = 1` (scanner)
2. Move `fast` through the array
3. When `nums[fast] != nums[slow]`:
   - Found a new unique element
   - Place it at `nums[slow + 1]`
   - Increment `slow` to expand unique section
4. Always increment `fast`
5. Return `slow + 1` as the new length

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(1) - in-place modification, only uses constant extra space

## Implementation Details

- In-place modification without extra array
- Maintains relative order of elements
- Slow pointer tracks unique section boundary
- Fast pointer finds next distinct value

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique (slow-fast pattern)
- In-place array modification
- Boundary tracking patterns

## Use Cases

- Deduplication of sorted data
- In-place array filtering
- Data cleaning algorithms
- Foundation for other two-pointer problems

## Related Problems

- Remove Duplicates from Sorted Array II (allow at most 2 duplicates)
- Remove Element
- Move Zeroes

## Files

- `TwoPointers.py`: Slow-fast two-pointer implementation

