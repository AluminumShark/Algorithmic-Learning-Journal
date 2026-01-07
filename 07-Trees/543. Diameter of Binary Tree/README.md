# 543. Diameter of Binary Tree

## Problem Description

Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the **length of the longest path** between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the **number of edges** between them.

**Example:**
```
    1
   / \
  2   3
 / \
4   5

Output: 3
Explanation: The longest path is [4,2,1,3] or [5,2,1,3], both with 3 edges.
```

## Solution: Post-order DFS with Global State

### The Key Insight

This problem requires tracking **two different things**:

| What | Used For | How |
|------|----------|-----|
| **Height** | Parent needs it to calculate its height | Returned from DFS |
| **Diameter** | Final answer, could be at any node | Updated via `nonlocal` |

### Why Return Height but Track Diameter?

```python
def dfs(node):
    nonlocal ans
    if not node: return 0
    
    left = dfs(node.left)    # Height of left subtree
    right = dfs(node.right)  # Height of right subtree
    
    ans = max(ans, left + right)  # Diameter THROUGH this node
    
    return max(left, right) + 1   # Height OF this node
```

**The diameter through node X** = `left_height + right_height`
- This counts edges: going down left + going down right

**The height of node X** = `max(left_height, right_height) + 1`
- Parent needs this to calculate its own height

### Visual Example

```
        1          height=3
       / \
      2   3        height of 2 = 2, height of 3 = 1
     / \
    4   5          height = 1
```

At node 2:
- `left_height = 1` (from node 4)
- `right_height = 1` (from node 5)
- Diameter through node 2 = `1 + 1 = 2`
- Height returned to node 1 = `max(1, 1) + 1 = 2`

At node 1:
- `left_height = 2` (from node 2)
- `right_height = 1` (from node 3)
- Diameter through node 1 = `2 + 1 = 3` ← **This is the answer!**

### Why `nonlocal`?

The maximum diameter might occur at **any node**, not necessarily the root. We need a way to track the global maximum across all recursive calls.

```python
ans = 0  # Outer scope

def dfs(node):
    nonlocal ans  # Allow modification of outer variable
    ...
    ans = max(ans, left + right)  # Update global max
```

**Alternative:** Use a class variable or return a tuple `(height, diameter)`.

## Complexity Analysis

- **Time:** `O(n)` - visit each node exactly once
- **Space:** `O(n)` - recursion stack (O(h) for balanced tree)

## Key Concepts

### The "Return One, Track Another" Pattern

This is a common pattern in tree problems:

| Problem | Return | Track (Side Effect) |
|---------|--------|---------------------|
| Diameter | Height | Max diameter |
| Max Path Sum | Path from root | Max path sum |
| Balanced Tree | Height | Is balanced |

### Post-order Traversal

This solution uses **post-order traversal** (process children before parent) because:
- We need children's heights before we can calculate parent's diameter
- Bottom-up computation is natural for tree metrics

### Common Mistakes

1. **Confusing height and diameter**
   - Height: longest path **downward** from a node
   - Diameter: longest path **through** a node (left + right)

2. **Forgetting diameter might not pass through root**
   ```
       1
      /
     2
    / \
   3   4
   ```
   Here, the diameter is at node 2, not at root 1.

3. **Counting nodes instead of edges**
   - Diameter = number of **edges**, not nodes
   - A path of 4 nodes has 3 edges

## Related Problems

- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (Hard version)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

