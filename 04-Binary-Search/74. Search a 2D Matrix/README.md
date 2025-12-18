# LeetCode 74: Search a 2D Matrix

## Overview

Search for a target value in a 2D matrix that is sorted both row-wise and column-wise, using binary search optimization.

## Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

## Algorithm

### Solution 1: Brute Force

**Key Steps:**
1. Iterate through each row
2. Skip rows where target is greater than the last element
3. For each valid row, iterate through columns
4. Return true if target is found, false otherwise

### Solution 2: Binary Search (Treat 2D as 1D)

**Key Steps:**
1. Treat the 2D matrix as a flattened 1D sorted array
2. Use binary search with virtual indices
3. Convert 1D index to 2D coordinates: `row = mid // m`, `col = mid % m`
4. Compare matrix value at calculated position with target
5. Adjust search range based on comparison

## Complexity Analysis

### Solution 1: Brute Force
- **Time Complexity:** O(m * n) - worst case visits every element
- **Space Complexity:** O(1) - only uses constant extra space

### Solution 2: Binary Search
- **Time Complexity:** O(log(m * n)) - binary search on flattened array
- **Space Complexity:** O(1) - only uses constant extra space

## Key Concepts

- **2D to 1D Mapping**: Convert 2D matrix indices to 1D array index
  - 1D index `i` → 2D position: `row = i // m`, `col = i % m`
  - This works because rows are stored consecutively in memory
- **Binary Search on Sorted Structure**: The matrix properties guarantee sorted order when flattened
- **Coordinate Conversion**: Efficiently map between linear and 2D indices

## Implementation Details

### Brute Force Approach
- Early termination when target exceeds row's last element
- Simple nested loop structure
- No preprocessing required

### Binary Search Approach
- Virtual indexing: treat matrix as 1D array without actually flattening
- Index conversion: `mid // m` gives row, `mid % m` gives column
- Standard binary search logic with coordinate translation
- Prevents integer overflow by using `(L + R) // 2`

## Pattern Recognition

This problem demonstrates:
- Binary search on 2D structures
- Index mapping between dimensions
- Treating multi-dimensional data as linear for search

## Use Cases

- Searching in sorted 2D data structures
- Matrix search optimization
- Converting multi-dimensional problems to 1D binary search

## Related Problems

- Search a 2D Matrix II (LeetCode 240) - Different sorting property
- Binary search variations
- Matrix traversal problems

## Files

- `solution.py`: Brute Force and Binary Search implementations

