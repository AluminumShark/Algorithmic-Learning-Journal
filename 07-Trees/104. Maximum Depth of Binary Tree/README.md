# 104. Maximum Depth of Binary Tree

## Problem Description

Given the `root` of a binary tree, return its **maximum depth**.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example:**
```
    3
   / \
  9  20
    /  \
   15   7

Output: 3
```

## Solutions

Like [226. Invert Binary Tree](../226.%20Invert%20Binary%20Tree/), this problem can be solved with **any traversal method** because we simply need to visit every node and track the maximum depth seen.

### Solution 1: BFS (Level Order Traversal)

Count the number of levels by processing nodes level-by-level.

```python
q = deque([root])
level = 0
while q:
    for _ in range(len(q)):  # Process entire level
        node = q.popleft()
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    level += 1
return level
```

**Key Insight:** After the while loop ends, `level` equals the number of levels = max depth.

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)` - widest level can have n/2 nodes

### Solution 2: Recursive DFS

The most elegant solution. The depth of a tree is `1 + max(left_depth, right_depth)`.

```python
def dfs(node):
    if not node:
        return 0
    return max(dfs(node.left), dfs(node.right)) + 1
```

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)` - recursion stack

### Solution 3: Iterative DFS (Stack with Depth Tracking)

Uses a stack storing `[node, depth]` pairs.

```python
stack = [[root, 1]]
ans = 0
while stack:
    node, depth = stack.pop()
    ans = max(ans, depth)
    if node.left: stack.append([node.left, depth + 1])
    if node.right: stack.append([node.right, depth + 1])
```

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)`

## Key Concepts

### Any Traversal Works!

All three approaches visit every node and track the maximum depth:

| Method | How Depth is Tracked |
|--------|---------------------|
| BFS | Count levels explicitly |
| Recursive DFS | Return depth from children, add 1 |
| Iterative DFS | Store depth alongside each node |

### BFS vs DFS for Depth Problems

| Scenario | Better Choice | Why |
|----------|--------------|-----|
| Find max depth | Both work | Same time complexity |
| Find min depth | BFS | Can return early when first leaf found |
| Wide tree | DFS | BFS uses O(width) space |
| Deep tree | BFS | DFS may stack overflow |

### Recursive Formula

```
depth(node) = 0                                  if node is null
            = 1 + max(depth(left), depth(right))  otherwise
```

This is a classic example of **bottom-up DFS** where:
- Base case returns a value (0)
- Each node combines children's results and adds its contribution (+1)

## Comparison of Approaches

| Aspect | Recursive DFS | Iterative DFS | BFS |
|--------|--------------|---------------|-----|
| Intuition | Natural recursion | Explicit tracking | Level counting |
| Code Length | Shortest | Medium | Medium |
| Best For | Interviews | Avoiding recursion | Finding min depth |

## Related Problems

- [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

