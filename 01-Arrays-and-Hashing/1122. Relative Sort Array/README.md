# LeetCode 1122: Relative Sort Array

## Overview

Sort an array `arr1` according to the relative order of elements in `arr2`, with remaining elements sorted in ascending order.

## Problem Description

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements that don't appear in `arr2` should be placed at the end of `arr1` in ascending order.

**Example:**
```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

## Algorithm

**Counting Sort Approach**: Use counting sort to efficiently handle bounded integer values (0-1000).

**Key Steps:**
1. Count the frequency of each element in `arr1`
2. First pass: iterate through `arr2` in order, adding each element according to its frequency
3. Second pass: iterate through remaining counts in ascending order to append elements not in `arr2`

## Complexity Analysis

- **Time Complexity:** O(n + m + k) - where n is length of arr1, m is length of arr2, and k is the value range (typically 1001)
- **Space Complexity:** O(k) - for the counting array (value range)

## Advantages of Counting Sort

- Efficient for bounded integer ranges (0-1000 in this problem)
- Linear time complexity when range is small
- Maintains relative order from `arr2`
- Handles duplicates naturally through frequency counting

## Implementation Details

- Uses frequency counting to preserve relative order
- Two-pass approach: first for `arr2` order, second for remaining elements
- Handles all elements in `arr1`, including those not in `arr2`

## Pattern Recognition

This problem demonstrates:
- Counting sort for bounded integer sorting
- Relative ordering with custom comparison
- Two-pass processing strategies

## Use Cases

- Custom sorting with predefined order
- Efficient sorting of bounded integer arrays
- Relative ranking problems

## Files

- `CountingSort..py`: Counting sort implementation for relative ordering

