# 102. Binary Tree Level Order Traversal

## Problem Description

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example:**
```
    3
   / \
  9  20
    /  \
   15   7

Output: [[3], [9, 20], [15, 7]]
```

## Solution: BFS with Queue

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    ans = []
    q = deque([root])
    while q:
        temp = []
        for _ in range(len(q)):
            node = q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(temp)
    return ans
```

**Complexity:**
- **Time:** `O(n)` - visit each node exactly once
- **Space:** `O(n)` - queue can hold up to n/2 nodes (widest level)

## Key Concepts

### The BFS Level-by-Level Pattern

The key technique is **processing one entire level before moving to the next**:

```python
for _ in range(len(q)):  # Process EXACTLY this many nodes
    node = q.popleft()
    # ... add children to queue
```

Why `range(len(q))`? At the start of each iteration, `len(q)` equals the number of nodes in the current level. We process exactly that many, then the queue contains only the next level.

### Visual Execution

```
    3          Initial: q = [3]
   / \
  9  20        Level 0: process 1 node -> q = [9, 20]
    /  \
   15   7      Level 1: process 2 nodes -> q = [15, 7]
               Level 2: process 2 nodes -> q = []

Result: [[3], [9, 20], [15, 7]]
```

### Template for BFS Level Order

```python
def bfs_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Snapshot current level size
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)  # Process node
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result
```

### Variations of Level Order Traversal

| Problem | Modification |
|---------|-------------|
| **Level Order** (this) | Collect all nodes per level |
| **Right Side View** | Only keep last node of each level |
| **Left Side View** | Only keep first node of each level |
| **Zigzag Order** | Alternate direction each level |
| **Level Order Bottom** | Reverse the final result |
| **Average of Levels** | Compute average instead of collecting |

### Why Deque?

```python
from collections import deque
q = deque([root])

node = q.popleft()  # O(1) - deque is optimized for this
```

Using a regular list with `pop(0)` would be O(n) for each removal!

### DFS Alternative (For Reference)

```python
def levelOrder(self, root):
    levels = []
    
    def dfs(node, level):
        if not node:
            return
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return levels
```

This DFS approach also works but BFS is more intuitive for level-based problems.

## Related Problems

- [199. Binary Tree Right Side View](../199.%20Binary%20Tree%20Right%20Side%20View/) - Keep only last element per level
- [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Bottom-up
- [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) - Alternating directions
- [104. Maximum Depth of Binary Tree](../104.%20Maximum%20Depth%20of%20Binary%20Tree/) - BFS can count levels
