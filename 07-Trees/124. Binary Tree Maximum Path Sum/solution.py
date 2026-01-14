# Time: O(n)
# Space: O(h)
# Concept: Post-order DFS. Calculate max contribution of left/right children (clamping to 0 if negative). Update global max with "arch" path (Left + Root + Right), but return only "straight" path (Root + max(Left, Right)) to parent.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # Max gain from subtrees, ignore if negative
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Update global maximum (Path can curve through root)
            self.ans = max(self.ans, left + right + node.val)

            # Return max path extending to parent (Must choose one side)
            return node.val + max(left, right)
        
        dfs(root)

        return self.ans
