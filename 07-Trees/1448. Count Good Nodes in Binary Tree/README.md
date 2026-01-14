# 1448. Count Good Nodes in Binary Tree

## Problem Description

Given a binary tree `root`, a node X in the tree is named **good** if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

**Example 1:**
```
      3
     / \
    1   4
   /   / \
  3   1   5

Output: 4
Good nodes: 3 (root), 4, 3 (left-left), 5
Node 1 (left child of root) is NOT good because 3 > 1
Node 1 (left child of 4) is NOT good because 4 > 1
```

**Example 2:**
```
      3
     /
    3
   / \
  4   2

Output: 3
Good nodes: 3 (root), 3, 4
```

## Solution: Pre-order DFS with Path Maximum

```python
def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, cmx):
        if not node:
            return 0
        
        if node.val >= cmx:
            good = 1
        else:
            good = 0

        cmx = max(cmx, node.val)
        
        good += dfs(node.left, cmx)
        good += dfs(node.right, cmx)

        return good

    return dfs(root, root.val)
```

**Complexity:**
- **Time:** `O(n)` - visit each node exactly once
- **Space:** `O(h)` - recursion stack depth equals tree height (O(log n) balanced, O(n) skewed)

## Key Concepts

### The "Path Maximum" Passing Technique

The key insight is to **pass down the maximum value seen so far** along the path from root to current node:

```python
cmx = max(cmx, node.val)  # Update path maximum before going deeper
```

| Parameter | Meaning |
|-----------|---------|
| `node` | Current node being processed |
| `cmx` | Maximum value seen on path from root to this node's parent |

### Why Pre-order DFS?

We use **pre-order** (process node before children) because:
1. We need to check if current node is "good" **before** going deeper
2. We need to update `cmx` **before** passing to children

```
Process Order:
1. Check if node is good (compare with cmx)
2. Update cmx = max(cmx, node.val)
3. Recurse left
4. Recurse right
5. Return count
```

### Visual Walkthrough

```
      3          dfs(3, cmx=3): 3 >= 3, good=1
     / \                       cmx stays 3
    1   4        dfs(1, cmx=3): 1 < 3, good=0
   /   / \       dfs(4, cmx=3): 4 >= 3, good=1, cmx->4
  3   1   5      dfs(3, cmx=3): 3 >= 3, good=1
                 dfs(1, cmx=4): 1 < 4, good=0
                 dfs(5, cmx=4): 5 >= 4, good=1

Total: 1 + 0 + 1 + 1 + 0 + 1 = 4 good nodes
```

### Alternative: Cleaner One-liner Logic

```python
def dfs(node, cmx):
    if not node:
        return 0
    good = 1 if node.val >= cmx else 0
    cmx = max(cmx, node.val)
    return good + dfs(node.left, cmx) + dfs(node.right, cmx)
```

### Space Complexity: O(h) vs O(n)

| Tree Shape | Height (h) | Space |
|------------|-----------|-------|
| Balanced | O(log n) | O(log n) |
| Skewed (worst) | O(n) | O(n) |

The space is determined by the **recursion stack depth**, which equals the tree height.

### Similar "Path Passing" Problems

| Problem | What We Pass Down |
|---------|------------------|
| Good Nodes (this) | Maximum value on path |
| Validate BST | Valid range (low, high) |
| Path Sum | Remaining sum to find |
| Depth/Level | Current depth |

## Related Problems

- [98. Validate Binary Search Tree](../98.%20Validate%20Binary%20Search%20Tree/) - Pass range instead of max
- [112. Path Sum](https://leetcode.com/problems/path-sum/) - Pass remaining sum
- [104. Maximum Depth of Binary Tree](../104.%20Maximum%20Depth%20of%20Binary%20Tree/) - Track depth
