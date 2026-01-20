# 22. Generate Parentheses

## Problem Description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```

## Solution: Constraint-based Backtracking

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur, res = [], []
        def dfs(open, close):
            if open == n and close == n:
                res.append(''.join(cur))
                return
            
            if open < n:
                cur.append('(')
                dfs(open + 1, close)
                cur.pop()
            
            if close < open:
                cur.append(')')
                dfs(open, close + 1)
                cur.pop()
        dfs(0, 0)
        return res
```

**Complexity:**
- **Time:** O(C_n * n) where C_n is the nth Catalan number
- **Space:** O(n) - recursion depth

## Key Concepts

### The Two Validity Constraints

For parentheses to be valid:

1. **`open < n`**: Can add `(` only if we haven't used all n open parens
2. **`close < open`**: Can add `)` only if there are unmatched open parens

```python
if open < n:        # Constraint 1: don't exceed n opens
    add '('
    
if close < open:    # Constraint 2: must have unmatched '(' to close
    add ')'
```

### Why `close < open` (not `close < n`)?

At any point, if `close >= open`, adding `)` would create invalid sequence:

```
open=1, close=1: "()"
  - Adding ')' -> "())" is INVALID!
  
open=2, close=1: "(()"
  - Adding ')' -> "(())" is VALID
```

### Decision Tree for n=2

```
                    "", open=0, close=0
                           |
                          (      <- open < 2, can add (
                    "(", open=1, close=0
                   /              \
                  (                )      <- close < open=1, can add )
           "((", o=2, c=0      "()", o=1, c=1
              |                      |
              )                      (      <- open < 2, can add (
         "(()", o=2, c=1        "()(", o=2, c=1
              |                      |
              )                      )
         "(())", o=2, c=2       "()()", o=2, c=2
         
Results: ["(())", "()()"]
```

### Connection to Catalan Numbers

The number of valid parentheses combinations is the **nth Catalan number**:

```
C_n = (2n)! / ((n+1)! * n!)

n=1: C_1 = 1     ["()"]
n=2: C_2 = 2     ["(())", "()()"]
n=3: C_3 = 5     ["((()))", "(()())", "(())()", "()(())", "()()()"]
n=4: C_4 = 14
```

Catalan numbers appear in many combinatorial problems:
- Valid parentheses
- Binary trees with n nodes
- Paths in a grid staying below diagonal
- Ways to triangulate a polygon

### Alternative: String Concatenation

```python
def generateParenthesis(n):
    res = []
    def dfs(s, open, close):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open < n:
            dfs(s + '(', open + 1, close)
        if close < open:
            dfs(s + ')', open, close + 1)
    dfs('', 0, 0)
    return res
```

Simpler but creates new strings at each step (less efficient).

### Why This Generates ALL Valid Combinations

The two constraints exactly define validity:
1. Never have more open than n
2. Never close more than opened

Any valid string satisfies these at every prefix. By exploring all paths that maintain these constraints, we generate exactly all valid combinations.

### Complexity Deep Dive

- Number of valid combinations: C_n (Catalan number)
- Each combination has length 2n
- Time to generate each: O(n) for the string join
- Total: O(C_n * n)

C_n grows as O(4^n / n^(3/2)), so overall time is approximately O(4^n / n^(1/2)).

## Related Problems

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Check if valid (stack)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) - DP or stack
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - BFS/Backtracking
