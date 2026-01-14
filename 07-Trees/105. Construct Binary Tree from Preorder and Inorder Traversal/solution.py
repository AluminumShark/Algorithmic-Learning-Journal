# Time: O(n) (conceptually, though slicing adds overhead)
# Space: O(n)
# Concept: Root is always preorder[0]. Find root index in inorder to calculate subtree sizes and split arrays recursively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        # Note: List slicing creates copies, conceptually O(N^2) behavior in worst case, but logic is O(N)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
