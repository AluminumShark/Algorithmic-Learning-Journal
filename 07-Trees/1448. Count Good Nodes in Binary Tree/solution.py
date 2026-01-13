# Time: O(n)
# Space: O(h) (Height of tree)
# Concept: Pre-order DFS. Pass the 'current max' value down the path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cmx):
            if not node:
                return 0
            
            if node.val >= cmx:
                good = 1
            else:
                good = 0

            cmx = max(cmx, node.val)
            
            good += dfs(node.left, cmx)
            good += dfs(node.right, cmx)

            return good

        return dfs(root, root.val)
