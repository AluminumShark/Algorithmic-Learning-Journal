# 145. Binary Tree Postorder Traversal

## Problem Description

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

**Postorder traversal** visits nodes in the following order:
1. **Left** subtree
2. **Right** subtree
3. **Root** (current node)

## Solutions

### Solution 1: Recursive

The recursive approach directly follows the definition of postorder traversal.

```python
def dfs(node):
    if not node: return
    dfs(node.left)        # Left subtree first
    dfs(node.right)       # Then right subtree
    res.append(node.val)  # Visit root last
```

**Complexity Analysis:**
- **Time:** `O(n)` - visit each node exactly once
- **Space:** `O(n)` - recursion stack depth (worst case for skewed tree)

### Solution 2: Iterative (Visit Flag / Tagging Method) ⭐

This is a **universal technique** that works for all three traversals (preorder, inorder, postorder) with minimal modification.

#### The Visit Flag Technique

The key insight is to use a **boolean flag** to track whether a node's children have been processed:

| Flag State | Meaning | Action |
|------------|---------|--------|
| `visited = False` | First encounter | Push node back (with `True`), then push children |
| `visited = True` | Second encounter | Process the node (add to result) |

#### How It Simulates Recursion

```
Push Order: root(True) → right(False) → left(False)
Pop Order:  left → right → root  ← This is postorder!
```

By pushing in reverse order and using the flag, we ensure:
1. Left subtree is fully processed first
2. Right subtree is processed second
3. Root is processed last (when we see it the second time)

#### Code Pattern

```python
stack = [root]
visit = [False]

while stack:
    cur, visited = stack.pop(), visit.pop()
    if cur:
        if visited:
            res.append(cur.val)  # Process on second visit
        else:
            # Schedule: root(True), right(False), left(False)
            stack.append(cur);       visit.append(True)
            stack.append(cur.right); visit.append(False)
            stack.append(cur.left);  visit.append(False)
```

**Complexity Analysis:**
- **Time:** `O(n)` - each node is pushed and popped twice
- **Space:** `O(n)` - stack space

## Key Concepts

### Why Postorder Iterative is Tricky

Unlike preorder (process immediately) and inorder (process after left), postorder requires processing a node **after both children**. This makes it harder to implement iteratively without some tracking mechanism.

### The Visit Flag Advantage

1. **Universal**: Same pattern works for all traversals (just change push order)
2. **Intuitive**: Directly simulates the call stack behavior
3. **No Reversal Tricks**: Some solutions use "modified preorder + reverse", but the flag method is more natural

### Comparison: Traversal Push Orders

| Traversal | Push Order (with flags) | Result Order |
|-----------|------------------------|--------------|
| Preorder | root(True), right(False), left(False) → process on True | Root → Left → Right |
| Inorder | right(False), root(True), left(False) → process on True | Left → Root → Right |
| Postorder | root(True), right(False), left(False) → process on True | Left → Right → Root |

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
- [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

