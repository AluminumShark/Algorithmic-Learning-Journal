# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# Solution 1: Recursive Flattening
# ============================================================
# Time: O(n) construction, O(1) next
# Space: O(n)
class BSTIteratorRecursive:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.itr = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)

    def next(self) -> int:
        val = self.arr[self.itr]
        self.itr += 1
        return val

    def hasNext(self) -> bool:
        return self.itr < len(self.arr)


# ============================================================
# Solution 2: Iterative (Stack - Controlled Recursion)
# ============================================================
# Time: O(1) amortized next()
# Space: O(h) where h is the height of the tree
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        val = cur.val
        cur = cur.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return val

    def hasNext(self) -> bool:
        return bool(self.stack)

