# 226. Invert Binary Tree

## Problem Description

Given the `root` of a binary tree, invert the tree, and return its root.

**Example:**
```
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

## Solutions

This problem can be solved using **any traversal method** (DFS or BFS) because:
- We need to visit every node exactly once
- The operation (swapping children) is independent of traversal order
- No specific processing order is required

### Solution 1: Recursive DFS

The most intuitive approach. Recursively invert left and right subtrees, then swap them.

```python
def dfs(node):
    if not node:
        return None
    left = dfs(node.left)
    right = dfs(node.right)
    node.left = right
    node.right = left
    return node
```

**Complexity:**
- **Time:** `O(n)` - visit each node once
- **Space:** `O(n)` - recursion stack (O(h) for balanced, O(n) for skewed)

### Solution 2: Iterative DFS (Stack)

Uses explicit stack to simulate recursion.

```python
stack = [root]
while stack:
    node = stack.pop()
    node.left, node.right = node.right, node.left
    if node.right: stack.append(node.right)
    if node.left: stack.append(node.left)
```

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)`

### Solution 3: BFS (Queue)

Level-order traversal using a queue.

```python
queue = deque([root])
while queue:
    node = queue.popleft()
    node.left, node.right = node.right, node.left
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)` - up to n/2 nodes at the widest level

## Key Concepts

### Any Traversal Works!

| Traversal | Data Structure | When to Use |
|-----------|---------------|-------------|
| Recursive DFS | Call Stack | Most readable, good for interviews |
| Iterative DFS | Stack | When recursion depth is a concern |
| BFS | Queue | When you prefer level-by-level processing |

For this problem, all three achieve the same result because:
1. Every node must be visited
2. Swapping is a local operation (doesn't depend on other nodes)
3. The final tree structure is the same regardless of traversal order

### The Famous Tweet

This problem is famously associated with Max Howell's tweet:
> "Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so f*** off."

## Comparison: DFS vs BFS

| Aspect | DFS (Recursive) | DFS (Iterative) | BFS |
|--------|-----------------|-----------------|-----|
| Code Simplicity | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Space (Balanced) | O(log n) | O(log n) | O(n) |
| Space (Skewed) | O(n) | O(n) | O(1) |
| Stack Overflow Risk | Yes | No | No |

## Related Problems

- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)

