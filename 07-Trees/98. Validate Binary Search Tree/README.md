# 98. Validate Binary Search Tree

## Problem Description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**
```
    2
   / \
  1   3

Output: true
```

**Example 2:**
```
    5
   / \
  1   4
     / \
    3   6

Output: false
(3 is in right subtree of 5, but 3 < 5)
```

## Solution: DFS with Valid Range

```python
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
    return dfs(root, float('-inf'), float('inf'))
```

**Complexity:**
- **Time:** `O(n)` - visit each node exactly once
- **Space:** `O(h)` - recursion stack depth equals tree height

## Key Concepts

### The "Valid Range" Propagation

Every node must satisfy: `low < node.val < high`

When we move down the tree, we **narrow the valid range**:

| Direction | How Range Changes |
|-----------|------------------|
| Go Left | `high` becomes `node.val` (must be < parent) |
| Go Right | `low` becomes `node.val` (must be > parent) |

```python
dfs(node.left, low, node.val)   # Left: update upper bound
dfs(node.right, node.val, high)  # Right: update lower bound
```

### Why Simple Parent Check Fails

A common mistake is to only check against the immediate parent:

```python
# WRONG! This doesn't work
def isValidBST(root):
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    # ...
```

Counter-example:
```
    5
   / \
  1   4      ← 4 < 5, passes parent check
     / \
    3   6    ← 3 is in RIGHT subtree of 5, but 3 < 5!
```

The node `3` passes the check against its parent `4`, but violates the BST property with respect to the root `5`.

### Visual Range Propagation

```
        5                 Range: (-∞, +∞)
       / \
      1   6               1: (-∞, 5) ✓    6: (5, +∞) ✓
     / \   \
    0   2   7             0: (-∞, 1) ✓    7: (6, +∞) ✓
                          2: (1, 5) ✓

Each node must be within its range!
```

### Alternative: In-order Traversal

BST in-order traversal produces sorted values. If we find any value ≤ previous, it's invalid:

```python
def isValidBST(self, root):
    self.prev = float('-inf')
    
    def inorder(node):
        if not node:
            return True
        if not inorder(node.left):
            return False
        if node.val <= self.prev:
            return False
        self.prev = node.val
        return inorder(node.right)
    
    return inorder(root)
```

### Comparison of Approaches

| Approach | Idea | Pros |
|----------|------|------|
| Range DFS | Pass valid (low, high) | Clean, intuitive |
| In-order | Check if sorted | Uses BST property directly |
| Iterative | Stack-based | Avoids recursion |

### Edge Cases

| Case | Result |
|------|--------|
| Empty tree | `True` |
| Single node | `True` |
| Duplicate values | `False` (BST requires strict inequality) |
| Integer overflow | Use `float('-inf')` and `float('inf')` |

## Related Problems

- [1448. Count Good Nodes](../1448.%20Count%20Good%20Nodes%20in%20Binary%20Tree/) - Similar path-passing pattern
- [230. Kth Smallest Element in BST](../230.%20Kth%20Smallest%20Element%20in%20a%20BST/) - Uses in-order traversal
- [235. Lowest Common Ancestor of BST](../235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/) - BST value comparison
