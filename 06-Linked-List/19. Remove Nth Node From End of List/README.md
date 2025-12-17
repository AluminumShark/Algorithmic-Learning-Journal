# LeetCode 19: Remove Nth Node From End of List

## Overview

Remove the nth node from the end of a linked list in a single pass using the two-pointer technique.

## Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

## Algorithm

**Two-Pointer Technique (Fast & Slow)**: Use two pointers with a fixed gap to locate the target node in one pass.

**Key Steps:**
1. Create a dummy node before head to handle edge cases (e.g., removing head)
2. Initialize `slow` at dummy and `fast` at head
3. Move `fast` pointer n steps ahead
4. Move both `slow` and `fast` simultaneously until `fast` reaches the end
5. When `fast` is None, `slow` is positioned right before the target node
6. Remove target node: `slow.next = slow.next.next`
7. Return `dummy.next` as the new head

## Complexity Analysis

- **Time Complexity:** O(L) - single pass through the list, where L is the length
- **Space Complexity:** O(1) - only uses constant extra space for pointers

## Key Insight

By maintaining a gap of n nodes between `fast` and `slow`:
- When `fast` reaches the end (None), `slow` is exactly n nodes from the end
- `slow.next` is the node to be removed
- Dummy node eliminates special case handling for head removal

## Visual Example

```
Initial: dummy -> 1 -> 2 -> 3 -> 4 -> 5, n = 2
         slow    fast

After moving fast n steps:
         dummy -> 1 -> 2 -> 3 -> 4 -> 5
         slow              fast

After moving both to end:
         dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                          slow              fast

Remove slow.next (node 4):
         dummy -> 1 -> 2 -> 3 -> 5
```

## Alternative Approaches

1. **Two-Pass Approach**: O(L) time, O(1) space
   - First pass: count list length
   - Second pass: remove (length - n)th node
   - Less elegant but straightforward

2. **Stack-Based**: O(L) time, O(L) space
   - Push all nodes onto stack
   - Pop n nodes, remove the next one
   - More space overhead

## Implementation Details

- **Dummy Node Pattern**: Simplifies edge case handling
  - If head needs to be removed, dummy ensures there's always a node before it
  - Eliminates need for special head removal logic

- **Fixed Gap Technique**: 
  - Gap of n nodes maintained throughout traversal
  - When fast reaches end, slow is at correct position

- **One-Pass Efficiency**: 
  - More efficient than two-pass approach
  - Better cache locality

## Edge Cases

- Removing the head node (n equals list length)
- Single node list (n = 1)
- Empty list
- n equals list length (remove head)

All handled by dummy node pattern.

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique with fixed gap
- Dummy node pattern for edge cases
- Single-pass optimization
- Linked list node removal

## Use Cases

- Removing nodes from specific positions
- Nth element operations
- Two-pointer patterns on linked lists
- Single-pass optimizations

## Related Problems

- Remove Duplicates from Sorted List
- Remove Linked List Elements
- Delete Node in a Linked List
- Middle of the Linked List

## Files

- `TwoPointers.py`: Two-pointer implementation with dummy node

