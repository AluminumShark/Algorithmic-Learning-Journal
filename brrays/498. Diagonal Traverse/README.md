# LeetCode 498: Diagonal Traverse

## Overview

Traverse a 2D matrix in diagonal order, alternating between upward-right and downward-left directions.

## Problem Description

Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

**Example:**
```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

The traversal pattern alternates between:
- Up-right direction: moving diagonally upward and right
- Down-left direction: moving diagonally downward and left

## Algorithm

**Direction-based Traversal** uses a direction flag to control movement and handles boundary conditions when hitting edges.

**Key Steps:**
1. Start at top-left corner `(0, 0)`
2. Use direction flag: `+1` for up-right, `-1` for down-left
3. Move along current diagonal until hitting a boundary
4. When hitting a boundary:
   - If at right edge: move down and flip direction
   - If at bottom edge: move right and flip direction
   - If at left edge: move down and flip direction
   - If at top edge: move right and flip direction
5. Continue until all elements are collected

## Complexity Analysis

- **Time Complexity:** O(m × n) - must visit every element in the matrix exactly once
- **Space Complexity:** O(1) - excluding output array; only uses constant extra space for tracking position and direction

## Implementation Details

- **Approach:** Direction flag with boundary checking
- **Edge Cases:** Handles empty matrix, single row, single column
- **Boundary Handling:** Checks boundaries before movement to determine next step and direction flip

## Pattern Recognition

This problem demonstrates:
- 2D matrix traversal patterns
- Direction management in grid problems
- Boundary condition handling
- State-based movement control

## Use Cases

- Matrix processing algorithms
- Spiral and zigzag traversal patterns
- Image processing (diagonal scanning)
- Foundation for other matrix traversal problems

## Files

- `DiagonalTraverse`: Direction-based diagonal traversal implementation

