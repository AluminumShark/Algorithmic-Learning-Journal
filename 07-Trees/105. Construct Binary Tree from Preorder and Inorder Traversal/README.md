# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Problem Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

**Example:**
```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

Output:
    3
   / \
  9  20
    /  \
   15   7
```

## Solution: Recursive Construction

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)

    root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root
```

**Complexity:**
- **Time:** `O(n)` conceptually, but see note below about slicing
- **Space:** `O(n)` - recursion stack + sliced arrays

## Key Concepts

### The Core Insight: Preorder[0] is Always the Root

| Traversal | Order | First Element |
|-----------|-------|---------------|
| Preorder | **Root** → Left → Right | Always the root |
| Inorder | Left → **Root** → Right | Root in middle |

So `preorder[0]` tells us **what** the root is, and `inorder` tells us **where** to split left/right subtrees.

### How the Split Works

```
preorder = [3, 9, 20, 15, 7]
            ↑
           root

inorder  = [9, 3, 15, 20, 7]
            ↑  ↑  ↑--------↑
          left root  right

mid = inorder.index(3) = 1

Left subtree:  1 node  (index 0)
Right subtree: 3 nodes (indices 2-4)
```

### Array Splitting

```python
# For left subtree:
preorder[1 : mid + 1]  # Skip root, take 'mid' elements
inorder[: mid]         # Everything before root

# For right subtree:
preorder[mid + 1:]     # Remaining elements
inorder[mid + 1:]      # Everything after root
```

### Visual Walkthrough

```
Step 1: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
        root=3, mid=1
        left:  preorder=[9], inorder=[9]
        right: preorder=[20,15,7], inorder=[15,20,7]

Step 2 (left): preorder=[9], inorder=[9]
               root=9, mid=0
               left:  [], [] → None
               right: [], [] → None

Step 3 (right): preorder=[20,15,7], inorder=[15,20,7]
                root=20, mid=1
                left:  preorder=[15], inorder=[15]
                right: preorder=[7], inorder=[7]

... continues until all nodes built
```

---

## ⚠️ Important: Slicing Complexity Discussion

### The Slicing Overhead Problem

The solution above uses Python list slicing:
```python
preorder[1 : mid + 1]  # Creates a NEW list copy!
```

**Each slice is O(k)** where k is the slice length. In the worst case (skewed tree), this leads to:
- Level 1: O(n) slice
- Level 2: O(n-1) slice
- ...
- Total: **O(n²)** time!

### Interview Discussion Point

This is an excellent topic to discuss in interviews:

| Aspect | Slicing Solution | Optimized Solution |
|--------|-----------------|-------------------|
| Code Clarity | ✅ Very clean | ❌ More complex |
| Time Complexity | O(n²) worst case | O(n) |
| Space for arrays | O(n²) total copies | O(1) extra |

### Optimized O(n) Solution with Indices

```python
def buildTree(self, preorder, inorder):
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    self.pre_idx = 0
    
    def build(in_left, in_right):
        if in_left > in_right:
            return None
        
        root_val = preorder[self.pre_idx]
        self.pre_idx += 1
        
        root = TreeNode(root_val)
        mid = inorder_map[root_val]
        
        root.left = build(in_left, mid - 1)
        root.right = build(mid + 1, in_right)
        
        return root
    
    return build(0, len(inorder) - 1)
```

**Key optimizations:**
1. **HashMap** for O(1) index lookup (vs O(n) `list.index()`)
2. **Pass indices** instead of slicing arrays
3. **Global preorder index** to track position

---

## Related Problems

- [106. Construct Binary Tree from Inorder and Postorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) - Similar but postorder[-1] is root
- [889. Construct Binary Tree from Preorder and Postorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)
- [297. Serialize and Deserialize Binary Tree](../297.%20Serialize%20and%20Deserialize%20Binary%20Tree/) - Another tree construction problem
