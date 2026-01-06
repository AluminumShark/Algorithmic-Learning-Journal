# 144. Binary Tree Preorder Traversal

## Problem Description

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

**Preorder traversal** visits nodes in the following order:
1. **Root** (current node)
2. **Left** subtree
3. **Right** subtree

## Solutions

### Solution 1: Recursive

The recursive approach directly follows the definition of preorder traversal.

```python
def dfs(node):
    if not node: return
    res.append(node.val)  # Visit root first
    dfs(node.left)        # Then left subtree
    dfs(node.right)       # Then right subtree
```

**Complexity Analysis:**
- **Time:** `O(n)` - visit each node exactly once
- **Space:** `O(n)` - recursion stack depth (worst case for skewed tree)

### Solution 2: Iterative (Stack)

Uses a stack to simulate the recursion. The key insight is that we process the current node immediately, save the right child for later, and continue left.

**Algorithm:**
1. While we have a current node or items in stack:
   - Go as far left as possible, visiting each node and saving its right child
   - When we can't go left anymore, pop a saved right child and repeat

**Complexity Analysis:**
- **Time:** `O(n)`
- **Space:** `O(n)`

## Key Concepts

1. **Traversal Order**: Preorder = Root → Left → Right
2. **Stack Usage**: Save right children to process after completing left subtrees
3. **Recursive vs Iterative**: Both achieve the same result; iterative gives explicit control over the call stack

## Comparison of Tree Traversals

| Traversal | Order | Common Use Cases |
|-----------|-------|------------------|
| **Preorder** | Root → Left → Right | Copy tree, prefix expression |
| **Inorder** | Left → Root → Right | BST sorted order |
| **Postorder** | Left → Right → Root | Delete tree, postfix expression |

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)

