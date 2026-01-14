# 235. Lowest Common Ancestor of a Binary Search Tree

## Problem Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

The lowest common ancestor is defined as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

**Example 1:**
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

p = 2, q = 8
Output: 6
```

**Example 2:**
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

p = 2, q = 4
Output: 2 (a node can be ancestor of itself)
```

## Solution: BST Split Point (Iterative)

```python
def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
        if cur.val < p.val and cur.val < q.val:
            cur = cur.right
        elif cur.val > p.val and cur.val > q.val:
            cur = cur.left
        else:
            return cur
```

**Complexity:**
- **Time:** `O(h)` where h is the height of the tree (O(log n) for balanced, O(n) worst case for skewed)
- **Space:** `O(1)` - no recursion, just a pointer!

## Key Concepts

### Why O(1) Space? Leveraging BST Properties!

This is **NOT** a generic binary tree LCA problem. Because we have a **BST**, we can use the **ordering property** to navigate without recursion:

| Condition | Meaning | Action |
|-----------|---------|--------|
| `cur.val < p.val AND cur.val < q.val` | Both p and q are in right subtree | Go right |
| `cur.val > p.val AND cur.val > q.val` | Both p and q are in left subtree | Go left |
| Otherwise | p and q are on different sides (or one equals cur) | **Found LCA!** |

### The "Split Point" Intuition

```
        6          <- p=2 is LEFT, q=8 is RIGHT -> SPLIT POINT!
       / \
      2   8
     / \ / \
    0  4 7  9

LCA(2, 8) = 6 because 6 is where the paths to 2 and 8 diverge.
```

The LCA is always the first node where p and q "split" into different subtrees.

### BST vs General Binary Tree LCA

| Aspect | BST (This Problem) | General Binary Tree |
|--------|-------------------|---------------------|
| Problem # | 235 | 236 |
| Can use values? | Yes - compare values | No - must search both subtrees |
| Space Complexity | O(1) iterative | O(n) recursive stack |
| Time Complexity | O(h) | O(n) |

### Recursive Version (For Reference)

```python
def lowestCommonAncestor(self, root, p, q):
    if root.val < p.val and root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return root
```

This is O(h) space due to recursion stack. The iterative version is preferred for O(1) space.

### Edge Cases

| Case | Example | Result |
|------|---------|--------|
| One node is ancestor of other | p=2, q=4 | Returns 2 |
| p and q are same node | p=2, q=2 | Returns 2 |
| p and q are leaves on opposite sides | p=0, q=9 | Returns 6 |

## Visual Walkthrough

```
Find LCA(3, 5):

        6     cur=6: 6 > 3 AND 6 > 5 -> go LEFT
       / \
      2   8
     / \ 
    0  4      cur=2: 2 < 3 AND 2 < 5 -> go RIGHT
      / \
     3   5    cur=4: 4 > 3 BUT 4 < 5 -> SPLIT! Return 4

LCA(3, 5) = 4
```

## Related Problems

- [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) - General tree version (harder)
- [102. Binary Tree Level Order Traversal](../102.%20Binary%20Tree%20Level%20Order%20Traversal/) - BFS on trees
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) - Uses same BST navigation
