# LeetCode 143: Reorder List

## Overview

Reorder a linked list in-place by interleaving nodes from the beginning and end, using three key techniques: find middle, reverse, and merge.

## Problem Description

You are given the head of a singly linked-list. The list can be represented as:

`L0 → L1 → … → Ln - 1 → Ln`

Reorder the list to be in the following form:

`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example:**
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Algorithm

**Three-Step Approach**: Find middle, reverse second half, merge alternately.

**Key Steps:**
1. **Find Middle**: Use slow/fast pointers to find the middle node
2. **Reverse Second Half**: Reverse the list starting from the middle
3. **Merge Two Halves**: Interleave nodes from first half and reversed second half

## Complexity Analysis

- **Time Complexity:** O(n) - three passes through the list
- **Space Complexity:** O(1) - only uses constant extra space for pointers

## Key Concepts

### Step 1: Find Middle (Slow/Fast Pointers)

```python
S, F = head, head
while F and F.next:
    S = S.next
    F = F.next.next
```

When fast pointer reaches end, slow pointer is at middle:
```
1 -> 2 -> 3 -> 4 -> 5
          S         F (F.next = None, stop)
```

### Step 2: Reverse Second Half

```python
prev, cur = None, S
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

After reversal:
```
First half:  1 -> 2 -> 3
Second half: 5 -> 4 -> 3 (prev points to 5)
```

### Step 3: Merge Two Halves

```python
list1, list2 = head, prev
while list2.next:
    tmp1 = list1.next
    tmp2 = list2.next
    list1.next = list2
    list2.next = tmp1
    list1 = tmp1
    list2 = tmp2
```

Interleaving process:
```
Step 1: 1 -> 5 -> 2 -> 3    (list1=2, list2=4)
Step 2: 1 -> 5 -> 2 -> 4 -> 3 (list2.next = None, stop)
```

### Visual Walkthrough

```
Original: 1 -> 2 -> 3 -> 4 -> 5

Step 1 - Find Middle:
         1 -> 2 -> 3 -> 4 -> 5
                   S         F

Step 2 - Reverse Second Half:
         First:  1 -> 2 -> 3
         Second: 5 -> 4 -> 3

Step 3 - Merge:
         1 -> 5 -> 2 -> 4 -> 3
```

## Implementation Details

- **In-place modification**: No new nodes created
- **Odd vs Even length**: Works for both cases
  - Odd: Middle node stays in place (shared by both halves)
  - Even: Clean split between halves
- **Loop termination**: `while list2.next` ensures we stop when all nodes are placed

## Pattern Recognition

This problem combines three fundamental linked list techniques:
1. **Slow/Fast pointers** - Finding middle
2. **Pointer reversal** - Reversing a list
3. **List merging** - Interleaving two lists

## Use Cases

- Linked list rearrangement
- In-place list manipulation
- Combining multiple techniques

## Related Problems

- Reverse Linked List (LeetCode 206)
- Middle of the Linked List (LeetCode 876)
- Palindrome Linked List (LeetCode 234)
- Merge Two Sorted Lists (LeetCode 21)

## Edge Cases

- Single node list
- Two node list
- Empty list

## Files

- `solution.py`: Three-step in-place solution

