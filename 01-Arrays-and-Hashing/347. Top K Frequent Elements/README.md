# LeetCode 347: Top K Frequent Elements

## Overview

Find the k most frequent elements in an array using various approaches from sorting to heap optimization.

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

## Algorithm

### Solution 1: Sorting

**Key Steps:**
1. Count frequency of each element
2. Sort elements by frequency in descending order
3. Return first k elements

### Solution 2: Counter

**Key Steps:**
1. Use Counter to count frequencies
2. Use `most_common(k)` to get top k elements

### Solution 3: Heap

**Key Steps:**
1. Count frequency of each element
2. Maintain a min-heap of size k
3. Pop smallest when heap exceeds k
4. Remaining k elements are the answer

## Complexity Analysis

### Solution 1: Sorting
- **Time Complexity:** O(n log n) - sorting dominates
- **Space Complexity:** O(n) - storing frequency map

### Solution 2: Counter
- **Time Complexity:** O(n log n) - most_common uses sorting internally
- **Space Complexity:** O(n) - Counter storage

### Solution 3: Heap
- **Time Complexity:** O(n log k) - each heap operation is O(log k)
- **Space Complexity:** O(n + k) - Counter + heap of size k

## Key Concepts

- **Frequency Counting**: Hash map for element counts
- **Heap/Priority Queue**: Efficient for top-k problems
- **Bucket Sort**: O(n) alternative (not shown)

## Implementation Details

### Sorting Approach
- Simple and intuitive
- Good for small datasets

### Counter Approach
- Most Pythonic solution
- Leverages built-in optimization

### Heap Approach
- Optimal for large n with small k
- Min-heap maintains k largest frequencies

## Pattern Recognition

This problem demonstrates:
- Top-K pattern using heaps
- Frequency counting with hash map
- Trade-offs between different approaches

## Alternative: Bucket Sort (O(n))

```python
def topKFrequent(self, nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
```

## Related Problems

- Kth Largest Element in an Array (LeetCode 215)
- Sort Characters By Frequency (LeetCode 451)
- Top K Frequent Words (LeetCode 692)

## Edge Cases

- All elements have same frequency
- k equals number of unique elements
- Single element array
- Array with all same elements

## Files

- `solution.py`: Sorting, Counter, and Heap implementations

