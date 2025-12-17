# LeetCode 36: Valid Sudoku

## Overview

Determine if a 9x9 Sudoku board is valid by checking rows, columns, and 3x3 sub-boxes for duplicates.

## Problem Description

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition
2. Each column must contain the digits 1-9 without repetition
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition

**Note:** A Sudoku board (partially filled) could be valid but is not necessarily solvable.

**Example:**
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

## Algorithm

**Hash Set Validation**: Use sets to track seen numbers in each row, column, and box.

**Key Steps:**
1. Initialize 9 sets each for rows, columns, and boxes
2. Iterate through each cell
3. Skip empty cells ('.')
4. Calculate box index from row and column
5. Check if value exists in any corresponding set
6. If duplicate found, return false
7. Otherwise, add to all three sets

## Complexity Analysis

- **Time Complexity:** O(1) - fixed 81 cells to check
- **Space Complexity:** O(1) - fixed 27 sets with at most 9 elements each

## Key Concepts

- **Hash Set**: O(1) duplicate detection
- **Box Index Calculation**: `(r // 3) * 3 + (c // 3)`
- **Validation vs Solving**: Only checks validity, not solvability

## Implementation Details

### Box Index Mapping
```
Row/Col (0-2, 0-2) -> Box 0
Row/Col (0-2, 3-5) -> Box 1
Row/Col (0-2, 6-8) -> Box 2
Row/Col (3-5, 0-2) -> Box 3
... and so on

Formula: (r // 3) * 3 + (c // 3)
```

### Set-Based Tracking
- Each set stores characters '1'-'9'
- Empty cells '.' are skipped
- Single pass through the board

## Pattern Recognition

This problem demonstrates:
- Hash set for duplicate detection
- 2D grid traversal
- Index mapping for sub-regions

## Related Problems

- Sudoku Solver (LeetCode 37)
- Check if Every Row and Column Contains All Numbers
- N-Queens validation

## Edge Cases

- Board with many empty cells
- Board with all cells filled
- Invalid board with duplicate in row
- Invalid board with duplicate in column
- Invalid board with duplicate in box

## Files

- `solution.py`: Hash set validation implementation

