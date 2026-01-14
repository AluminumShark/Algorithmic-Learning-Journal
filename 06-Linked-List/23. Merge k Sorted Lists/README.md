# 23. Merge k Sorted Lists

## Problem Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Constraints:**
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`

## Solution: Min-Heap (Priority Queue)

Use a min-heap to always get the smallest element among all list heads.

### Algorithm

1. **Initialize**: Push the head of each non-empty list into the heap
2. **Process**: Repeatedly pop the smallest, add it to result, push its next node
3. **Terminate**: When heap is empty, all nodes have been processed

### The Tie-Breaking Problem

Python's `heapq` compares tuples element by element. If two nodes have equal values, it tries to compare the nodes themselves:

```python
# This will FAIL when values are equal!
heapq.heappush(heap, (node.val, node))

# TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
```

### Solution: Add Index as Tie-Breaker

```python
# Store (value, list_index, node)
heapq.heappush(heap, (node.val, i, node))
```

Now the comparison sequence is:
1. Compare `val` -> if different, we're done
2. Compare `i` (index) -> always different, so we never compare nodes!

| Tuple A | Tuple B | Comparison |
|---------|---------|------------|
| `(5, 0, nodeA)` | `(5, 1, nodeB)` | `5 == 5` -> compare `0 < 1` |
| `(3, 2, nodeC)` | `(5, 0, nodeA)` | `3 < 5` |

### Complexity Analysis

- **Time:** `O(n log k)`
  - Each of `n` nodes is pushed and popped once
  - Each heap operation is `O(log k)`
- **Space:** `O(k)` for the heap (at most `k` nodes at any time)

### Why This is Better Than Merge One-by-One

| Approach | Time Complexity |
|----------|-----------------|
| Merge pairs one-by-one | `O(kn)` |
| **Min-Heap** | `O(n log k)` |
| Divide and Conquer | `O(n log k)` |

For large `k`, the heap approach is significantly faster.

## Key Concepts

1. **Min-Heap for k-way Merge**: Classic technique for merging multiple sorted sequences
2. **Tuple Tie-Breaking**: Use a unique index to avoid comparing non-comparable objects
3. **Dummy Node**: Simplifies edge cases for linked list construction

## Alternative Approaches

### Divide and Conquer
Recursively merge pairs of lists, similar to merge sort. Also achieves `O(n log k)`.

### Merge One-by-One
Merge list 1 with list 2, then result with list 3, etc. Simple but slower: `O(kn)`.

## Related Problems

- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

