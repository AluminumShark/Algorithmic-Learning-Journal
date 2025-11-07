# LeetCode 148: Sort List

## Overview

Sort a linked list in O(n log n) time and O(1) extra space using various sorting algorithms adapted for linked list data structure.

## Problem Description

Given the head of a linked list, return the list after sorting it in ascending order.

**Example:**
```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

## Algorithm Implementations

This problem demonstrates multiple sorting approaches adapted for linked lists:

### Merge Sort (Recommended)
**Time Complexity:** O(n log n)  
**Space Complexity:** O(log n) - recursion stack

**Key Steps:**
1. Find middle node using slow/fast pointers
2. Split list into two halves
3. Recursively sort both halves
4. Merge two sorted lists

**Advantages:**
- Optimal time complexity for linked lists
- Stable sorting
- Well-suited for linked lists (no random access needed)

### Quick Sort
**Time Complexity:** O(n log n) average, O(n²) worst case  
**Space Complexity:** O(log n) - recursion stack

**Key Steps:**
1. Partition list around pivot
2. Recursively sort left and right partitions
3. Swap values (not nodes) during partition

**Note:** May cause TLE on worst-case inputs

### Radix Sort
**Time Complexity:** O(d × n) where d is number of digits  
**Space Complexity:** O(n) - for buckets

**Key Steps:**
1. Find maximum value to determine digit passes
2. For each digit position, distribute nodes into buckets
3. Rebuild linked list from buckets

**Limitation:** Only works for non-negative integers

### Other Implementations
- **Bubble Sort**: O(n²) - educational purposes only
- **Selection Sort**: O(n²) - educational purposes only
- **Insertion Sort**: O(n²) - educational purposes only
- **Counting Sort**: O(n + k) - for bounded integer ranges

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Status on LC 148 |
|-----------|----------------|------------------|------------------|
| Merge Sort | O(n log n) | O(log n) | Accepted |
| Quick Sort | O(n log n) avg | O(log n) | May TLE |
| Radix Sort | O(d × n) | O(n) | Accepted* |
| Counting Sort | O(n + k) | O(k) | Accepted* |
| Bubble/Selection/Insertion | O(n²) | O(1) | TLE |

*Only for non-negative integers or bounded ranges

## Why Merge Sort for Linked Lists?

Unlike arrays, linked lists:
- Have O(1) insertion at any position
- Don't support random access
- Merge operation is efficient (just pointer manipulation)
- No need for extra space for merging (unlike array merge sort)

## Implementation Details

### Merge Sort Highlights
- **Finding Middle:** Slow/fast pointer technique
- **Splitting:** Set `slow.next = None` to break list
- **Merging:** Dummy head pattern simplifies pointer manipulation
- **Recursion:** Natural divide-and-conquer structure

### Quick Sort Highlights
- **Partition:** Swap values instead of nodes
- **Pivot Selection:** Uses first element as pivot
- **Range:** Uses `[left, right)` half-open interval

### Radix Sort Highlights
- **Bucket Distribution:** Collect values by digit
- **List Rebuilding:** Reconstruct linked list from buckets
- **Digit Processing:** Least significant to most significant

## Pattern Recognition

This problem demonstrates:
- Adapting array sorting algorithms to linked lists
- Pointer manipulation in sorting
- Divide-and-conquer on linked structures
- Trade-offs between different sorting approaches

## Use Cases

- Sorting linked data structures
- Understanding algorithm adaptation
- Performance comparison of sorting methods
- Linked list manipulation techniques

## Recommended Approach

**Merge Sort** is the recommended solution because:
1. Guaranteed O(n log n) time complexity
2. Stable sorting algorithm
3. Well-suited for linked list structure
4. Acceptable on LeetCode 148

## Files

- `MergeSort.py`: Recommended O(n log n) solution
- `QuickSort.py`: Partition-based sorting (may TLE)
- `RadixSort.py`: Digit-based sorting for integers
- `CountingSort.py`: Frequency-based sorting for bounded ranges
- `BubbleSort.py`, `SelectionSort.py`, `InsertionSort.py`: Educational implementations

