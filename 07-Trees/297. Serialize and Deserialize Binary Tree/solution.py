# Time: O(n)
# Space: O(h)
# Concept: Preorder DFS with '#' for nulls. Use a global iterator/index to reconstruct during deserialization.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        def dfs(node):
            if not node:
                arr.append('#')
                return
            
            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        return ','.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        self.i = 0  # Use class attribute or nonlocal in nested function

        def dfs():
            if self.i >= len(arr): return None
            
            val = arr[self.i]
            self.i += 1
            
            if val == '#':
                return None
            
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
