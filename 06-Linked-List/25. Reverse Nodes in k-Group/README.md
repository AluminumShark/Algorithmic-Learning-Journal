# 25. Reverse Nodes in k-Group

## Problem Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Solution: Iterative Group Reversal

### Visual Walkthrough

For `[1,2,3,4,5]` with `k = 2`:

```
Initial:   dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
                   ^       ^
              groupStart  groupNext
           
After 1st: dummy -> 2 -> 1 -> 3 -> 4 -> 5 -> null
                        ^   ^       ^
                   groupPrev groupStart groupNext
                   
After 2nd: dummy -> 2 -> 1 -> 4 -> 3 -> 5 -> null
                             ^   ^
                        groupPrev  (5 is < k, stop)
```

### Algorithm

```
For each group:
1. Find kth node (return if < k nodes remain)
2. Reverse the group in-place
3. Reconnect: previous -> reversed group -> next group
4. Advance groupPrev to end of reversed group
```

### Key Pointers

| Pointer | Purpose |
|---------|---------|
| `dummy` | Anchor before head (handles edge case of reversing first group) |
| `groupPrev` | Node immediately before current group |
| `groupStart` | First node of current group (becomes last after reversal) |
| `kth` | Last node of current group (becomes first after reversal) |
| `groupNext` | First node of next group |

### The Reversal Step

Standard linked list reversal, but with a twist:
- Initialize `prev = groupNext` (not `null`)
- This automatically connects the reversed group to the next part

```python
prev = groupNext  # Key: reversed tail points to next group
cur = groupStart
while cur != groupNext:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

### Complexity Analysis

- **Time:** `O(n)` - each node is visited at most twice
  - Once when finding kth node
  - Once during reversal
- **Space:** `O(1)` - only pointer manipulation

## Key Concepts

1. **Dummy Node**: Simplifies handling of the head node
2. **Group Boundaries**: Clearly define start, end, prev, next for each group
3. **In-Place Reversal**: Modified standard reversal that connects to next group
4. **Early Termination**: Return immediately when fewer than k nodes remain

## Common Pitfalls

1. **Forgetting to check k nodes exist**: Must verify before reversing
2. **Losing connections**: Save `groupNext` before modifying pointers
3. **Infinite loop**: Ensure `groupPrev` advances after each reversal

## Step-by-Step Trace

For `[1,2,3,4,5]`, `k = 3`:

| Step | Action | List State |
|------|--------|------------|
| Init | Setup dummy | `dummy->1->2->3->4->5` |
| Find k=3 | kth=3 | groupPrev=dummy, groupStart=1, kth=3, groupNext=4 |
| Reverse | 1->2->3 becomes 3->2->1 | `dummy->3->2->1->4->5` |
| Connect | groupPrev->kth, groupPrev=1 | `dummy->3->2->1->4->5` |
| Find k=3 | Only 2 nodes left | **Return** |

**Result:** `[3,2,1,4,5]`

## Related Problems

- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (k=2 special case)
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

