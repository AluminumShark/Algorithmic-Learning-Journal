# LeetCode 88: Merge Sorted Array

## Overview

Merge two sorted arrays in-place, where the first array has sufficient space at the end to accommodate all elements.

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array. The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored.

**Example:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

## Algorithm

**Two-Pointer from the End**: Merge from the back of the arrays to avoid overwriting unprocessed elements.

**Key Steps:**
1. Use three pointers:
   - `i`: last initialized element in `nums1` (at index `m-1`)
   - `j`: last element in `nums2` (at index `n-1`)
   - `k`: last position in `nums1` (at index `m+n-1`)
2. Compare elements at `nums1[i]` and `nums2[j]`
3. Place the larger element at `nums1[k]` and move pointers
4. Continue until both arrays are processed
5. If `nums2` has remaining elements, copy them to `nums1`

## Complexity Analysis

- **Time Complexity:** O(m + n) - each element is visited exactly once
- **Space Complexity:** O(1) - only uses constant extra space for pointers

## Why Merge from the End?

Merging from the beginning would require shifting elements, which would be inefficient. Merging from the end:
- Utilizes the available space at the end of `nums1`
- Avoids overwriting unprocessed elements
- Eliminates the need for additional space

## Implementation Details

- In-place merging without extra array
- Three-pointer technique
- Handles remaining elements in `nums2`
- Non-decreasing order maintained

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique
- In-place array manipulation
- Merge operation from merge sort
- Backward iteration strategy

## Use Cases

- Merging sorted arrays efficiently
- In-place array operations
- Two-pointer pattern applications
- Foundation for merge sort algorithm

## Alternative Approaches

1. **Copy and sort**: O((m+n) log(m+n)) - simpler but less efficient
2. **Copy nums1 first**: O(m+n) time and O(m) space - uses extra space

## Files

- `MergeSort.py`: Two-pointer merge from the end implementation

