# LeetCode 206: Reverse Linked List

## Overview

Reverse a singly linked list using iterative pointer manipulation.

## Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

**Example:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
```

## Algorithm

**Iterative Pointer Manipulation**: Traverse the list once, reversing each pointer as we go.

**Key Steps:**
1. Initialize `prev = None` and `curr = head`
2. While `curr` is not None:
   - Save next node: `temp = curr.next`
   - Reverse the arrow: `curr.next = prev`
   - Move forward: `prev = curr`, `curr = temp`
3. Return `prev` (new head of reversed list)

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the list
- **Space Complexity:** O(1) - only uses constant extra space for pointers

## Key Concepts

### Iterative Pointer Manipulation

The core technique involves three pointers working together:

```
Before:  prev -> curr -> temp -> ...
After:   prev <- curr    temp -> ...
                  v
         new prev  new curr
```

**Three Steps per Iteration:**
1. **Save**: Store `curr.next` before we lose it
2. **Reverse**: Point `curr.next` back to `prev`
3. **Move**: Shift both pointers forward

### Visual Walkthrough

```
Initial: None   1 -> 2 -> 3 -> 4 -> 5 -> None
         prev  curr

Step 1:  None <- 1    2 -> 3 -> 4 -> 5 -> None
               prev  curr

Step 2:  None <- 1 <- 2    3 -> 4 -> 5 -> None
                     prev curr

Step 3:  None <- 1 <- 2 <- 3    4 -> 5 -> None
                          prev curr

Step 4:  None <- 1 <- 2 <- 3 <- 4    5 -> None
                               prev curr

Step 5:  None <- 1 <- 2 <- 3 <- 4 <- 5    None
                                    prev  curr

Return prev (node 5) as new head
```

## Implementation Details

- `prev` starts as `None` (will become new tail's next pointer)
- `curr` starts at `head`
- `temp` temporarily stores `curr.next` before we overwrite it
- When `curr` becomes `None`, `prev` points to the last node (new head)

## Alternative Approaches

### Recursive Approach
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head
```
- **Time:** O(n)
- **Space:** O(n) due to recursion stack

## Pattern Recognition

This problem demonstrates:
- In-place linked list manipulation
- Pointer reversal technique
- Iterative vs recursive trade-offs
- Foundation for many linked list problems

## Use Cases

- Reversing linked data structures
- Palindrome checking in linked lists
- Rotating linked lists
- Foundation for reverse in groups

## Related Problems

- Reverse Linked List II (LeetCode 92) - reverse portion
- Palindrome Linked List (LeetCode 234)
- Reverse Nodes in k-Group (LeetCode 25)
- Swap Nodes in Pairs (LeetCode 24)

## Edge Cases

- Empty list (`head = None`)
- Single node list
- Two node list

## Files

- `solution.py`: Iterative pointer manipulation solution

