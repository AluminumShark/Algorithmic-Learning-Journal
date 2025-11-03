# LeetCode 278: First Bad Version

## Overview

Find the first bad version in a sequence using binary search, given an API that can check if a version is bad.

## Problem Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

**Example:**
```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

## Algorithm

**Binary Search for Boundary**: Search for the first position where `isBadVersion` returns true.

**Key Steps:**
1. Initialize `left = 1` and `right = n`
2. While `left < right`:
   - Calculate `mid = left + (right - left) // 2`
   - If `isBadVersion(mid)` is true:
     - First bad version is at `mid` or before
     - Set `right = mid` (search left half)
   - Else:
     - First bad version is after `mid`
     - Set `left = mid + 1` (search right half)
3. Return `right` (or `left`, they converge to same value)

## Complexity Analysis

- **Time Complexity:** O(log n) - binary search halves search space each iteration
- **Space Complexity:** O(1) - only uses constant extra space

## Key Insight

This is a binary search for the first occurrence problem. The array (implicit) has:
- `false, false, ..., false, true, true, ..., true`
- We need to find the first `true`

## Implementation Details

- Uses `left + (right - left) // 2` to prevent integer overflow
- When `isBadVersion(mid)` is true, keep `mid` in search range (`right = mid`)
- When false, exclude `mid` (`left = mid + 1`)
- Loop condition `left < right` ensures convergence

## Pattern Recognition

This problem demonstrates:
- Binary search for boundary/transition point
- First/last occurrence search
- API-based search problems

## Use Cases

- Finding transition points in sequences
- Boundary detection algorithms
- API-based search problems
- First occurrence search patterns

## Related Problems

- Search Insert Position
- Find First and Last Position of Element in Sorted Array
- Binary search variations

## Files

- `BinarySearch.py`: Binary search for first bad version

