# 208. Implement Trie (Prefix Tree)

## Problem Description

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the `Trie` class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Example:**
```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## Solution: Nested Hash Maps

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
```

**Complexity:**
- **Time:** `O(L)` for all operations, where L = length of word/prefix
- **Space:** `O(S)` where S = total characters stored across all words

## Key Concepts

### Trie Structure

A Trie is a tree where:
- Each node represents a **character**
- Each path from root to a node represents a **prefix**
- Nodes marked with `end = True` represent **complete words**

```
After inserting: "apple", "app", "ape"

        root
         |
         a
         |
         p
        / \
       p   e (end)
       |
       l
       |
       e (end)

Words: "ape" ends at 'e' (depth 3)
       "app" ends at second 'p' (depth 3)
       "apple" ends at 'e' (depth 5)
```

### TrieNode Design

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.end = False    # True if this node marks end of a word
```

Two key attributes:
1. **children**: Dictionary mapping characters to child nodes
2. **end**: Boolean flag indicating if this node completes a word

### search() vs startsWith()

| Method | Returns True When |
|--------|------------------|
| `search("app")` | "app" was inserted as a complete word |
| `startsWith("app")` | Any word starting with "app" exists |

The only difference in implementation:
```python
# search: must be a complete word
return cur.end

# startsWith: just needs to exist as a prefix
return True
```

### Why Hash Map (Dict) for Children?

| Implementation | Pros | Cons |
|---------------|------|------|
| Dict/HashMap | O(1) lookup, flexible charset | Slightly more memory |
| Array[26] | Faster for a-z only | Fixed to lowercase letters |

For interview problems, Dict is usually preferred for flexibility.

### Alternative: Array-based Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # For a-z only
        self.end = False
    
    def get_child(self, c):
        return self.children[ord(c) - ord('a')]
    
    def set_child(self, c, node):
        self.children[ord(c) - ord('a')] = node
```

### Common Trie Applications

| Application | How Trie Helps |
|-------------|---------------|
| Autocomplete | Find all words with given prefix |
| Spell checker | Search + suggest similar words |
| IP routing | Longest prefix matching |
| Word games | Fast dictionary lookup |

## Related Problems

- [211. Design Add and Search Words](../211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure/) - Trie + wildcard search
- [212. Word Search II](../212.%20Word%20Search%20II/) - Trie + backtracking
- [745. Prefix and Suffix Search](../745.%20Prefix%20and%20Suffix%20Search/) - Advanced Trie application
