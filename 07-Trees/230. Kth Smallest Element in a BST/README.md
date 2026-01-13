# 230. Kth Smallest Element in a BST

## Problem Description

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (**1-indexed**) of all the values of the nodes in the tree.

**Example 1:**
```
    3
   / \
  1   4
   \
    2

k = 1, Output: 1
```

**Example 2:**
```
        5
       / \
      3   6
     / \
    2   4
   /
  1

k = 3, Output: 3
```

## Key Insight: In-order Traversal = Sorted Order

**In-order traversal of a BST always produces values in ascending sorted order!**

```
In-order: Left → Node → Right

        5
       / \
      3   6        In-order: [1, 2, 3, 4, 5, 6]
     / \           The kth smallest = the kth element in this sequence
    2   4
   /
  1
```

So finding the kth smallest is just: **perform in-order traversal, stop at the kth node**.

---

## Solution 1: Recursive In-order

```python
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.k = k
    self.ans = None
    
    def dfs(node):
        if not node or self.ans:
            return
        dfs(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
        dfs(node.right)
    
    dfs(root)
    return self.ans
```

**Complexity:**
- **Time:** `O(n)` worst case, but can exit early
- **Space:** `O(h)` - recursion stack

### Why `self.k` and `self.ans`?

We use instance variables because:
1. `k` needs to persist across recursive calls (count down)
2. `ans` signals when to stop (early termination)

---

## Solution 2: Iterative In-order (Stack)

```python
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    cur = root

    while cur or stack:
        # Go all the way left
        while cur:
            stack.append(cur)
            cur = cur.left
        
        # Process node (in-order position)
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        
        # Move to right subtree
        cur = cur.right
```

**Complexity:**
- **Time:** `O(n)` worst case
- **Space:** `O(h)` - explicit stack

---

## Comparison of Solutions

| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| Clarity | More intuitive | More explicit control |
| Early Exit | Via `self.ans` check | Direct `return` |
| Stack | Implicit (call stack) | Explicit |
| Space | O(h) | O(h) |

---

## Key Concepts

### In-order Traversal Pattern (Iterative)

The iterative in-order traversal has a specific pattern:

```python
while cur or stack:
    # Phase 1: Go left as far as possible
    while cur:
        stack.append(cur)
        cur = cur.left
    
    # Phase 2: Process current (pop from stack)
    cur = stack.pop()
    # >>> DO SOMETHING WITH cur.val HERE <<<
    
    # Phase 3: Move to right subtree
    cur = cur.right
```

This is the **standard template** for iterative in-order traversal.

### Visual Walkthrough

```
        5        k = 3
       / \
      3   6      Stack-based in-order:
     / \
    2   4        1. Push 5, 3, 2 → pop 2, k=2
   /             2. Pop 3, k=1
  1              3. Push 4 → pop 4, k=0 → return 4? NO!
                 
Wait, let me trace correctly:
1. Push 5,3,2,1 → pop 1, k=2
2. Pop 2, k=1  
3. Pop 3, k=0 → return 3 ✓

kth smallest = 3
```

### Why O(h) Space, Not O(n)?

The stack/recursion only holds nodes along a single path from root to current position. The maximum path length is the tree height h:
- Balanced tree: h = O(log n)
- Skewed tree: h = O(n)

---

## Follow-up: Frequent Queries?

If `kthSmallest` is called frequently, we can optimize by:
1. **Augmented BST**: Store subtree sizes in each node
2. **Cache**: Store in-order array (O(n) space, O(1) query)

```python
# Augmented approach: O(h) per query
# Each node stores: count of nodes in left subtree
def kthSmallest(node, k):
    left_count = node.left.count if node.left else 0
    if k == left_count + 1:
        return node.val
    elif k <= left_count:
        return kthSmallest(node.left, k)
    else:
        return kthSmallest(node.right, k - left_count - 1)
```

## Related Problems

- [98. Validate Binary Search Tree](../98.%20Validate%20Binary%20Search%20Tree/) - In-order gives sorted order
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) - The traversal pattern
- [173. Binary Search Tree Iterator](../173.%20Binary%20Search%20Tree%20Iterator/) - Iterative in-order with state
