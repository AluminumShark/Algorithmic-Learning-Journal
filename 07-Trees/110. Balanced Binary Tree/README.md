# 110. Balanced Binary Tree

## Problem Description

Given a binary tree, determine if it is **height-balanced**.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**
```
    3
   / \
  9  20
    /  \
   15   7

Output: true
```

**Example 2:**
```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Output: false
```

## Solution: Bottom-up DFS

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        if left == -1:
            return -1
        
        right = dfs(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

    return dfs(root) != -1
```

**Complexity:**
- **Time:** `O(n)` - each node visited exactly once
- **Space:** `O(n)` - recursion stack (worst case for skewed tree)

## Key Concepts

### Bottom-up DFS with Failure Propagation

The key insight is using `-1` as a **sentinel value** to propagate failure up the tree:

| Return Value | Meaning |
|--------------|---------|
| `≥ 0` | Valid height of subtree |
| `-1` | Subtree is unbalanced |

This approach has two major benefits:

1. **Early Termination:** Once we detect an imbalance anywhere, we immediately propagate `-1` all the way up without doing any more work.

2. **Single Pass:** We compute height and check balance simultaneously, achieving `O(n)` time.

### Why Not Top-down?

A naive top-down approach would:
1. Check if current node is balanced (requires computing heights of both subtrees)
2. Recursively check left and right subtrees

```python
# Top-down: O(n²) time - DON'T USE
def isBalanced(root):
    if not root:
        return True
    left_height = getHeight(root.left)   # O(n)
    right_height = getHeight(root.right) # O(n)
    if abs(left_height - right_height) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)  # Recurse
```

This is `O(n²)` because `getHeight()` is called repeatedly for the same nodes.

### The -1 Propagation Pattern

```
        1
       / \
      2   2
     / \
    3   3
   / \
  4   4

DFS execution:
- Node 4 (left):  returns 1
- Node 4 (right): returns 1
- Node 3 (left):  left=1, right=1, balanced, returns 2
- Node 3 (right): left=0, right=0, balanced, returns 1
- Node 2 (left):  left=2, right=1, balanced, returns 3
- Node 2 (right): left=0, right=0, balanced, returns 1
- Node 1:         left=3, right=1, |3-1|=2 > 1, UNBALANCED!
                  returns -1

Final: dfs(root) == -1, so return False
```

### Comparison with Related Problems

| Problem | What We Return | Failure Signal |
|---------|---------------|----------------|
| Max Depth | height | N/A |
| Balanced Tree | height or -1 | -1 |
| Diameter | height (update global) | N/A |

## Related Problems

- [104. Maximum Depth of Binary Tree](../104.%20Maximum%20Depth%20of%20Binary%20Tree/) - Foundation for height calculation
- [543. Diameter of Binary Tree](../543.%20Diameter%20of%20Binary%20Tree/) - Similar bottom-up pattern
- [100. Same Tree](../100.%20Same%20Tree/) - Another tree validation problem
