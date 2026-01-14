# 572. Subtree of Another Tree

## Problem Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants.

**Example 1:**
```
    root:          subRoot:
       3              4
      / \            / \
     4   5          1   2
    / \
   1   2

Output: true
```

**Example 2:**
```
    root:          subRoot:
       3              4
      / \            / \
     4   5          1   2
    / \              \
   1   2              0

Output: false (subRoot has extra node)
```

## Solution: Double Recursion

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Helper function (Same as isSameTree)
    def dfs(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return dfs(a.left, b.left) and dfs(a.right, b.right)

    if not subRoot:
        return True
    if not root:
        return False

    if dfs(root, subRoot):
        return True
    
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

**Complexity:**
- **Time:** `O(m × n)` worst case, where m = nodes in subRoot, n = nodes in root
- **Space:** `O(m + n)` - recursion stack depth

## Key Concepts

### Double Recursion Pattern

This problem requires **two layers of recursion**:

```
┌─────────────────────────────────────────────────────────┐
│  Outer Recursion: isSubtree()                           │
│  Purpose: Traverse every node in 'root'                 │
│  Time: O(n) - visits each node in root once             │
│                                                         │
│    ┌─────────────────────────────────────────────────┐  │
│    │  Inner Recursion: dfs() (isSameTree)            │  │
│    │  Purpose: Check if current subtree == subRoot   │  │
│    │  Time: O(m) - compares all nodes in subRoot     │  │
│    └─────────────────────────────────────────────────┘  │
│                                                         │
│  Total: O(n) × O(m) = O(n × m)                          │
└─────────────────────────────────────────────────────────┘
```

### Execution Flow

```
    root:          subRoot:
       3              4
      / \            / \
     4   5          1   2
    / \
   1   2

Step 1: isSubtree(root=3, subRoot)
        -> dfs(3, 4) -> 3 ≠ 4, return False
        -> Try left: isSubtree(root=4, subRoot)

Step 2: isSubtree(root=4, subRoot)
        -> dfs(4, 4) -> 4 == 4, match
          -> dfs(1, 1) -> 1 == 1, match
            -> dfs(None, None) -> True
            -> dfs(None, None) -> True
          -> dfs(2, 2) -> 2 == 2, match
            -> dfs(None, None) -> True
            -> dfs(None, None) -> True
        -> Return True!

Result: True (found matching subtree at node 4)
```

### Why O(m × n) Worst Case?

Consider when root is a skewed tree and every node has the same value as subRoot's root:

```
root:           subRoot:
    1               1
   /               /
  1               1
 /
1

Each node in root triggers a full dfs() comparison.
```

### Edge Cases

| root | subRoot | Result | Reason |
|------|---------|--------|--------|
| Any | `None` | `True` | Empty tree is subtree of everything |
| `None` | Any non-null | `False` | Can't find non-empty subtree in empty tree |
| Same tree | Same tree | `True` | A tree is its own subtree |

### Code Structure Breakdown

```python
def isSubtree(self, root, subRoot):
    # Edge case: empty subRoot is always a subtree
    if not subRoot:
        return True
    # Edge case: can't find subtree in empty root
    if not root:
        return False

    # Check if current root matches subRoot entirely
    if dfs(root, subRoot):
        return True
    
    # Otherwise, search in left or right subtree
    return self.isSubtree(root.left, subRoot) or \
           self.isSubtree(root.right, subRoot)
```

### Optimization: String Serialization

An alternative O(m + n) approach using tree serialization:

```python
def isSubtree(self, root, subRoot):
    def serialize(node):
        if not node:
            return "#"
        return f"^{node.val}#{serialize(node.left)}#{serialize(node.right)}"
    
    return serialize(subRoot) in serialize(root)
```

Note: The `^` prefix prevents false matches like node value `12` matching `2`.

## Related Problems

- [100. Same Tree](../100.%20Same%20Tree/) - The core helper function
- [652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/) - Uses serialization
- [110. Balanced Binary Tree](../110.%20Balanced%20Binary%20Tree/) - Another tree validation
