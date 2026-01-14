# 297. Serialize and Deserialize Binary Tree

## Problem Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Example:**
```
    1
   / \
  2   3
     / \
    4   5

Serialized: "1,2,#,#,3,4,#,#,5,#,#"
```

## Solution: Preorder DFS with Null Markers

### Serialize

```python
def serialize(self, root):
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
```

### Deserialize

```python
def deserialize(self, data):
    arr = data.split(',')
    self.i = 0

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
```

**Complexity:**
- **Time:** `O(n)` - visit each node once
- **Space:** `O(n)` - string storage + recursion stack O(h)

## Key Concepts

### Why Preorder DFS with Null Markers?

The combination of **preorder traversal** + **null markers (#)** allows **unique reconstruction**:

| Format | Can Reconstruct? | Why |
|--------|-----------------|-----|
| Preorder only | No | Can't determine structure |
| Preorder + Inorder | Yes | But needs two arrays |
| Preorder + Nulls | Yes | Nulls encode structure! |

### How Null Markers Encode Structure

```
    1
   / \
  2   3
     / \
    4   5

Preorder with nulls: 1, 2, #, #, 3, 4, #, #, 5, #, #
                     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^
                     1  2  2L 2R 3  4  4L 4R 5  5L 5R

Each # tells us "this child is null, go back up"
```

### The Deserialization Process

```
Input: "1,2,#,#,3,4,#,#,5,#,#"

i=0: val=1, create node(1)
  i=1: val=2, create node(2) as left child
    i=2: val=#, return None (left of 2)
    i=3: val=#, return None (right of 2)
  i=4: val=3, create node(3) as right child
    i=5: val=4, create node(4) as left child
      i=6: val=#, return None
      i=7: val=#, return None
    i=8: val=5, create node(5) as right child
      i=9: val=#, return None
      i=10: val=#, return None

Result: Original tree reconstructed!
```

### Why Global Index `self.i`?

```python
self.i = 0  # Shared across all recursive calls

def dfs():
    val = arr[self.i]
    self.i += 1  # Advance for ALL future calls
    ...
```

The index must be **shared** because each recursive call consumes the next value. Using a local variable wouldn't work - it would reset on each call.

### Alternative: Using Iterator

```python
def deserialize(self, data):
    def dfs(nodes):
        val = next(nodes)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = dfs(nodes)
        node.right = dfs(nodes)
        return node
    
    return dfs(iter(data.split(',')))
```

Using Python's `iter()` and `next()` is cleaner than tracking index manually.

### BFS Alternative

```python
def serialize(self, root):
    if not root: return ''
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        if node:
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            result.append('#')
    return ','.join(result)
```

BFS serialization is also valid but slightly more complex for deserialization.

### Edge Cases

| Input | Serialized |
|-------|-----------|
| Empty tree | `"#"` |
| Single node | `"1,#,#"` |
| Left-skewed | `"1,2,3,#,#,#,#"` |

## Related Problems

- [105. Construct Binary Tree from Preorder and Inorder](../105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/) - Tree construction
- [449. Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/) - BST version (no nulls needed)
- [428. Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) - N-ary extension
