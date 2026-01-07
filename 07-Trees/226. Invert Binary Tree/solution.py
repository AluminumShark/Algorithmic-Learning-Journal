# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# Solution 1: Recursive DFS
# ============================================================
# Time: O(n)
# Space: O(n) - recursion stack (O(h) for balanced tree)
class SolutionRecursive:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)
            node.left = right
            node.right = left
            return node

        return dfs(root)


# ============================================================
# Solution 2: Iterative DFS (Stack)
# ============================================================
# Time: O(n)
# Space: O(n)
class SolutionIterative:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            # Swap children
            node.left, node.right = node.right, node.left
            # Add children to stack (order doesn't matter for inversion)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root


# ============================================================
# Solution 3: BFS (Queue)
# ============================================================
# Time: O(n)
# Space: O(n)
class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            # Swap children
            node.left, node.right = node.right, node.left
            # Add children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# Default solution
Solution = SolutionRecursive

