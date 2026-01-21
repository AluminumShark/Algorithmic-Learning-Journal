# 17. Letter Combinations of a Phone Number

## Problem Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons):

```
2 -> abc    3 -> def    4 -> ghi
5 -> jkl    6 -> mno    7 -> pqrs
8 -> tuv    9 -> wxyz
```

**Example:**
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Solution: Mapping + Backtracking

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []  # IMPORTANT: Handle empty input!
            
        cur, res = [], []
        mp = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def dfs(i):
            if i == len(digits):
                res.append(''.join(cur))
                return
            
            chs = mp[digits[i]]

            for j in range(len(chs)):
                cur.append(chs[j])
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res
```

**Complexity:**
- **Time:** O(4^N * N) where N = number of digits (4 because some digits map to 4 letters)
- **Space:** O(N) - recursion depth

## Key Concepts

### Handle Empty Input!

```python
if not digits:
    return []  # NOT return [""]
```

This is a common edge case. Without this check, the code would return `[""]` (a list with one empty string), not `[]` (an empty list).

### The Mapping

```python
mp = {
    '2': 'abc',  '3': 'def',  '4': 'ghi',
    '5': 'jkl',  '6': 'mno',  '7': 'pqrs',
    '8': 'tuv',  '9': 'wxyz'
}
```

Note: 7 and 9 have **4 letters** (pqrs, wxyz), others have 3.

### Decision Tree for "23"

```
digits = "23"

                    dfs(0)
                  digits[0] = '2' -> "abc"
            /          |          \
           a           b           c
        dfs(1)      dfs(1)      dfs(1)
      '3'->"def"  '3'->"def"  '3'->"def"
      / | \       / | \       / | \
     d  e  f     d  e  f     d  e  f
    
Results: ad, ae, af, bd, be, bf, cd, ce, cf
```

### The Core Pattern

```python
chs = mp[digits[i]]        # Get letters for current digit

for j in range(len(chs)):  # Try each letter
    cur.append(chs[j])     # Choose
    dfs(i + 1)             # Explore next digit
    cur.pop()              # Unchoose (backtrack)
```

This is the standard backtracking template applied to string generation.

### Why 4^N?

- Each digit maps to 3-4 letters
- Worst case: all digits are 7 or 9 (4 letters each)
- N digits -> 4^N combinations maximum

For "234": 3 * 3 * 3 = 27 combinations
For "79":  4 * 4 = 16 combinations

### Alternative: Iterative BFS-like Approach

```python
def letterCombinations(digits):
    if not digits:
        return []
    
    mp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
          '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    
    result = ['']
    for digit in digits:
        result = [prefix + ch for prefix in result for ch in mp[digit]]
    return result
```

This builds combinations iteratively by expanding each existing prefix.

### Alternative: More Pythonic

```python
from itertools import product

def letterCombinations(digits):
    if not digits:
        return []
    mp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
          '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    return [''.join(p) for p in product(*[mp[d] for d in digits])]
```

Using `itertools.product` for Cartesian product.

### Comparison: Three Approaches

| Approach | Pros | Cons |
|----------|------|------|
| Backtracking | Classic pattern, low space | More code |
| Iterative | Easy to understand | O(4^N) space for intermediate results |
| itertools | Shortest code | Less educational |

## Related Problems

- [22. Generate Parentheses](../22.%20Generate%20Parentheses/) - Similar generation pattern
- [46. Permutations](../46.%20Permutations/) - Backtracking template
- [77. Combinations](https://leetcode.com/problems/combinations/) - Choose k elements
