# 100. Same Tree

## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are **structurally identical**, and the nodes have the **same value**.

**Example 1:**
```
  p:     q:
   1      1
  / \    / \
 2   3  2   3

Output: true
```

**Example 2:**
```
  p:     q:
   1      1
  /        \
 2          2

Output: false (different structure)
```

**Example 3:**
```
  p:     q:
   1      1
  / \    / \
 2   1  1   2

Output: false (different values)
```

## Solution: Recursive DFS

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return False
```

**Complexity:**
- **Time:** `O(n)` - visit each node once (n = min nodes of the two trees)
- **Space:** `O(n)` - recursion stack (worst case for skewed tree)

## Key Concepts

### Three-Way Condition Check

At each recursive call, there are exactly three possible states:

| p | q | Result |
|---|---|--------|
| `None` | `None` | `True` - both empty, structurally same |
| `None` | Node | `False` - structure differs |
| Node | `None` | `False` - structure differs |
| Node | Node | Compare values, then recurse |

The code elegantly handles this:

```python
if not p and not q:           # Both null -> same
    return True
if p and q and p.val == q.val: # Both exist with same value -> check children
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
else:                          # All other cases -> not same
    return False
```

### Alternative Cleaner Version

```python
def isSameTree(self, p, q):
    if not p or not q:
        return p == q  # True only if both are None
    return (p.val == q.val and 
            self.isSameTree(p.left, q.left) and 
            self.isSameTree(p.right, q.right))
```

### Iterative BFS Solution

```python
def isSameTree(self, p, q):
    queue = deque([(p, q)])
    while queue:
        n1, n2 = queue.popleft()
        if not n1 and not n2:
            continue
        if not n1 or not n2 or n1.val != n2.val:
            return False
        queue.append((n1.left, n2.left))
        queue.append((n1.right, n2.right))
    return True
```

### Why This is a Fundamental Pattern

The `isSameTree` logic is reused in many tree problems:

| Problem | How isSameTree is Used |
|---------|----------------------|
| [572. Subtree of Another Tree](../572.%20Subtree%20of%20Another%20Tree/) | Check if a subtree matches |
| Symmetric Tree | Check `isSameTree(root.left, mirror(root.right))` |
| Find Duplicate Subtrees | Compare subtrees for equality |

## Related Problems

- [572. Subtree of Another Tree](../572.%20Subtree%20of%20Another%20Tree/) - Uses isSameTree as helper
- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) - Mirror version
- [110. Balanced Binary Tree](../110.%20Balanced%20Binary%20Tree/) - Another tree validation
