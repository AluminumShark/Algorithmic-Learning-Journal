# 173. Binary Search Tree Iterator

## Problem Description

Implement the `BSTIterator` class that represents an iterator over the **in-order traversal** of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

**Follow up:** Could you implement `next()` and `hasNext()` to run in average `O(1)` time and use `O(h)` memory, where `h` is the height of the tree?

## Solutions

### Solution 1: Recursive Flattening

The simplest approach is to perform an in-order traversal during construction and store all values in an array.

**Complexity Analysis:**
- **Time:** `O(n)` for construction, `O(1)` for `next()` and `hasNext()`
- **Space:** `O(n)` to store all node values

### Solution 2: Iterative (Stack - Controlled Recursion)

This solution uses a stack to simulate the recursion, achieving `O(h)` space complexity. The key insight is that we only need to keep track of the "left spine" of the current subtree.

**Algorithm:**
1. In the constructor, push all left children onto the stack (the leftmost path)
2. For `next()`:
   - Pop the top node (this is the next smallest)
   - If it has a right child, push all left children of the right subtree onto the stack
3. `hasNext()` simply checks if the stack is non-empty

**Complexity Analysis:**
- **Time:** `O(1)` amortized for `next()` (each node is pushed and popped exactly once)
- **Space:** `O(h)` where `h` is the height of the tree

## Key Concepts

1. **In-order Traversal of BST**: Produces elements in sorted (ascending) order
2. **Controlled Recursion**: Using a stack to manually control the traversal state
3. **Amortized Analysis**: While a single `next()` call might do `O(h)` work, across `n` calls the total work is `O(n)`, giving `O(1)` amortized time

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

