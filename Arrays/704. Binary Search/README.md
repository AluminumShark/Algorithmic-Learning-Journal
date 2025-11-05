# LeetCode 704: Binary Search

## Overview

Implementation of binary search algorithm for finding a target element in a sorted array.

## Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

## Algorithm

**Binary Search** uses the divide-and-conquer approach to eliminate half of the search space in each iteration.

**Key Steps:**
1. Initialize two pointers (`left` and `right`) defining the search range
2. Calculate the middle index: `mid = left + (right - left) // 2`
3. Compare `nums[mid]` with target:
   - If equal, return the index
   - If less than target, search right half (`left = mid + 1`)
   - If greater than target, search left half (`right = mid - 1`)
4. Repeat until target is found or search range is empty

## Complexity Analysis

- **Time Complexity:** O(log n) - eliminates half of the search space in each iteration
- **Space Complexity:** O(1) - uses only constant extra space

## Implementation Details

- **Approach:** Iterative implementation
- **Overflow Protection:** Uses `left + (right - left) // 2` instead of `(left + right) // 2` to prevent integer overflow
- **Termination Condition:** `left <= right` ensures proper boundary handling

## Use Cases

- Searching in sorted arrays
- Finding insertion positions
- Optimization problems with monotonic properties
- Base pattern for many binary search variants

## Files

- `BinarySearch.py`: Iterative binary search implementation

