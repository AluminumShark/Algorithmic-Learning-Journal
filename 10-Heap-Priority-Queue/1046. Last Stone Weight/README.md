# 1046. Last Stone Weight

## Problem Description

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.

**Example:**
```
Input: stones = [2,7,4,1,8,1]
Output: 1

Explanation:
- Smash 7 and 8: [2,4,1,1,1]
- Smash 4 and 2: [2,1,1,1]
- Smash 2 and 1: [1,1,1]
- Smash 1 and 1: [1]
- Return 1
```

## Solution: Max-Heap Simulation with Negation

```python
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python's heap is min-heap, so we negate values to simulate max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x1 = heapq.heappop(heap)  # Largest (most negative)
            x2 = heapq.heappop(heap)  # Second largest
            if x1 == x2:
                continue
            else:
                heapq.heappush(heap, -abs(x1 - x2))
        return -heap[0] if heap else 0
```

**Complexity:**
- **Time:** O(N log N) - Each smash is O(log N), at most N-1 smashes
- **Space:** O(N) - Heap stores all stones

## Key Concepts

### Python heapq is Min-Heap: The Negation Trick

**Problem:** Python's `heapq` only provides a **min-heap**, but we need a **max-heap** to always get the two heaviest stones.

**Solution:** Store **negative values**! The smallest negative is the largest original value.

```python
stones = [2, 7, 4, 1, 8, 1]
heap = [-2, -7, -4, -1, -8, -1]  # Negate all

heappop(heap)  # Returns -8 (most negative = largest original)
heappop(heap)  # Returns -7 (second largest)
```

### The Negation Pattern

| Operation | Min-Heap | Max-Heap (Simulated) |
|-----------|----------|---------------------|
| Insert x | `heappush(heap, x)` | `heappush(heap, -x)` |
| Get max | N/A | `-heap[0]` |
| Pop max | N/A | `-heappop(heap)` |

### Walkthrough

```
stones = [2, 7, 4, 1, 8, 1]
heap = [-8, -7, -4, -1, -2, -1]  (after heapify)

Round 1:
  Pop -8 and -7 (stones 8 and 7)
  Difference: |(-8) - (-7)| = 1
  Push -1
  heap = [-4, -2, -1, -1, -1]

Round 2:
  Pop -4 and -2 (stones 4 and 2)
  Difference: 2
  Push -2
  heap = [-2, -1, -1, -1]

Round 3:
  Pop -2 and -1 (stones 2 and 1)
  Difference: 1
  Push -1
  heap = [-1, -1, -1]

Round 4:
  Pop -1 and -1 (stones 1 and 1)
  Equal, no push
  heap = [-1]

Return: -(-1) = 1
```

### Why `abs(x1 - x2)`?

Since both x1 and x2 are negative, their difference can be tricky:

```python
x1 = -8, x2 = -7
x1 - x2 = -8 - (-7) = -1

# We want the weight difference: |8 - 7| = 1
# So we use abs(x1 - x2) = 1, then negate to push -1
```

### Edge Cases

| Case | Result |
|------|--------|
| Empty array | 0 |
| Single stone | That stone's weight |
| All equal stones (even count) | 0 |
| All equal stones (odd count) | Stone weight |

### Alternative: Using `nlargest`

```python
import heapq
def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        diff = stones[-1] - stones[-2]
        stones = stones[:-2]
        if diff:
            stones.append(diff)
    return stones[0] if stones else 0
```

This is O(N^2 log N) - simpler but slower.

## Related Problems

- [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) - DP version (harder)
- [703. Kth Largest Element in a Stream](../703.%20Kth%20Largest%20Element%20in%20a%20Stream/) - Heap fundamentals
- [215. Kth Largest Element in an Array](../215.%20Kth%20Largest%20Element%20in%20an%20Array/) - Heap vs QuickSelect
