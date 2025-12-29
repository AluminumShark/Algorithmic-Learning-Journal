# LeetCode 19: Remove Nth Node From End of List

## Overview

Remove the nth node from the end of a linked list in a single pass using the two-pointer technique with a fixed gap.

## Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
```

## Algorithm

**Two Pointers with a Gap**: Create a fixed gap of n nodes between slow and fast pointers to locate the target node in one pass.

**Key Steps:**
1. Create a dummy node before head to handle edge cases
2. Initialize both `S` (slow) and `F` (fast) at dummy
3. Move `F` pointer n steps ahead
4. Move both `S` and `F` simultaneously until `F.next` is None
5. Remove target node: `S.next = S.next.next`
6. Return `dummy.next` as the new head

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the list
- **Space Complexity:** O(1) - only uses constant extra space for pointers

## Key Concepts

### Two Pointers with Fixed Gap

By maintaining a gap of n nodes between fast and slow:

```python
# Move Fast pointer n steps ahead
for _ in range(n):
    F = F.next

# Now F is n steps ahead of S
# Move both until Fast reaches the end
while F.next:
    S = S.next
    F = F.next
```

When `F.next` is None, `S` is positioned right before the target node.

### Visual Walkthrough

```
List: 1 -> 2 -> 3 -> 4 -> 5, n = 2

Step 1 - Initialize at dummy:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
S, F

Step 2 - Move F ahead n (2) steps:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
S            F

Step 3 - Move both until F.next is None:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
              S            F

Step 4 - Remove S.next (node 4):
dummy -> 1 -> 2 -> 3 ------> 5

Result: 1 -> 2 -> 3 -> 5
```

### Dummy Node Pattern

The dummy node handles edge cases elegantly:
- If head needs to be removed (n = list length), dummy ensures there's always a node before it
- `dummy.next` always points to the correct new head

## Implementation Details

- Both pointers start at `dummy` (not head)
- Loop condition `while F.next` ensures `F` stops at the last node
- When `F.next` is None, `S.next` is the node to remove
- `S.next = S.next.next` performs the removal

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique with fixed gap
- Dummy node pattern for edge cases
- Single-pass optimization
- Linked list node removal

## Use Cases

- Removing nodes from specific positions
- Nth element from end operations
- Two-pointer patterns on linked lists
- Single-pass optimizations

## Related Problems

- Remove Duplicates from Sorted List
- Remove Linked List Elements
- Delete Node in a Linked List (LeetCode 237)
- Middle of the Linked List (LeetCode 876)

## Edge Cases

- Removing the head node (n equals list length)
- Single node list (n = 1)
- n equals list length (remove head)

All handled by dummy node pattern.

## Files

- `solution.py`: Two-pointer implementation with dummy node
