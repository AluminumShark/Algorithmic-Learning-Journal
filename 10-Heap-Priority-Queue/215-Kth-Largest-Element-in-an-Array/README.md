# 215. Kth Largest Element in an Array

## Problem Description

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Solution

### Approach: Min-Heap of Size K

The key insight is to maintain a min-heap of size `k`. As we iterate through the array:
- Add each element to the heap
- If the heap size exceeds `k`, remove the smallest element
- After processing all elements, the root of the heap is the kth largest element

**Why this works:**
- A min-heap of size `k` keeps the `k` largest elements seen so far
- The smallest of these `k` largest elements (at the root) is the kth largest overall

### Complexity Analysis

- **Time Complexity:** O(N log K)
  - We iterate through N elements
  - Each heap operation (push/pop) takes O(log K)
  - Total: O(N log K)

- **Space Complexity:** O(K)
  - The heap stores at most K elements

### Key Concepts

1. **Min-Heap for Kth Largest**: Use a min-heap (not max-heap) to find the kth largest element
2. **Heap Size Management**: Keep the heap size at exactly `k` by removing the smallest element when size exceeds `k`
3. **Efficient Selection**: This approach is more efficient than sorting (O(N log N)) when `k` is small compared to `N`

### Alternative Approaches

- **Sorting**: Sort the array and return `nums[-k]` → O(N log N) time, O(1) space
- **QuickSelect**: Average O(N), worst case O(N²) time, O(1) space
- **Max-Heap**: Build a max-heap and pop k-1 times → O(N + K log N) time, O(N) space
