# Time: O(m * n) (worst case)
# Space: O(m + n)
# Concept: Traverse 'root' (O(n)), and for each node, perform a Same Tree check (O(m)).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function (Same as isSameTree)
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)

        if not subRoot:
            return True
        if not root:
            return False

        if dfs(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
