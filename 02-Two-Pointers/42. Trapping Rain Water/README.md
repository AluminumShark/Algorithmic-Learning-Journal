# LeetCode 42: Trapping Rain Water

## Overview

Calculate how much water can be trapped between bars after raining, using prefix/suffix arrays or optimized two pointers.

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Visualization:
       #
   # ~ ~ ~ # #
 # ~ # # ~ # # # ~ #
_#_#_#_#_#_#_#_#_#_#_#_#
0 1 0 2 1 0 1 3 2 1 2 1
```

## Algorithm

### Solution 1: Dynamic Programming

**Key Steps:**
1. Compute `left[i]` = max height from left up to i
2. Compute `right[i]` = max height from right up to i
3. Water at position i = `min(left[i], right[i]) - height[i]`
4. Sum all water amounts

### Solution 2: Two Pointers (Space Optimized)

**Key Steps:**
1. Use two pointers from both ends
2. Track running maxLeft and maxRight
3. Process the side with smaller max (determines water level)
4. Add water and move pointer

## Complexity Analysis

### Solution 1: Dynamic Programming
- **Time Complexity:** O(n) - three passes
- **Space Complexity:** O(n) - two arrays for left/right max

### Solution 2: Two Pointers
- **Time Complexity:** O(n) - single pass
- **Space Complexity:** O(1) - only pointers and running max

## Key Concepts

- **Water Level**: Determined by `min(maxLeft, maxRight)`
- **Prefix/Suffix Pattern**: Precompute boundary information
- **Two Pointer Optimization**: Process smaller side first

## Implementation Details

### Why Process Smaller Max Side?
```python
if maxLeft <= maxRight:
    ans += maxLeft - height[L]
    L += 1
```

When `maxLeft <= maxRight`:
- Water at L is bounded by maxLeft
- We don't need to know exact maxRight (it's at least maxLeft)
- Safe to calculate and move forward

### DP Arrays Example
```
height:  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left:    [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
right:   [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
water:   [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0] = 6
```

## Pattern Recognition

This problem demonstrates:
- Prefix/suffix precomputation pattern
- Two pointer optimization
- Space-time trade-off

## Related Problems

- Container With Most Water (LeetCode 11)
- Largest Rectangle in Histogram (LeetCode 84)
- Product of Array Except Self (same prefix/suffix pattern)

## Edge Cases

- Empty array
- Single element
- All same heights (no water)
- Monotonically increasing/decreasing
- Single valley

## Files

- `solution.py`: DP and Two Pointers implementations

