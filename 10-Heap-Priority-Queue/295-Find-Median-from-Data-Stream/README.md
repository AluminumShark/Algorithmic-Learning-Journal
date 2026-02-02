# 295. Find Median from Data Stream

## Problem Description

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far.

**Example:**
```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

## Solutions

### Solution 1: Sorting (Brute Force)

**Approach:** Maintain a sorted list and return the middle element(s).

**Algorithm:**
1. `addNum`: Append the number and sort the entire list
2. `findMedian`: Return the middle element(s)

**Complexity:**
- **Time:** O(N log N) per `addNum`, O(1) per `findMedian`
- **Space:** O(N)

**Why it's slow:** Re-sorting the entire list every time we add a number is inefficient.

---

### Solution 2: Two Heaps (Optimal) ⭐

**Approach:** Use two heaps to maintain the left and right halves of the sorted data.

### Key Insight: Divide and Conquer

Imagine dividing a sorted array into two halves:
```
[1, 2, 3, 4] | [5, 6, 7, 8, 9]
  ← small →      ← large →
  (left half)    (right half)

Median = middle element(s)
- If odd: top of small
- If even: average of (top of small, top of large)
```

**To efficiently find median:**
1. Keep the **smaller half** in a **max-heap** (easy access to largest of small values)
2. Keep the **larger half** in a **min-heap** (easy access to smallest of large values)
3. Balance the heaps so their sizes differ by at most 1

### Data Structures

- **`small`** (Max-Heap): Stores the smaller half of numbers
  - Implemented as min-heap with negative values
  - Top element: largest in the smaller half
- **`large`** (Min-Heap): Stores the larger half of numbers
  - Standard min-heap
  - Top element: smallest in the larger half

### Invariants

1. **Ordering**: All elements in `small` ≤ all elements in `large`
2. **Size balance**: `len(small)` = `len(large)` OR `len(small)` = `len(large) + 1`

### Algorithm

**`addNum(num)`:**
```python
1. Push num to small (as max-heap, store -num)
2. Move top of small to large (ensures ordering invariant)
3. If large has more elements than small, balance by moving top of large to small
```

**Why this works:**
- Step 1: Temporarily add to small
- Step 2: Ensure largest of small ≤ smallest of large (ordering)
- Step 3: Ensure size balance (small can have at most 1 more element)

**`findMedian()`:**
```python
If len(small) > len(large):
    return top of small (odd count)
Else:
    return average of (top of small, top of large) (even count)
```

### Visual Example

```
Initial: small = [], large = []

addNum(1):
  small = [-1], large = []
  median = 1

addNum(2):
  small = [-1], large = [2]
  median = (1 + 2) / 2 = 1.5

addNum(3):
  small = [-2, -1], large = [3]
  median = 2

addNum(4):
  small = [-2, -1], large = [3, 4]
  median = (2 + 3) / 2 = 2.5

State visualization:
small (max-heap): [2, 1] → largest on top
large (min-heap): [3, 4] → smallest on top
                    ↑   ↑
                median candidates
```

### Complexity Analysis

**Time Complexity:**
- `addNum`: O(log N) - 3 heap operations, each O(log N)
- `findMedian`: O(1) - just access heap tops

**Space Complexity:**
- O(N) - store N elements across two heaps

### Why Two Heaps?

**Alternative approaches:**

| Approach | addNum | findMedian | Why Two Heaps is Better |
|----------|--------|------------|------------------------|
| Sorting | O(N log N) | O(1) | Avoids re-sorting entire array |
| BST | O(log N) | O(N) | Avoids tree traversal to find middle |
| Ordered List + Binary Search | O(N) | O(1) | Avoids shifting elements on insert |
| Two Heaps | O(log N) | O(1) | ✅ Best of both worlds |

### Edge Cases Handled

1. **Empty data stream**: `small` and `large` both empty
2. **Single element**: Only `small` has one element
3. **Duplicate elements**: Heaps handle duplicates naturally
4. **Negative numbers**: Work with both max-heap (negated) and min-heap

## Key Concepts

### 1. Max-Heap in Python

Python's `heapq` only provides min-heap. To simulate max-heap:
```python
# Store negative values
heapq.heappush(max_heap, -value)
max_value = -heapq.heappop(max_heap)
```

### 2. Median Definition

- **Odd count**: Middle element (index `n // 2`)
- **Even count**: Average of two middle elements (indices `n // 2 - 1` and `n // 2`)

### 3. Two-Pointer Mental Model

Think of the heap tops as two pointers:
```
[.... small heap ....]  [.... large heap ....]
                   ↑    ↑
               left mid  right mid
```

### 4. Invariant Maintenance

The algorithm maintains two invariants:
1. **Value invariant**: `max(small) ≤ min(large)`
2. **Size invariant**: `|len(small) - len(large)| ≤ 1`

Always enforce value invariant first, then size invariant.

### 5. Why Small Gets Extra Element?

When the total count is odd, `small` gets the extra element:
- Makes `findMedian` logic cleaner
- Median is always `top of small` when sizes differ

## Step-by-Step Example

```python
medianFinder = MedianFinder()

# Add 5
small = [-5], large = []
median = 5

# Add 15
# Step 1: push to small → [-15, -5]
# Step 2: move top to large → small = [-5], large = [15]
# Step 3: balanced
median = (5 + 15) / 2 = 10

# Add 1
# Step 1: push to small → [-5, -1]
# Step 2: move top to large → small = [-1], large = [5, 15]
# Step 3: large > small, rebalance → small = [-5, -1], large = [15]
median = 5

# Add 3
# Step 1: push to small → [-5, -3, -1]
# Step 2: move top to large → small = [-3, -1], large = [5, 15]
# Step 3: balanced
median = (3 + 5) / 2 = 4
```

## Alternative: Self-Balancing BST

Another O(log N) approach using a self-balancing BST (like AVL or Red-Black Tree):
- Insert: O(log N)
- Find median: O(log N) to find the middle node

**Trade-off:**
- More complex to implement
- Requires maintaining size/rank information at each node
- Two heaps are simpler and achieve same time complexity

## Related Problems

- [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
- [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [502. IPO](https://leetcode.com/problems/ipo/)

## Interview Tips

1. **Clarify constraints**: Can numbers be negative? Duplicates allowed?
2. **Start with brute force**: Mention sorting approach first
3. **Optimize with two heaps**: Explain the divide-and-conquer insight
4. **Explain invariants**: Show you understand why the algorithm is correct
5. **Handle edge cases**: Empty stream, single element, even/odd counts

## Conclusion

The **Two Heaps** approach is a classic example of using the right data structures to achieve optimal time complexity. By dividing the problem space in half and using heaps to efficiently access the boundary elements, we reduce `addNum` from O(N log N) to O(log N) while maintaining O(1) median lookup.

This pattern appears in many streaming data problems where we need to maintain statistics (median, percentiles) dynamically.
