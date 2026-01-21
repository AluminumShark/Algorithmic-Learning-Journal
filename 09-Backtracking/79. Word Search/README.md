# 79. Word Search

## Problem Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**
```
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"

Output: true
```

## Solution: Grid DFS + Backtracking

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r > R - 1 or c > C - 1 or 
                board[r][c] == '#' or board[r][c] != word[i]):
                return False

            ch = board[r][c]
            board[r][c] = '#'  # Mark visited

            res = (
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1)
            )

            board[r][c] = ch  # Restore (Backtrack)

            return res
            
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False
```

**Complexity:**
- **Time:** O(R * C * 4^L) where L = length of word
- **Space:** O(L) - recursion depth

## Key Concepts

### The Mark Visited / Backtrack Restore Pattern

This is a **critical pattern** for grid-based backtracking:

```python
ch = board[r][c]     # 1. Save original value
board[r][c] = '#'    # 2. Mark as visited (using placeholder)

# 3. Explore all directions
res = dfs(...) or dfs(...) or dfs(...) or dfs(...)

board[r][c] = ch     # 4. Restore original value (backtrack)
```

### Why Use `#` as Placeholder?

Any character not in the input works. Using `#`:
- Makes it clear this cell is "visited"
- Fails the `board[r][c] != word[i]` check immediately
- Easy to debug and visualize

### Combined Boundary Check

```python
if (r < 0 or c < 0 or r > R - 1 or c > C - 1 or  # Out of bounds
    board[r][c] == '#' or                         # Already visited
    board[r][c] != word[i]):                      # Wrong character
    return False
```

All invalid conditions in one check for efficiency.

### Visual Walkthrough

```
board = [["A","B","C","E"],        word = "ABCCED"
         ["S","F","C","S"],
         ["A","D","E","E"]]

Start at (0,0) 'A', i=0:
  A matches word[0]
  Mark (0,0) as '#'
  Try (0,1) 'B', i=1:
    B matches word[1]
    Mark (0,1) as '#'
    Try (0,2) 'C', i=2:
      C matches word[2]
      Mark (0,2) as '#'
      Try (1,2) 'C', i=3:
        C matches word[3]
        Mark (1,2) as '#'
        Try (2,2) 'E', i=4:
          E matches word[4]
          Mark (2,2) as '#'
          Try (2,1) 'D', i=5:
            D matches word[5]
            i+1 == len(word) -> return True!
```

### Why Backtracking is Essential

Without restoring visited cells:

```
Finding "ABCB" in:
A - B
|   |
C - B

Path 1: A -> B -> C -> B (can't use B again!)
Without backtrack: B stays marked, Path 2 fails
With backtrack: B is unmarked after Path 1, can try other routes
```

### Alternative: Using a Set

```python
def exist(board, word):
    R, C = len(board), len(board[0])
    visited = set()
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= R or c >= C or
            (r, c) in visited or board[r][c] != word[i]):
            return False
        
        visited.add((r, c))
        res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or 
               dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
        visited.remove((r, c))
        return res
    
    # ... rest same
```

This uses extra O(L) space but doesn't modify the input.

### Time Complexity Analysis

- Starting points: R * C
- At each step: 4 directions (but really 3, can't go back)
- Maximum depth: L (word length)
- Total: O(R * C * 4^L), but practically closer to O(R * C * 3^L)

## Related Problems

- [212. Word Search II](../../08-Tries/212.%20Word%20Search%20II/) - Multiple words (use Trie)
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Grid DFS
- [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Grid DFS with boundary
