# 973. K Closest Points to Origin

## Problem Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `sqrt(x^2 + y^2)`).

You may return the answer in **any order**. The answer is **guaranteed** to be unique (except for the order that it is in).

**Example:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Explanation:
Distance of (1,3) = sqrt(10)
Distance of (-2,2) = sqrt(8)
(-2,2) is closer to origin.
```

## Solution: Max-Heap with Negation

```python
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store (-distance, x, y) to simulate Max-Heap
        heap = [(-(x ** 2 + y ** 2), x, y) for x, y in points]
        heapq.heapify(heap)
        
        # Pop the "largest" distances until only k elements remain
        while len(heap) > k:
            heapq.heappop(heap)
            
        res = [[x, y] for _, x, y in heap]
        return res
```

**Complexity:**
- **Time:** O(N + (N-K) log N) - heapify O(N), then N-K pops
- **Space:** O(N) - heap stores all points initially

## Key Concepts

### Why Max-Heap for "Closest"?

**Goal:** Keep the K **smallest** distances.

**Strategy:** Use a max-heap so we can efficiently **remove the largest** distance when we have more than K elements.

```
Points with distances: [10, 2, 5, 8, 3], k = 2

Max-Heap (negated): [-10, -8, -5, -3, -2]

Pop until size = k:
  Pop -10 (distance 10, the farthest)
  Pop -8 (distance 8)
  Pop -5 (distance 5)
  
Remaining: [-3, -2] -> distances [3, 2] -> K closest!
```

### The Negation Pattern for K Smallest

| Goal | Heap Type | Reason |
|------|-----------|--------|
| K Largest | Min-Heap | Pop smallest, keep largest |
| K Smallest | Max-Heap | Pop largest, keep smallest |

Since Python only has min-heap, we negate for max-heap:
```python
heap = [(-distance, x, y) for x, y in points]
```

### Why Skip `sqrt()`?

```python
# We use x^2 + y^2 instead of sqrt(x^2 + y^2)
distance_squared = x ** 2 + y ** 2
```

Since `sqrt` is monotonic, comparing squared distances gives the same ordering:
- `sqrt(a) < sqrt(b)` if and only if `a < b`

This avoids floating-point operations.

### Alternative: Min-Heap with Size K

```python
def kClosest(points, k):
    # Min-heap of size k, storing (-dist, x, y)
    # Actually, use max-heap logic: push, if size > k, pop max
    heap = []
    for x, y in points:
        dist = -(x ** 2 + y ** 2)  # Negate for max-heap
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)  # Remove farthest point
    return [[x, y] for _, x, y in heap]
```

This is O(N log K) time, better when K << N.

### Alternative: QuickSelect

```python
def kClosest(points, k):
    def distance(p):
        return p[0] ** 2 + p[1] ** 2
    
    points.sort(key=distance)
    return points[:k]
```

Using `sort()` is O(N log N). QuickSelect can achieve O(N) average.

### Comparison of Approaches

| Approach | Time | Space | Best When |
|----------|------|-------|-----------|
| Max-Heap (all points) | O(N + (N-K) log N) | O(N) | K close to N |
| Max-Heap (size K) | O(N log K) | O(K) | K << N |
| Sort | O(N log N) | O(1) or O(N) | Simple case |
| QuickSelect | O(N) average | O(1) | Large N |

### Visual Example

```
points = [[3,3], [5,-1], [-2,4]], k = 2

Distances squared:
  [3,3]:  9 + 9 = 18
  [5,-1]: 25 + 1 = 26
  [-2,4]: 4 + 16 = 20

Max-Heap (negated): [(-26, 5, -1), (-20, -2, 4), (-18, 3, 3)]

Pop until k=2:
  Pop (-26, 5, -1)  <- farthest point removed
  
Remaining: [(-20, -2, 4), (-18, 3, 3)]
Result: [[-2, 4], [3, 3]]  <- 2 closest points
```

## Related Problems

- [703. Kth Largest Element in a Stream](../703.%20Kth%20Largest%20Element%20in%20a%20Stream/) - Similar heap pattern
- [215. Kth Largest Element in an Array](../215.%20Kth%20Largest%20Element%20in%20an%20Array/) - QuickSelect alternative
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - K elements by frequency
