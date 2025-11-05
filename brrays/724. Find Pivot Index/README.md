# LeetCode 724: Find Pivot Index

## Overview

Find the pivot index where the sum of all elements to the left equals the sum of all elements to the right.

## Problem Description

Given an array of integers `nums`, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return `-1`.

**Example:**
```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: 
Left sum = 1 + 7 + 3 = 11
Right sum = 5 + 6 = 11
```

## Algorithm

**Iterative Approach with Sum Calculation**: Iterate through the array and for each position, calculate the sum of left and right subarrays.

**Key Steps:**
1. Iterate through each index `i` in the array
2. Calculate left sum: sum of elements from index `0` to `i-1`
3. Calculate right sum: sum of elements from index `i+1` to end
4. If left sum equals right sum, return the current index
5. If no pivot found, return `-1`

## Complexity Analysis

- **Time Complexity:** O(n²) - for each of n positions, we calculate sums which take O(n) time
- **Space Complexity:** O(1) - only uses constant extra space

## Optimization Note

A more efficient approach using prefix sums can achieve O(n) time complexity:
1. Pre-compute total sum of array
2. For each index, track cumulative left sum
3. Calculate right sum as `total_sum - left_sum - current_element`
4. Compare left and right sums

This optimization reduces time complexity from O(n²) to O(n).

## Edge Cases

- Empty array: return `-1`
- Single element: return `0` (left and right sums are both 0)
- All elements on one side: handle leftmost/rightmost indices
- No valid pivot: return `-1`

## Pattern Recognition

This problem demonstrates:
- Prefix sum techniques
- Array boundary handling
- Two-pointer approach potential (for optimized version)

## Use Cases

- Balanced partitioning problems
- Array equilibrium problems
- Prefix sum pattern applications
- Foundation for divide-and-conquer array problems

## Files

- `FindPivotIndex.py`: Iterative implementation with sum calculation

