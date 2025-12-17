# LeetCode 11: Container With Most Water

## Overview

Find two vertical lines that together with the x-axis form a container that holds the most water using two pointers.

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Example:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 form container with area = 7 × 7 = 49
```

## Algorithm

**Two Pointers Approach**:

**Key Steps:**
1. Initialize pointers at both ends
2. Calculate area: `min(height[L], height[R]) × (R - L)`
3. Update maximum area
4. Move the pointer with smaller height inward
5. Repeat until pointers meet

## Complexity Analysis

- **Time Complexity:** O(n) - single pass with two pointers
- **Space Complexity:** O(1) - only uses pointers

## Key Concepts

- **Two Pointers**: Start from maximum width
- **Greedy Choice**: Move shorter line to potentially find taller one
- **Area Formula**: `min(h1, h2) × width`

## Implementation Details

### Why Move the Shorter Line?
- Water is limited by the shorter line
- Moving the taller line can only decrease or maintain area (width decreases)
- Moving the shorter line might find a taller line (potential increase)

### Proof of Correctness
```
If height[L] < height[R]:
  - Any container with L as left boundary is limited by height[L]
  - Maximum width with L is already considered (R - L)
  - Moving L inward is the only way to potentially find a better solution
```

## Pattern Recognition

This problem demonstrates:
- Two pointers for optimization
- Greedy algorithm reasoning
- Area maximization problem

## Visualization

```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
          L                       R
          
Area = min(1, 7) × 8 = 8

Move L (shorter):
             L                    R
Area = min(8, 7) × 7 = 49 ← Maximum
```

## Related Problems

- Trapping Rain Water (LeetCode 42)
- Largest Rectangle in Histogram (LeetCode 84)
- Maximum Area of Island

## Edge Cases

- Two elements only
- All same heights
- Increasing heights
- Decreasing heights
- Single peak in middle

## Files

- `solution.py`: Two pointers implementation

