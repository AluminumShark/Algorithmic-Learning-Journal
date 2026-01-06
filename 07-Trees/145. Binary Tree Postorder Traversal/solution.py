# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

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
# Space: O(n) due to recursion stack
class SolutionRecursive:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)        # Left subtree first
            dfs(node.right)       # Then right subtree
            res.append(node.val)  # Visit root last

        dfs(root)
        return res


# ============================================================
# Solution 2: Iterative (Visit Flag / Tagging Method)
# ============================================================
# Time: O(n)
# Space: O(n)
#
# Key Technique: Visit Flag (Tagging)
# -----------------------------------
# This technique uses a boolean flag to track whether a node has been
# "visited" (i.e., its children have been processed).
#
# - First encounter (visited=False): Push the node back with visited=True,
#   then push right and left children (in that order, so left is processed first)
# - Second encounter (visited=True): Add node's value to result
#
# This elegantly simulates the call stack behavior of recursion,
# ensuring we process: Left → Right → Root (postorder)
#
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visit = [False]

        while stack:
            cur, visited = stack.pop(), visit.pop()

            if cur:
                if visited:
                    # Second visit: now we can add to result
                    res.append(cur.val)
                else:
                    # First visit: schedule for later, process children first
                    # Push order: root(True) → right(False) → left(False)
                    # Pop order: left → right → root (postorder!)
                    stack.append(cur)
                    visit.append(True)

                    stack.append(cur.right)
                    visit.append(False)

                    stack.append(cur.left)
                    visit.append(False)

        return res

