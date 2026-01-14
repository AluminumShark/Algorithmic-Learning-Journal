# 124. Binary Tree Maximum Path Sum

## Problem Description

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any **non-empty** path.

**Example 1:**
```
    1
   / \
  2   3

Output: 6 (path: 2 -> 1 -> 3)
```

**Example 2:**
```
   -10
   /  \
  9   20
     /  \
    15   7

Output: 42 (path: 15 -> 20 -> 7)
```

## Solution: Post-order DFS with Global Maximum

```python
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.ans = float('-inf')

    def dfs(node):
        if not node:
            return 0
        
        # Max gain from subtrees, ignore if negative
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # Update global maximum (Path can curve through root)
        self.ans = max(self.ans, left + right + node.val)

        # Return max path extending to parent (Must choose one side)
        return node.val + max(left, right)
    
    dfs(root)
    return self.ans
```

**Complexity:**
- **Time:** `O(n)` - visit each node once
- **Space:** `O(h)` - recursion stack depth

## Key Concepts

### The Critical Distinction: "Arch" vs "Straight" Paths

This is the **most important concept** in this problem:

```
        node
       /    \
     left   right

"Arch" path:    left <- node -> right  (curves through node)
"Straight" path: left <- node  OR  node -> right (extends to parent)
```

| Path Type | Formula | When Used |
|-----------|---------|-----------|
| **Arch** | `left + node + right` | Update global max (path ends here) |
| **Straight** | `node + max(left, right)` | Return to parent (path continues up) |

### Why Can't We Return the "Arch" Path?

```
       parent
         |
        node      <- If we include BOTH left and right...
       /    \
     left   right

We CAN'T also go up to parent! That would create a fork, not a path.
```

A valid path must be a **single connected line**. If we "arch" through a node (using both children), we cannot extend further upward.

### The `max(0, ...)` Clamping

```python
left = max(0, dfs(node.left))
right = max(0, dfs(node.right))
```

Why clamp to 0? **If a subtree sum is negative, don't include it!**

```
    5
   /
 -10     <- Including this makes sum worse
 /
3

Best path from 5: just [5], not [5, -10, 3]
```

### Visual Walkthrough

```
   -10
   /  \
  9   20
     /  \
    15   7

DFS Post-order:
1. Node 9:  left=0, right=0
            arch = 0+9+0 = 9, update ans=9
            return 9

2. Node 15: left=0, right=0
            arch = 0+15+0 = 15, update ans=15
            return 15

3. Node 7:  left=0, right=0
            arch = 0+7+0 = 7, ans stays 15
            return 7

4. Node 20: left=15, right=7
            arch = 15+20+7 = 42, update ans=42 (max!)
            return 20+max(15,7) = 35

5. Node -10: left=9, right=35
             arch = 9+(-10)+35 = 34, ans stays 42
             return -10+max(9,35) = 25

Final answer: 42
```

### Common Mistakes

1. **Forgetting negative values**: Initialize `ans = float('-inf')`, not 0
2. **Not clamping to 0**: Negative subtrees should be excluded
3. **Returning arch instead of straight**: Can't fork paths

### Similar Pattern: Diameter of Binary Tree

```python
# 543. Diameter - same pattern!
def diameterOfBinaryTree(root):
    self.ans = 0
    def dfs(node):
        if not node: return 0
        left = dfs(node.left)
        right = dfs(node.right)
        self.ans = max(self.ans, left + right)  # "Arch" path (edges)
        return max(left, right) + 1             # "Straight" path
    dfs(root)
    return self.ans
```

| Problem | What We're Maximizing | Arch Formula | Return Formula |
|---------|----------------------|--------------|----------------|
| Max Path Sum | Node values | L + node + R | node + max(L, R) |
| Diameter | Edge count | L + R | max(L, R) + 1 |

## Related Problems

- [543. Diameter of Binary Tree](../543.%20Diameter%20of%20Binary%20Tree/) - Same arch vs straight pattern
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) - Similar DFS pattern
- [1448. Count Good Nodes](../1448.%20Count%20Good%20Nodes%20in%20Binary%20Tree/) - Another DFS with global tracking
