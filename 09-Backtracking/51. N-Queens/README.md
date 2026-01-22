# 51. N-Queens

## Problem Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example:**
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],
         ["..Q.","Q...","...Q",".Q.."]]

Visual:
Solution 1:       Solution 2:
. Q . .           . . Q .
. . . Q           Q . . .
Q . . .           . . . Q
. . Q .           . Q . .
```

## Solution: Backtracking with Set Constraints

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()  # Negative diagonal (r - c)
        diag2 = set()  # Positive diagonal (r + c)
        board = [['.'] * n for _ in range(n)]
        res = []

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                dfs(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        dfs(0)
        return res
```

**Complexity:**
- **Time:** O(N!) - At most N choices for first row, N-1 for second, etc.
- **Space:** O(N^2) - Board storage

## Key Concepts

### Strategy: Place Queens Row by Row

Since each row must have exactly one queen, we place queens **one row at a time**:

```
Row 0: Try column 0, 1, 2, ..., n-1
  For each valid placement:
    Row 1: Try column 0, 1, 2, ..., n-1
      For each valid placement:
        Row 2: ...
          ...
            Row n-1: Found a solution!
```

This eliminates row conflicts automatically.

### The Three Constraints

A queen attacks in 4 directions: horizontal, vertical, and both diagonals.

| Constraint | How to Check | Data Structure |
|------------|-------------|----------------|
| Same Column | `c in cols` | `cols` set |
| Negative Diagonal (\\) | `(r - c) in diag1` | `diag1` set |
| Positive Diagonal (/) | `(r + c) in diag2` | `diag2` set |

Row conflicts are impossible since we place one queen per row.

### Why `r - c` for Negative Diagonal (\\)?

**Key insight:** Cells on the same top-left to bottom-right diagonal have the **same `r - c` value**.

```
     c=0  c=1  c=2  c=3
r=0   0   -1   -2   -3      <- r - c values
r=1   1    0   -1   -2
r=2   2    1    0   -1
r=3   3    2    1    0

Diagonal examples (same r-c):
  r-c = 0: (0,0), (1,1), (2,2), (3,3)  <- main diagonal
  r-c = 1: (1,0), (2,1), (3,2)
  r-c = -1: (0,1), (1,2), (2,3)
```

Visual:
```
  0   1   2   3
+---+---+---+---+
| 0 |-1 |-2 |-3 | r=0
+---+---+---+---+
| 1 | 0 |-1 |-2 | r=1
+---+---+---+---+
| 2 | 1 | 0 |-1 | r=2
+---+---+---+---+
| 3 | 2 | 1 | 0 | r=3
+---+---+---+---+

Cells with same number are on same \ diagonal!
```

### Why `r + c` for Positive Diagonal (/)?

**Key insight:** Cells on the same bottom-left to top-right diagonal have the **same `r + c` value**.

```
     c=0  c=1  c=2  c=3
r=0   0    1    2    3      <- r + c values
r=1   1    2    3    4
r=2   2    3    4    5
r=3   3    4    5    6

Diagonal examples (same r+c):
  r+c = 3: (0,3), (1,2), (2,1), (3,0)  <- anti-diagonal
  r+c = 2: (0,2), (1,1), (2,0)
  r+c = 4: (1,3), (2,2), (3,1)
```

Visual:
```
  0   1   2   3
+---+---+---+---+
| 0 | 1 | 2 | 3 | r=0
+---+---+---+---+
| 1 | 2 | 3 | 4 | r=1
+---+---+---+---+
| 2 | 3 | 4 | 5 | r=2
+---+---+---+---+
| 3 | 4 | 5 | 6 | r=3
+---+---+---+---+

Cells with same number are on same / diagonal!
```

### The Backtracking Template

```python
for c in range(n):
    if not valid(r, c):
        continue
    
    # Place queen
    board[r][c] = 'Q'
    cols.add(c)
    diag1.add(r - c)
    diag2.add(r + c)
    
    # Recurse to next row
    dfs(r + 1)
    
    # Remove queen (backtrack)
    board[r][c] = '.'
    cols.remove(c)
    diag1.remove(r - c)
    diag2.remove(r + c)
```

### Walkthrough for n=4

```
Row 0: Try c=0
  Place Q at (0,0), cols={0}, diag1={0}, diag2={0}
  
  Row 1: c=0 blocked (col), c=1 blocked (diag1), try c=2
    Place Q at (1,2), cols={0,2}, diag1={0,-1}, diag2={0,3}
    
    Row 2: c=0,1,2,3 all blocked! Backtrack.
  
  Row 1: try c=3
    Place Q at (1,3), cols={0,3}, diag1={0,-2}, diag2={0,4}
    
    Row 2: c=0,3 blocked, c=1 blocked (diag2=3), try c=1? No, diag2.
           Actually c=1: diag2=2+1=3? No. Try systematically...
    ... (continue until solution found)

Solutions found:
. Q . .    . . Q .
. . . Q    Q . . .
Q . . .    . . . Q
. . Q .    . Q . .
```

### Time Complexity: Why O(N!)?

- Row 0: N choices
- Row 1: At most N-1 valid choices (one column blocked)
- Row 2: At most N-2 valid choices
- ...
- Worst case: N * (N-1) * (N-2) * ... * 1 = N!

In practice, diagonal constraints prune many branches, making it faster.

### N-Queens II (Count Solutions)

For [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/), just count instead of building boards:

```python
def totalNQueens(n):
    # Same logic, but:
    # Instead of: res.append([...])
    # Do: self.count += 1
    # Return self.count
```

## Related Problems

- [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/) - Just count solutions
- [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) - Similar constraint backtracking
- [79. Word Search](../79.%20Word%20Search/) - Grid backtracking
