# Time: O(n)
# Space: O(n)
# Concept: BFS. Capture the last node (i == len(q) - 1) of every level.

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        q = deque([root])
        ans = []
        while q:
            end = len(q)
            for i in range(end):
                node = q.popleft()
                if i == end - 1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
