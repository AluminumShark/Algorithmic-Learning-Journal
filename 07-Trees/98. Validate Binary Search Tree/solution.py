# Time: O(n)
# Space: O(h)
# Concept: DFS with Range. Maintain (low, high) boundaries. Left child must be < current, Right child must be > current.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))
