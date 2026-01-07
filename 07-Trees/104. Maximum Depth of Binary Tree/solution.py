# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# Solution 1: BFS (Level Order Traversal)
# ============================================================
# Time: O(n)
# Space: O(n) - up to n/2 nodes at widest level
class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            # Process all nodes at current level
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level


# ============================================================
# Solution 2: Recursive DFS
# ============================================================
# Time: O(n)
# Space: O(n) - recursion stack
class SolutionRecursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            return max(left, right)

        return dfs(root)


# ============================================================
# Solution 3: Iterative DFS (Stack with Depth Tracking)
# ============================================================
# Time: O(n)
# Space: O(n)
class SolutionIterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]  # [node, current_depth]
        ans = 0

        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)

            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])

        return ans


# Default solution
Solution = SolutionRecursive

