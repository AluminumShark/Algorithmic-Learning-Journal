# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# Solution 1: Recursive
# ============================================================
# Time: O(n)
# Space: O(n) due to recursion stack (O(h) for balanced tree)
class SolutionRecursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)  # Visit root first
            dfs(node.left)        # Then left subtree
            dfs(node.right)       # Then right subtree

        dfs(root)
        return res


# ============================================================
# Solution 2: Iterative (Stack)
# ============================================================
# Time: O(n)
# Space: O(n)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while root or stack:
            while root:
                res.append(root.val)      # Visit node immediately
                stack.append(root.right)  # Save right child for later
                root = root.left          # Go left
            root = stack.pop()            # Process saved right children

        return res

