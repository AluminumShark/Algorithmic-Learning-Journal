# 212. Word Search II

## Problem Description

Given an `m x n` board of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example:**
```
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

## Solution: Trie + Backtracking + Pruning

```python
class TrieNode:
    __slots__ = ("children", "word")
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie from words
        root = TrieNode()
        for w in words:
            cur = root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = w  # Store complete word at end node
        
        ans = []
        R, C = len(board), len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            nxt = node.children[ch]

            if nxt.word is not None:
                ans.append(nxt.word)
                nxt.word = None  # Avoid duplicates
            
            board[r][c] = '#'  # Mark visited

            # Explore 4 directions
            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, nxt)
            if r < R - 1 and board[r + 1][c] != '#':
                dfs(r + 1, c, nxt)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, nxt)
            if c < C - 1 and board[r][c + 1] != '#':
                dfs(r, c + 1, nxt)
            
            board[r][c] = ch  # Backtrack

            # CRITICAL: Leaf node pruning
            if not nxt.children:
                node.children.pop(ch, None)
            
        for r in range(R):
            for c in range(C):
                dfs(r, c, root)

        return ans
```

**Complexity:**
- **Time:** O(R * C * 3^L) where L = max word length, 3 because we don't go back
- **Space:** O(S) where S = total characters in all words (Trie size)

## Key Concepts

### Why Trie + Backtracking?

**Naive approach**: For each word, do Word Search I (backtracking on grid)
- Time: O(W * R * C * 4^L) where W = number of words

**Trie approach**: Build Trie once, search all words simultaneously
- Time: O(R * C * 3^L) - much better!

The Trie lets us **share prefix checks** across multiple words.

### Algorithm Flow

```
1. Build Trie from all words
2. For each cell (r, c) on board:
   - DFS from (r, c), guided by Trie
   - If we reach a node where word != None, found a word!
   - Backtrack and continue searching
3. Return all found words
```

### Critical Optimization: Leaf Node Pruning

```python
# After backtracking, remove empty branches
if not nxt.children:
    node.children.pop(ch, None)
```

**Why this matters:**

```
Words: ["oath", "oat"]
After finding "oath":
  - Node for 'h' has no children
  - Remove 'h' from 't's children
  - Now searching for any word starting with "oath..." is skipped!

After finding "oat":
  - Node for 't' now has no children (we removed 'h')
  - Remove 't' from 'a's children
  - Continue pruning up the tree
```

This optimization can **dramatically** reduce search time, especially when:
- Many words share prefixes
- Grid has many potential paths

### Avoid Duplicates: `nxt.word = None`

```python
if nxt.word is not None:
    ans.append(nxt.word)
    nxt.word = None  # Mark as found
```

If the same word can be formed from multiple paths, we only want to add it once.

### Backtracking Template

```python
board[r][c] = '#'      # 1. Mark as visited

# 2. Explore neighbors
for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
    nr, nc = r + dr, c + dc
    if valid(nr, nc) and board[nr][nc] != '#':
        dfs(nr, nc, nxt)

board[r][c] = ch       # 3. Restore (backtrack)
```

### `__slots__` Optimization

```python
class TrieNode:
    __slots__ = ("children", "word")
```

This Python optimization:
- Reduces memory usage per node
- Speeds up attribute access
- Prevents accidental attribute creation

### Visual Example

```
Board:          Trie for ["eat", "oath"]:
o a a n              root
e t a e             /    \
i h k r            e      o
i f l v            |      |
                   a      a
                   |      |
                   t*     t
                          |
                          h*

Starting from (1,1) 't':
- Can't match (no 't' branch from root)

Starting from (0,0) 'o':
- Match 'o' -> go to 'o' node
- At (1,0) 'e': no 'e' child of 'o', backtrack
- At (0,1) 'a': match! go to 'a' node
- Continue... eventually find "oath"
```

### Time Complexity Breakdown

| Component | Complexity | Explanation |
|-----------|------------|-------------|
| Build Trie | O(W * L) | W words, L avg length |
| DFS per cell | O(3^L) | 3 directions (not going back) |
| Total cells | O(R * C) | Visit each as start |
| **Total** | O(R * C * 3^L) | After Trie is built |

## Related Problems

- [79. Word Search](https://leetcode.com/problems/word-search/) - Single word version
- [208. Implement Trie](../208.%20Implement%20Trie%20(Prefix%20Tree)/) - Basic Trie
- [211. Design Add and Search Words](../211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure/) - Trie with wildcards
