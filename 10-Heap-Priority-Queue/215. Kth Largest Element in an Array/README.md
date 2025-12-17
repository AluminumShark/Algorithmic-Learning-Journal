# LeetCode 215: Kth Largest Element in an Array

## Overview

Find the kth largest element in an unsorted array.

## Problem Description

Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

## Algorithm

**Max Heap Approach**: Build a max heap and extract the maximum element k times.

**Key Steps:**
1. Build a max heap from all elements in the array
2. Extract the maximum element (root) k times
3. The kth extracted element is the kth largest

## Complexity Analysis

- **Time Complexity:** O(n log n) - building heap takes O(n log n) with repeated insertions, extracting k elements takes O(k log n)
- **Space Complexity:** O(n) - for the heap storage

## Alternative Approaches

1. **Quick Select**: O(n) average case, O(n²) worst case
   - Partition-based selection algorithm
   - More efficient for large arrays when k is small

2. **Min Heap of Size k**: O(n log k)
   - Maintain a min heap of size k
   - More space-efficient when k << n

3. **Sorting**: O(n log n)
   - Simple but not optimal

## Implementation Details

- Custom MaxHeap class with push/pop operations
- Heapify operations to maintain heap property
- Straightforward approach: build heap then extract

## Pattern Recognition

This problem demonstrates:
- Heap data structure applications
- Selection algorithms
- Priority queue concepts

## Use Cases

- Finding top-k elements
- Priority queue problems
- Selection algorithms
- Order statistics

## Optimization Note

For better performance, consider:
- Using min heap of size k (O(n log k))
- Quick select algorithm (O(n) average case)
- Python's `heapq.nlargest()` for practical applications

## Files

- `MaxHeap.py`: Max heap implementation with kth largest extraction

