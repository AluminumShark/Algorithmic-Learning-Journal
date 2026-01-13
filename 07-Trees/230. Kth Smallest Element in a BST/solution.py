# Concept: BST In-order Traversal gives sorted values. Stop at the kth element.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive In-order
# Time: O(n)
# Space: O(h)
class SolutionRecursive:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None
        def dfs(node):
            if not node or self.ans:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
            dfs(node.right)
        dfs(root)
        return self.ans


# Solution 2: Iterative In-order (Stack)
# Time: O(n)
# Space: O(h)
class SolutionIterative:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        ans = 0

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
