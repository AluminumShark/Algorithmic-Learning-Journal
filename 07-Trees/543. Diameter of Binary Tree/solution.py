# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# Solution: Post-order DFS with Global State
# ============================================================
# Time: O(n)
# Space: O(n) - recursion stack
#
# Key Insight:
# ------------
# The DFS function returns HEIGHT (for parent to use),
# but updates DIAMETER as a side effect (global/nonlocal).
#
# Why?
# - Height is needed by parent: parent's height = max(left_h, right_h) + 1
# - Diameter through a node = left_height + right_height
# - The maximum diameter might be at ANY node, not just root
#
# This is a classic "return one thing, track another" pattern.
#
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            # Get heights of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # The longest path through THIS node is left_height + right_height
            # (number of edges = left_height + right_height)
            ans = max(ans, left + right)

            # Return the height of this subtree to parent
            # Height = max depth from this node = max(left, right) + 1
            return max(left, right) + 1

        dfs(root)
        return ans

