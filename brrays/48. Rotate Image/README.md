# LeetCode 48: Rotate Image

## Overview

Rotate a 2D matrix 90 degrees clockwise in-place without using additional matrix.

## Problem Description

You are given an `n × n` 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. Do not allocate another 2D matrix and do the rotation.

**Example:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

## Algorithm

**Two-Step Transformation**: 
1. Transpose the matrix (swap elements across main diagonal)
2. Reverse each row (horizontal mirroring)

This combination achieves a 90-degree clockwise rotation.

**Key Steps:**
1. **Transpose**: Swap `matrix[i][j]` with `matrix[j][i]` for all `j >= i`
   - Only swap upper triangle to avoid double-swapping
2. **Reverse rows**: Reverse each row of the transposed matrix
   - Swap `matrix[i][j]` with `matrix[i][n-1-j]` for each row

## Complexity Analysis

- **Time Complexity:** O(n²) - must visit every element once for transpose, once for reversal
- **Space Complexity:** O(1) - in-place modification, only uses constant extra space

## Mathematical Insight

A 90-degree clockwise rotation can be decomposed into:
1. Transpose: reflects matrix across main diagonal
2. Row reversal: mirrors horizontally

This is equivalent to: `rotate(matrix) = reverse(transpose(matrix))`

## Alternative Approaches

1. **Layer-by-layer rotation**: Rotate in concentric squares
   - More intuitive but slightly more complex indexing

2. **Direct coordinate mapping**: Calculate new positions directly
   - `(i, j) → (j, n-1-i)` for 90° clockwise rotation

## Implementation Details

- In-place modification without extra matrix
- Careful index management to avoid double-swapping
- Transpose only upper triangle (`j >= i`)
- Row reversal for each row

## Pattern Recognition

This problem demonstrates:
- Matrix transformation techniques
- In-place algorithm design
- Coordinate mapping patterns
- Decomposition of complex operations

## Use Cases

- Image rotation algorithms
- Matrix manipulation problems
- 2D array transformation
- In-place algorithm design patterns

## Files

- `RotateImage.py`: Transpose and reverse implementation

