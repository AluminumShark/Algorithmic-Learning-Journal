# 131. Palindrome Partitioning

## Problem Description

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

**Example:**
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

## Solution: The "Cut Line" Strategy

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur, res = [], []
        
        def is_pal(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            
            # j defines the end of the current substring (the cut point)
            for j in range(i, len(s)):
                if is_pal(i, j):
                    cur.append(s[i : j + 1])
                    dfs(j + 1)
                    cur.pop()
        
        dfs(0)
        return res
```

**Complexity:**
- **Time:** O(N * 2^N) - 2^(N-1) ways to partition, O(N) to check palindrome
- **Space:** O(N) - recursion depth

## Key Concepts

### The "Cut Line" Visualization

**Think of it like cutting a cake:**

```
String: "a a b"
         0 1 2

The loop 'j' is like holding a knife, deciding where to make the cut.

j = 0: Cut after position 0
       [a | a b]  ->  "a" is palindrome? Yes! Take it, recurse on "ab"

j = 1: Cut after position 1
       [a a | b]  ->  "aa" is palindrome? Yes! Take it, recurse on "b"

j = 2: Cut after position 2
       [a a b |]  ->  "aab" is palindrome? No! Skip this cut.
```

### Step-by-Step for "aab"

```
dfs(0): Try cutting at different positions
        
        j=0: s[0:1]="a" is palindrome
             cur=["a"], dfs(1)
             
             dfs(1): j=1: s[1:2]="a" is palindrome
                          cur=["a","a"], dfs(2)
                          
                          dfs(2): j=2: s[2:3]="b" is palindrome
                                       cur=["a","a","b"], dfs(3)
                                       
                                       dfs(3): i==len(s), FOUND! ["a","a","b"]
                          
                     j=2: s[1:3]="ab" is NOT palindrome, skip
        
        j=1: s[0:2]="aa" is palindrome
             cur=["aa"], dfs(2)
             
             dfs(2): j=2: s[2:3]="b" is palindrome
                          cur=["aa","b"], dfs(3)
                          
                          dfs(3): i==len(s), FOUND! ["aa","b"]
        
        j=2: s[0:3]="aab" is NOT palindrome, skip

Result: [["a","a","b"], ["aa","b"]]
```

### The Core Logic

```python
for j in range(i, len(s)):    # Try every possible cut position
    if is_pal(i, j):          # If left piece is palindrome
        cur.append(s[i:j+1])  # Take it
        dfs(j + 1)            # Recurse on remaining string
        cur.pop()             # Backtrack
```

| Variable | Meaning |
|----------|---------|
| `i` | Start of current piece (left edge) |
| `j` | End of current piece (right edge / cut line) |
| `s[i:j+1]` | The piece we're cutting |
| `j + 1` | Start of next piece |

### Why Every Single Character is a Palindrome

This guarantees we always find at least one valid partition:

```
"abc" -> ["a", "b", "c"]  (always valid!)
```

Single characters are trivially palindromes, so the "cut after every character" solution always exists.

### Decision Tree Visualization

```
s = "aab"

                         dfs(0)
              /            |             \
         "a"             "aa"          "aab"(X)
        dfs(1)          dfs(2)
       /      \            |
     "a"     "ab"(X)      "b"
    dfs(2)               dfs(3)
      |                    |
     "b"               COMPLETE
    dfs(3)            ["aa","b"]
      |
  COMPLETE
["a","a","b"]
```

### Why 2^N Partitions?

For a string of length N, there are N-1 potential cut positions:

```
"a | a | b"
    ^   ^
    2 positions, each can be cut or not

2^(N-1) = 2^2 = 4 potential partitions
```

But we prune non-palindrome paths, so actual work is less.

### Optimization: Precompute Palindromes

```python
def partition(s):
    n = len(s)
    # dp[i][j] = True if s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
    
    # Then use dp[i][j] instead of is_pal(i, j)
```

This avoids repeated palindrome checks.

## Related Problems

- [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) - Min cuts (DP)
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) - Find longest
- [78. Subsets](../78.%20Subsets/) - Similar backtracking pattern
