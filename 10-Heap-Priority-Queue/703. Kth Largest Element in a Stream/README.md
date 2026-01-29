# 703. Kth Largest Element in a Stream

## Problem Description

Design a class to find the `kth` largest element in a stream. Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.

**Example:**
```
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4  (stream: [2,3,4,5,8], 3rd largest = 4)
kthLargest.add(5);   // return 5  (stream: [2,3,4,5,5,8], 3rd largest = 5)
kthLargest.add(10);  // return 5  (stream: [2,3,4,5,5,8,10], 3rd largest = 5)
kthLargest.add(9);   // return 8  (stream: [2,3,4,5,5,8,9,10], 3rd largest = 8)
kthLargest.add(4);   // return 8  (stream: [2,3,4,4,5,5,8,9,10], 3rd largest = 8)
```

## Solution: Min-Heap of Size K

```python
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(nums)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

**Complexity:**
- **Time:** O(N log K) for init, O(log K) for each add
- **Space:** O(K) - heap stores exactly K elements

## Key Concepts

### The "Min-Heap of Size K" Trick

**Key insight:** If we maintain a min-heap of exactly K elements, the **root (minimum)** is always the **Kth largest** overall.

```
Stream: [8, 5, 4, 2], k = 3

Sorted view: [2, 4, 5, 8]
              ^     ^  ^
              |     |  |
            small  3rd largest
                   (this is what we want)

Min-heap of size 3: [4, 5, 8]
                     ^
                    root = 4 = 3rd largest!
```

### Why Min-Heap, Not Max-Heap?

| Goal | Heap Type | Keep | Pop |
|------|-----------|------|-----|
| Kth Largest | Min-Heap | Top K largest | Smallest elements |
| Kth Smallest | Max-Heap | Top K smallest | Largest elements |

For Kth largest, we keep the **K largest** elements. A min-heap lets us:
1. Quickly identify the smallest of the K (the root)
2. Easily remove elements smaller than the Kth largest

### Visual: How the Heap Evolves

```
k = 3, nums = [4, 5, 8, 2]

After heapify: [2, 4, 5, 8] (heap property, not sorted)
After trimming to k=3: [4, 5, 8]
                        ^
                       root = 4 = 3rd largest

add(3):
  Push 3: [3, 4, 5, 8]
  Size > k, pop min: [4, 5, 8]
  Return root = 4

add(5):
  Push 5: [4, 5, 5, 8]
  Size > k, pop min: [5, 5, 8]
  Return root = 5

add(10):
  Push 10: [5, 5, 8, 10]
  Size > k, pop min: [5, 8, 10]
  Return root = 5
```

### Why Not Just Sort Every Time?

| Approach | add() Time | Space |
|----------|-----------|-------|
| Sort each time | O(N log N) | O(N) |
| Min-Heap of size K | O(log K) | O(K) |

The heap approach is much faster, especially for large streams with small K.

### Python heapq Basics

```python
import heapq

# Create heap from list (in-place, O(N))
heapq.heapify(nums)

# Push element (O(log N))
heapq.heappush(heap, val)

# Pop minimum (O(log N))
min_val = heapq.heappop(heap)

# Peek minimum (O(1))
min_val = heap[0]
```

**Important:** Python's `heapq` is a **Min-Heap** by default!

## Related Problems

- [215. Kth Largest Element in an Array](../215.%20Kth%20Largest%20Element%20in%20an%20Array/) - One-time query (can use QuickSelect)
- [973. K Closest Points to Origin](../973.%20K%20Closest%20Points%20to%20Origin/) - Similar K-element heap pattern
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Heap for frequency
