# LeetCode 21: Merge Two Sorted Lists

## Overview

Merge two sorted linked lists into one sorted linked list using the two-pointer technique with a dummy head node.

## Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a sorted order. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

## Algorithm

**Two-Pointer Merge with Dummy Head**: Use two pointers to traverse both lists simultaneously, comparing values and building the merged list.

**Key Steps:**
1. Create a dummy head node to simplify edge cases
2. Initialize a current pointer at the dummy node
3. While both lists are non-empty:
   - Compare values at current positions
   - Link the smaller node to the merged list
   - Advance the pointer of the list from which we took the node
   - Advance the merged list pointer
4. Append remaining nodes from the non-empty list
5. Return `dummy.next` as the head of merged list

## Complexity Analysis

- **Time Complexity:** O(n + m) - where n and m are lengths of the two lists, each node visited once
- **Space Complexity:** O(1) - only uses constant extra space for pointers (dummy node and current pointer)

## Key Insight

The merge process is similar to the merge step in merge sort:
- Compare elements from both lists
- Always choose the smaller element
- Link nodes directly (no new node creation needed)
- Handle remaining elements after one list is exhausted

## Implementation Details

### Dummy Head Pattern
- Eliminates special case handling for empty lists
- Simplifies pointer manipulation
- Provides a consistent starting point

### Node Linking
- Directly link existing nodes (no value copying)
- Efficient: O(1) per node operation
- Maintains original node structure

### Remaining Elements
- After one list is exhausted, simply link the rest
- No need to iterate through remaining nodes
- Single assignment: `cur.next = list1 if list1 else list2`

## Visual Example

```
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4

Step 1: Compare 1 and 1, take first 1
dummy -> 1
         cur

Step 2: Compare 2 and 1, take 1 from list2
dummy -> 1 -> 1
              cur

Step 3: Compare 2 and 3, take 2
dummy -> 1 -> 1 -> 2
                   cur

Step 4: Compare 4 and 3, take 3
dummy -> 1 -> 1 -> 2 -> 3
                        cur

Step 5: Compare 4 and 4, take first 4
dummy -> 1 -> 1 -> 2 -> 3 -> 4
                             cur

Step 6: list2 exhausted, link remaining from list1
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
                                  cur
```

## Alternative Approaches

1. **Recursive Approach**: O(n + m) time, O(n + m) space
   - More elegant but uses recursion stack
   - Less space-efficient

2. **In-Place Modification**: O(n + m) time, O(1) space
   - Modify one list to include nodes from the other
   - More complex pointer manipulation

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique on linked lists
- Dummy head pattern for simplification
- Merge operation (core of merge sort)
- Efficient node linking without copying

## Use Cases

- Merging sorted data structures
- Merge sort implementation
- Combining sorted sequences
- Foundation for merge k sorted lists

## Related Problems

- Merge k Sorted Lists
- Merge Two Sorted Arrays
- Sort List (uses merge operation)
- Merge In Between Linked Lists

## Edge Cases

- One or both lists are empty
- Lists of different lengths
- All elements in one list are smaller than the other
- Duplicate values (handled by `<=` comparison)

## Files

- `TwoPointers.py`: Two-pointer merge with dummy head implementation

