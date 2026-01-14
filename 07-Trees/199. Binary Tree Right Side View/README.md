# 199. Binary Tree Right Side View

## Problem Description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

**Example 1:**
```
    1         ->  1
   / \
  2   3       ->  3
   \   \
    5   4     ->  4

Output: [1, 3, 4]
```

**Example 2:**
```
    1         ->  1
   /
  2           ->  2
 /
3             ->  3

Output: [1, 2, 3]
(Left side is visible when right is empty!)
```

## Solution: BFS - Last Node of Each Level

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
        
    q = deque([root])
    ans = []
    while q:
        end = len(q)
        for i in range(end):
            node = q.popleft()
            if i == end - 1:  # Last node in this level
                ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans
```

**Complexity:**
- **Time:** `O(n)` - visit each node once
- **Space:** `O(n)` - queue can hold up to n/2 nodes

## Key Concepts

### Right Side View = Last Element of Each BFS Level

This is essentially [102. Binary Tree Level Order Traversal](../102.%20Binary%20Tree%20Level%20Order%20Traversal/) with one modification: instead of collecting all nodes, we only keep the **last one**.

```
Level Order:        [[1], [2, 3], [5, 4]]
Right Side View:    [1, 3, 4]  <- last element of each level
```

### The Key Check

```python
if i == end - 1:  # Is this the last node in current level?
    ans.append(node.val)
```

We're iterating left-to-right through each level. The last node we see (`i == end - 1`) is the rightmost visible node.

### Alternative: Simplified Version

```python
def rightSideView(self, root):
    if not root:
        return []
    
    ans = []
    q = deque([root])
    while q:
        # Just grab the rightmost node directly
        ans.append(q[-1].val)
        
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans
```

Using `q[-1]` to peek at the last element before processing!

### DFS Alternative: Right-First Traversal

```python
def rightSideView(self, root):
    result = []
    
    def dfs(node, depth):
        if not node:
            return
        if depth == len(result):  # First node at this depth
            result.append(node.val)
        dfs(node.right, depth + 1)  # Go right FIRST
        dfs(node.left, depth + 1)
    
    dfs(root, 0)
    return result
```

By visiting right subtree first, the first node we encounter at each depth is the rightmost one!

### Left Side View (Bonus)

For left side view, just change which node to capture:

```python
# BFS: capture first instead of last
if i == 0:  # First node in level
    ans.append(node.val)

# DFS: visit left first
dfs(node.left, depth + 1)   # Go left FIRST
dfs(node.right, depth + 1)
```

### Visual Comparison

```
        1
       / \
      2   3
     / \   \
    4   5   6

Level 0: [1]       -> Right view: 1, Left view: 1
Level 1: [2, 3]    -> Right view: 3, Left view: 2
Level 2: [4, 5, 6] -> Right view: 6, Left view: 4

Right Side View: [1, 3, 6]
Left Side View:  [1, 2, 4]
```

## Related Problems

- [102. Binary Tree Level Order Traversal](../102.%20Binary%20Tree%20Level%20Order%20Traversal/) - Foundation pattern
- [513. Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/) - First node of last level
- [116. Populating Next Right Pointers](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) - Level order with linking
