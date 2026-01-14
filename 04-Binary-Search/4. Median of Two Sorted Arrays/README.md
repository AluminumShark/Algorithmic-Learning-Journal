# LeetCode 4: Median of Two Sorted Arrays

## Overview

Find the median of two sorted arrays in O(log(min(m,n))) time using binary search partitioning.

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).

**Example:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3)/2 = 2.5.
```

## Algorithm

### Solution 1: Brute Force (Merge and Sort)

**Key Steps:**
1. Concatenate both arrays
2. Sort the merged array
3. Return middle element (odd length) or average of two middle elements (even length)

### Solution 2: Binary Search (Optimal Partitioning)

**Key Steps:**
1. Ensure A is the smaller array (for efficiency)
2. Binary search on partition position `i` in array A
3. Calculate corresponding partition `j` in array B
4. Check if partition is valid (left elements ≤ right elements)
5. Adjust binary search based on partition validity

## Complexity Analysis

### Solution 1: Brute Force
- **Time Complexity:** O((m+n) * log(m+n)) - sorting merged array
- **Space Complexity:** O(m+n) - storing merged array

### Solution 2: Binary Search
- **Time Complexity:** O(log(min(m, n))) - binary search on smaller array
- **Space Complexity:** O(1) - only uses constant extra space

---

## Detailed Explanation of Binary Search Solution

This section provides an in-depth explanation of the optimal solution, which many find challenging to understand.

### The Core Idea: Partitioning

The median divides a sorted array into two halves. For two sorted arrays, we want to find a **partition** that:
1. Splits the combined elements into two halves
2. All elements in the left half ≤ all elements in the right half

```
Array A:  [1, 3, | 5, 7]      <- partition at position i=2
Array B:  [2, 4, | 6, 8, 9]   <- partition at position j=2

Left half:  {1, 3, 2, 4}  ->  max = 4
Right half: {5, 7, 6, 8, 9}  ->  min = 5
```

### Understanding the Variables

#### `i` and `j` - Partition Positions

```python
i = (L + R) // 2    # Number of elements from A in left half
j = leftSize - i    # Number of elements from B in left half
```

- **`i`**: How many elements we take from array A for the left half
- **`j`**: How many elements we take from array B for the left half
- **`leftSize = total // 2`**: Total elements needed in the left half

**Example:**
```
A = [1, 3, 5], B = [2, 4, 6, 8]
total = 7, leftSize = 3

If i = 1: We take 1 element from A -> [1]
Then j = 3 - 1 = 2: We take 2 elements from B -> [2, 4]
Left half = {1, 2, 4}
```

#### `Aleft`, `Aright`, `Bleft`, `Bright` - Boundary Elements

```python
Aleft  = A[i - 1] if i > 0 else float('-inf')  # Largest element from A in left half
Aright = A[i]     if i < m else float('inf')   # Smallest element from A in right half
Bleft  = B[j - 1] if j > 0 else float('-inf')  # Largest element from B in left half
Bright = B[j]     if j < n else float('inf')   # Smallest element from B in right half
```

**Visual Representation:**
```
Array A:  [ ... Aleft | Aright ... ]
                 ^    ^
              A[i-1]  A[i]

Array B:  [ ... Bleft | Bright ... ]
                 ^    ^
              B[j-1]  B[j]
```

**Why `-inf` and `inf`?**
- If `i = 0`: No elements from A in left half -> `Aleft = -inf` (won't affect max comparison)
- If `i = m`: All elements from A in left half -> `Aright = inf` (won't affect min comparison)
- Same logic applies to B

### The Partition Condition

```python
if Aleft <= Bright and Bleft <= Aright:
    # Valid partition found!
```

**Why these conditions?**

For a valid partition, every element in the left half must be ≤ every element in the right half:

```
Left Half:  {A[0..i-1], B[0..j-1]}   must be ≤   Right Half: {A[i..m-1], B[j..n-1]}
```

We only need to check **cross comparisons** because arrays are already sorted internally:
- `Aleft <= Bright`: Largest from A's left <= Smallest from B's right
- `Bleft <= Aright`: Largest from B's left <= Smallest from A's right

```
     Aleft ------> Bright  (cross check 1)
       |            |
A: [1, 3 | 5, 7]   
B: [2, 4 | 6, 8]
       |            |
     Bleft ------> Aright  (cross check 2)
```

### Adjusting the Binary Search

```python
if Aleft > Bright:
    R = i - 1    # Aleft too big, take fewer elements from A
else:
    L = i + 1    # Bleft too big (Bleft > Aright), take more elements from A
```

**When `Aleft > Bright`:**
- The largest element from A's left is bigger than the smallest from B's right
- We took too many elements from A -> decrease `i`

**When `Bleft > Aright`:**
- The largest element from B's left is bigger than the smallest from A's right
- We took too few elements from A -> increase `i`

### Computing the Median

```python
if total % 2 == 1:
    return min(Aright, Bright)  # Odd: first element of right half
else:
    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0  # Even: average of middle two
```

**Odd total length:**
- Left half has `leftSize` elements, right half has `leftSize + 1` elements
- Median is the smallest element in the right half: `min(Aright, Bright)`

**Even total length:**
- Both halves have equal elements
- Median is average of: largest in left half + smallest in right half
- `(max(Aleft, Bleft) + min(Aright, Bright)) / 2.0`

### Complete Example Walkthrough

```
A = [1, 3], B = [2]
m = 2, n = 1, total = 3, leftSize = 1

Binary Search: L=0, R=2

Iteration 1: i = 1, j = 0
  Aleft = A[0] = 1
  Aright = A[1] = 3
  Bleft = -inf (j=0, no elements from B)
  Bright = B[0] = 2

  Check: Aleft(1) <= Bright(2) OK
         Bleft(-inf) <= Aright(3) OK

  Valid partition!
  total is odd -> return min(Aright, Bright) = min(3, 2) = 2
```

---

## Key Concepts

- **Binary Search on Partition**: Search for the correct split point, not an element
- **Partition Invariant**: Left half elements ≤ Right half elements
- **Cross Comparison**: Only need to check elements at partition boundaries
- **Boundary Handling**: Use `-inf`/`inf` for edge cases

## Pattern Recognition

This problem demonstrates:
- Binary search on answer space (partition position)
- Divide and conquer on sorted data
- Handling edge cases with sentinel values

## Related Problems

- Kth Element of Two Sorted Arrays
- Find K-th Smallest Pair Distance
- Binary search variations

## Files

- `solution.py`: Brute Force and Binary Search partitioning solutions

