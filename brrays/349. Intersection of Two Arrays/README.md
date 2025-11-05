# LeetCode 349: Intersection of Two Arrays

## Overview

Find the intersection of two arrays, returning unique elements that appear in both arrays.

## Problem Description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

**Example:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

## Algorithm

**Two Pointers after Sorting**: Sort both arrays, then use two pointers to find common elements while avoiding duplicates.

**Key Steps:**
1. Sort both `nums1` and `nums2`
2. Initialize two pointers, one for each array
3. Compare elements at both pointers:
   - If equal: add to result (if not duplicate) and move both pointers
   - If `nums1[pt1] < nums2[pt2]`: move `pt1` forward
   - If `nums1[pt1] > nums2[pt2]`: move `pt2` forward
4. Continue until one array is exhausted

## Complexity Analysis

- **Time Complexity:** O(n log n + m log m) - sorting both arrays, where n and m are array lengths
- **Space Complexity:** O(min(n, m)) - for the result array in worst case

## Alternative Approaches

1. **Hash Set**: O(n + m) time, O(n + m) space
   - Convert one array to set, iterate through other
   - More efficient for unsorted arrays

2. **Built-in Set Intersection**: O(n + m) average case
   - Use Python's set operations: `set(nums1) & set(nums2)`

## Implementation Details

- Duplicate avoidance: check if last element in result equals current
- Two-pointer technique for sorted arrays
- Handles arrays of different sizes

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique on sorted arrays
- Set intersection concepts
- Duplicate handling strategies

## Use Cases

- Finding common elements between datasets
- Set intersection operations
- Data comparison algorithms

## Files

- `TwoPointers.py`: Two-pointer implementation with sorting

