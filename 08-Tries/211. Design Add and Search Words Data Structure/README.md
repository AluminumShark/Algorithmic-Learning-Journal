# 211. Design Add and Search Words Data Structure

## Problem Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

**Example:**
```
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True (matches "bad", "dad", "mad")
wordDictionary.search("b.."); // return True (matches "bad")
```

## Solution: Trie + DFS Backtracking

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.end
            
            ch = word[i]

            if ch == '.':
                return any(dfs(i + 1, child) for child in node.children.values())
            
            if ch not in node.children:
                return False
            
            return dfs(i + 1, node.children[ch])
        
        return dfs(0, self.root)
```

**Complexity:**
- **Time:** 
  - `addWord`: O(L) where L = word length
  - `search`: O(26^k * L) worst case, where k = number of '.' in the pattern
- **Space:** O(L) for recursion stack

## Key Concepts

### The Wildcard Challenge

The `.` character can match **any** letter. This means when we encounter a `.`, we must explore **all possible branches**:

```python
if ch == '.':
    return any(dfs(i + 1, child) for child in node.children.values())
```

### DFS Backtracking for Wildcards

```
Trie after adding "bad", "dad", "mad":

        root
       / | \
      b  d  m
      |  |  |
      a  a  a
      |  |  |
      d  d  d
    (end)(end)(end)

Search ".ad":
- At root, '.' matches any -> try 'b', 'd', 'm'
- For each: check if "ad" exists
- At least one succeeds -> return True
```

### Search Logic Flow

```python
def dfs(i, node):
    # Base case: reached end of pattern
    if i == len(word):
        return node.end
    
    ch = word[i]

    # Wildcard: try ALL children
    if ch == '.':
        return any(dfs(i + 1, child) for child in node.children.values())
    
    # Regular char: follow specific path
    if ch not in node.children:
        return False
    
    return dfs(i + 1, node.children[ch])
```

### Time Complexity Analysis

| Pattern | Time Complexity | Explanation |
|---------|----------------|-------------|
| "abc" | O(L) | Direct traversal |
| ".bc" | O(26 * L) | One wildcard at start |
| "..." | O(26^3) | Three wildcards |
| General | O(26^k * L) | k wildcards |

Worst case is when the pattern is all dots: "......" (k dots)

### Why `any()` Instead of Loop?

```python
# Using any() - short circuits on first True
return any(dfs(i + 1, child) for child in node.children.values())

# Equivalent to:
for child in node.children.values():
    if dfs(i + 1, child):
        return True
return False
```

`any()` is more Pythonic and automatically short-circuits.

### Edge Cases

| Input | Result | Reason |
|-------|--------|--------|
| `search("")` on empty dict | False | No words added |
| `search(".")` | True if any single-char word exists | Matches any char |
| `addWord("")` then `search("")` | True | Empty string is valid |

## Related Problems

- [208. Implement Trie](../208.%20Implement%20Trie%20(Prefix%20Tree)/) - Basic Trie operations
- [212. Word Search II](../212.%20Word%20Search%20II/) - Trie + grid backtracking
- [79. Word Search](https://leetcode.com/problems/word-search/) - Single word search in grid
