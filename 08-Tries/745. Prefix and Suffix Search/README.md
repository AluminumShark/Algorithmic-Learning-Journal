# 745. Prefix and Suffix Search

## Problem Description

Design a special dictionary that searches words by a prefix and a suffix.

Implement the `WordFilter` class:
- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
- `f(string pref, string suff)` Returns the index of the word in the dictionary that has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return the **largest** of them. If there is no such word, return `-1`.

**Example:**
```
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0
// "apple" has prefix "a" and suffix "e"
```

## Solution: Hash Map with All Combinations

```python
class WordFilter:
    def __init__(self, words: List[str]):
        self.mp = {}
        for idx, w in enumerate(words):
            L = len(w)
            prefixes = [w[:i] for i in range(L + 1)]
            suffixes = [w[j:] for j in range(L + 1)]

            for p in prefixes:
                for s in suffixes:
                    self.mp[p + '#' + s] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.mp.get(pref + '#' + suff, -1)
```

**Complexity:**
- **Time:** 
  - Constructor: O(N * L^3) where N = number of words, L = max word length
  - `f()`: O(1) hash lookup
- **Space:** O(N * L^3) for storing all combinations

## Key Concepts

### The Strategy: Precompute All Combinations

Instead of using a traditional Trie, we **precompute all possible prefix+suffix pairs** and store them in a hash map.

For word "apple" (index 0):
```
Prefixes: "", "a", "ap", "app", "appl", "apple"
Suffixes: "", "e", "le", "ple", "pple", "apple"

Generate all combinations:
"#"        -> 0
"#e"       -> 0
"#le"      -> 0
"a#"       -> 0
"a#e"      -> 0
"a#le"     -> 0
"ap#"      -> 0
"ap#e"     -> 0
...
"apple#apple" -> 0
```

### Why This Works

| Query | Key | Result |
|-------|-----|--------|
| f("a", "e") | "a#e" | 0 |
| f("ap", "le") | "ap#le" | 0 |
| f("", "e") | "#e" | 0 |
| f("x", "y") | "x#y" | -1 |

The `#` separator ensures no collision between prefix and suffix.

### Handling Duplicates / Largest Index

```python
for idx, w in enumerate(words):
    ...
    self.mp[p + '#' + s] = idx  # Later indices overwrite earlier ones
```

Since we iterate in order, if the same combination appears for multiple words, the **largest index** is kept (last write wins).

### Space/Time Trade-off

| Approach | Constructor | Query | Space |
|----------|-------------|-------|-------|
| Hash Map (this) | O(N * L^3) | O(1) | O(N * L^3) |
| Two Tries + Filter | O(N * L) | O(N * L) | O(N * L) |
| Wrapped Trie | O(N * L^2) | O(L) | O(N * L^2) |

This solution prioritizes **O(1) query time** at the cost of more preprocessing space.

### Why L^3?

For a word of length L:
- Number of prefixes: L + 1
- Number of suffixes: L + 1
- Combinations: (L + 1)^2
- Each combination string length: up to 2L

Total per word: O(L^2 * L) = O(L^3)

### Alternative: Wrapped Suffix Trie

A more space-efficient approach uses a Trie where each word is stored as:
```
suffix + '#' + word

For "apple":
Insert: "apple#apple", "pple#apple", "ple#apple", "le#apple", "e#apple", "#apple"

Query f("ap", "le"):
Search for: "le#ap" as a prefix in the Trie
```

This reduces space to O(N * L^2) but increases query time.

### Edge Cases

| Input | Behavior |
|-------|----------|
| Empty prefix `f("", "e")` | Valid, uses "#e" |
| Empty suffix `f("a", "")` | Valid, uses "a#" |
| Both empty `f("", "")` | Valid, uses "#" |
| Same word multiple times | Returns largest index |

### Implementation Notes

```python
# Generate all prefixes including empty string
prefixes = [w[:i] for i in range(L + 1)]  # "", "a", "ap", ...

# Generate all suffixes including empty string
suffixes = [w[j:] for j in range(L + 1)]  # "apple", "pple", ..., ""
```

## Related Problems

- [208. Implement Trie](../208.%20Implement%20Trie%20(Prefix%20Tree)/) - Basic Trie
- [211. Design Add and Search Words](../211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure/) - Trie with wildcards
- [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) - Trie for autocomplete
