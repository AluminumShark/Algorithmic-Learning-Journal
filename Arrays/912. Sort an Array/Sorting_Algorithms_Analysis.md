# Sorting Algorithms Analysis
## Comprehensive Study for Algorithmic Problem Solving

This document provides a detailed analysis of various sorting algorithms implemented for LeetCode 912 (Sort an Array). Each algorithm is examined with respect to its approach, complexity analysis, and practical considerations.

---

## Table of Contents

1. [O(n²) Comparison-Based Sorts](#on2-comparison-based-sorts)
   - Bubble Sort
   - Selection Sort
   - Insertion Sort
2. [O(n log n) Comparison-Based Sorts](#on-log-n-comparison-based-sorts)
   - Merge Sort
   - Quick Sort (Multiple Variants)
   - Heap Sort
   - Shell Sort
3. [Linear-Time Sorts](#linear-time-sorts)
   - Counting Sort
   - Radix Sort

---

## O(n²) Comparison-Based Sorts

### Bubble Sort

**Algorithm Description:**
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates the list is sorted.

**Key Steps:**
1. Outer loop runs n times (each pass places one element in correct position)
2. Inner loop compares adjacent elements up to the unsorted portion
3. Optimization: early termination if no swaps occur in a pass

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n²) - array in reverse order
  - Average Case: O(n²)
  - Best Case: O(n) - already sorted array (with optimization)
- **Space Complexity:** O(1) - in-place sorting

**Advantages:**
- Simple to understand and implement
- Stable sorting algorithm
- Adaptive: performs well on nearly sorted arrays

**Disadvantages:**
- Very slow for large datasets
- Not practical for production use

**Use Cases:**
- Educational purposes
- Small datasets or nearly sorted arrays
- Not suitable for LeetCode 912 (causes TLE)

---

### Selection Sort

**Algorithm Description:**
Selection Sort divides the input list into two parts: a sorted sublist at the left and an unsorted sublist at the right. The algorithm repeatedly finds the minimum element from the unsorted sublist and places it at the end of the sorted sublist.

**Key Steps:**
1. Outer loop: iterate over each position in the array
2. Inner loop: find the index of the smallest element in the remaining array
3. Swap the minimum element with the current position

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n²)
  - Average Case: O(n²)
  - Best Case: O(n²)
  - Always performs O(n²) comparisons regardless of input
- **Space Complexity:** O(1) - in-place sorting

**Advantages:**
- Simple implementation
- Minimal number of swaps (at most n-1 swaps)
- In-place sorting

**Disadvantages:**
- Always requires O(n²) comparisons
- Not adaptive (performance doesn't improve for partially sorted arrays)
- Not stable (can change relative order of equal elements)

**Use Cases:**
- Educational purposes
- Small datasets where simplicity matters more than performance
- Not suitable for LeetCode 912 (causes TLE)

---

### Insertion Sort

**Algorithm Description:**
Insertion Sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms, but it has several advantages such as adaptive behavior and simplicity.

**Key Steps:**
1. Start from the second element (index 1)
2. For each element, compare it with elements in the sorted portion
3. Shift greater elements to the right
4. Insert the current element into its correct position

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n²) - array in reverse order
  - Average Case: O(n²)
  - Best Case: O(n) - already sorted array
- **Space Complexity:** O(1) - in-place sorting

**Advantages:**
- Simple to implement
- Efficient for small datasets
- Adaptive: efficient for nearly sorted arrays
- Stable sorting algorithm
- Online algorithm: can sort a list as it receives it

**Disadvantages:**
- Inefficient for large datasets
- Quadratic time complexity in worst case

**Use Cases:**
- Small datasets
- Nearly sorted arrays
- As a subroutine in more efficient algorithms (e.g., Timsort)
- Not suitable for LeetCode 912 (causes TLE)

---

## O(n log n) Comparison-Based Sorts

### Merge Sort

**Algorithm Description:**
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, sorts them separately, and then merges them back together. It is one of the most efficient and stable sorting algorithms.

**Key Steps:**
1. **Divide:** Split the array into two halves
2. **Conquer:** Recursively sort both halves
3. **Combine:** Merge the two sorted halves into a single sorted array

**Merge Process:**
- Use two pointers to traverse both sorted subarrays
- Compare elements and add smaller one to result
- Copy remaining elements after one subarray is exhausted

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n log n)
  - Average Case: O(n log n)
  - Best Case: O(n log n)
  - Always performs O(n log n) operations
- **Space Complexity:** O(n) - requires additional array for merging

**Advantages:**
- Guaranteed O(n log n) performance
- Stable sorting algorithm
- Predictable performance
- Well-suited for parallelization

**Disadvantages:**
- Requires O(n) extra space
- Not in-place (unless using in-place merge, which is complex)

**Use Cases:**
- Large datasets where guaranteed O(n log n) is important
- When stability is required
- External sorting (sorting large files)
- Suitable for LeetCode 912

---

### Quick Sort

**Algorithm Description:**
Quick Sort is a divide-and-conquer algorithm that picks a pivot element and partitions the array around the pivot. Elements smaller than pivot go to the left, and elements greater go to the right. The algorithm then recursively sorts the subarrays.

**Key Steps:**
1. Choose a pivot element (random selection to avoid worst case)
2. Partition the array around the pivot
3. Recursively sort the left and right partitions

**Partition Strategies:**
- **Two-pointer approach:** Use left and right pointers moving toward each other
- **Hoare partition:** More efficient with strict comparisons to handle duplicates

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n²) - when pivot is always smallest or largest (rare with randomization)
  - Average Case: O(n log n)
  - Best Case: O(n log n)
- **Space Complexity:** O(log n) - recursion stack depth (in-place version)

**Advantages:**
- Average-case O(n log n) performance
- In-place sorting
- Cache-friendly (good locality of reference)
- Often faster than Merge Sort in practice

**Disadvantages:**
- Worst-case O(n²) time complexity
- Not stable (can change relative order of equal elements)
- Performance depends on pivot selection

**Optimizations:**
- Random pivot selection to avoid worst case
- Strict comparisons in partition to handle duplicates efficiently
- Hybrid approach: switch to Insertion Sort for small subarrays

**Variants Implemented:**
1. **Classic Quick Sort:** Two-pointer partition with random pivot
2. **Hoare Partition:** More efficient partition scheme with strict comparisons
3. **Pythonic Quick Sort:** Non-in-place version using list comprehensions (inefficient for large inputs)

**Use Cases:**
- General-purpose sorting where average performance matters
- When in-place sorting is preferred
- May cause TLE on LeetCode 912 in worst-case scenarios

---

### Heap Sort

**Algorithm Description:**
Heap Sort uses a binary heap data structure to sort elements. It first builds a heap from the input data, then repeatedly extracts the minimum (or maximum) element from the heap and rebuilds the heap.

**Key Steps:**
1. Build a min-heap from all elements
2. Extract the minimum element repeatedly
3. Each extraction removes the root and maintains heap property

**Heap Operations:**
- **Heapify Up:** Restore heap property when inserting (bubble up)
- **Heapify Down:** Restore heap property when removing root (bubble down)

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n log n)
  - Average Case: O(n log n)
  - Best Case: O(n log n)
  - Always performs O(n log n) operations
- **Space Complexity:** O(n) - for the heap storage (can be optimized to O(1) with in-place heap construction)

**Advantages:**
- Guaranteed O(n log n) performance
- In-place sorting possible (with array-based heap)
- No worst-case O(n²) scenario like Quick Sort

**Disadvantages:**
- Slower than Quick Sort in practice (more comparisons)
- Not stable
- Cache-unfriendly (heap operations access memory in unpredictable patterns)

**Use Cases:**
- When guaranteed O(n log n) is required
- Priority queue operations
- Suitable for LeetCode 912

---

### Shell Sort

**Algorithm Description:**
Shell Sort is an optimization of Insertion Sort that allows exchange of items that are far apart. It sorts elements that are a certain distance (gap) apart and reduces the gap until it becomes 1 (at which point it becomes Insertion Sort).

**Key Steps:**
1. Start with a large gap (typically n/2)
2. Perform gapped insertion sort for each gap value
3. Gradually reduce the gap (usually by half)
4. When gap becomes 1, perform final insertion sort

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n²) - with gap sequence of n/2, n/4, ...
  - Average Case: O(n^(3/2)) to O(n log² n) - depends on gap sequence
  - Best Case: O(n log n) - with certain gap sequences
- **Space Complexity:** O(1) - in-place sorting

**Advantages:**
- More efficient than simple O(n²) algorithms
- In-place sorting
- Adaptive: performs well on partially sorted arrays
- Simple to implement

**Disadvantages:**
- Time complexity depends heavily on gap sequence
- Not stable
- Not as fast as O(n log n) algorithms for large datasets

**Use Cases:**
- Medium-sized datasets
- When in-place sorting is preferred
- Suitable for LeetCode 912 (accepted)

---

## Linear-Time Sorts

### Counting Sort

**Algorithm Description:**
Counting Sort is a non-comparison based sorting algorithm that sorts integers by counting the number of occurrences of each unique value. It works well when the range of input values is small compared to the number of elements.

**Key Steps:**
1. Find the range of input values (min and max)
2. Initialize a counting array to store frequency of each value
3. Count occurrences of each number
4. Compute cumulative counts (prefix sums) to determine positions
5. Build the sorted result array using cumulative counts

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(n + k) - where k is the range of input values
  - Average Case: O(n + k)
  - Best Case: O(n + k)
  - Linear time when k = O(n)
- **Space Complexity:** O(k) - for the counting array

**Advantages:**
- Linear time complexity when range is small
- Stable sorting algorithm
- Simple to implement

**Disadvantages:**
- Only works for integer inputs
- Requires knowing the range of input values
- Inefficient when k is much larger than n

**Use Cases:**
- Integer sorting with small value range
- As a subroutine in Radix Sort
- Suitable for LeetCode 912 when value range is manageable

---

### Radix Sort

**Algorithm Description:**
Radix Sort is a non-comparison based sorting algorithm that sorts numbers by processing individual digits. It processes digits from least significant to most significant, using a stable sort (typically Counting Sort) for each digit position.

**Key Steps:**
1. Find the maximum number of digits (d) in the input
2. For each digit position from least to most significant:
   - Group numbers by the current digit
   - Recombine groups in order
3. After processing all digits, array is sorted

**Handling Negative Numbers:**
- Separate negative and non-negative numbers
- Sort negatives separately (convert to positive, sort, then reverse and negate)
- Combine sorted negatives with sorted non-negatives

**Complexity Analysis:**
- **Time Complexity:**
  - Worst Case: O(d × (n + k)) - where d is number of digits, k is base (typically 10)
  - Average Case: O(d × (n + k))
  - Best Case: O(d × (n + k))
  - Linear when d is constant and k = O(n)
- **Space Complexity:** O(n + k) - for buckets and counting arrays

**Advantages:**
- Linear time complexity when d is small
- Stable sorting algorithm
- Works well for integers with fixed number of digits

**Disadvantages:**
- Only works for integer inputs
- Requires additional space for buckets
- Not as flexible as comparison-based sorts

**Variants Implemented:**
1. **Basic Radix Sort:** Only handles non-negative integers
2. **Fixed Radix Sort:** Handles both negative and non-negative integers

**Use Cases:**
- Sorting integers with small number of digits
- When integer range is large but digit count is small
- Suitable for LeetCode 912

---

## Comparative Summary

### Time Complexity Comparison

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Shell Sort | O(n log n) | O(n^(3/2)) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) |
| Radix Sort | O(d × n) | O(d × n) | O(d × n) |

### Space Complexity Comparison

| Algorithm | Space Complexity | Notes |
|-----------|------------------|-------|
| Bubble Sort | O(1) | In-place |
| Selection Sort | O(1) | In-place |
| Insertion Sort | O(1) | In-place |
| Shell Sort | O(1) | In-place |
| Merge Sort | O(n) | Requires auxiliary array |
| Quick Sort | O(log n) | Recursion stack |
| Heap Sort | O(n) | Heap storage (can be O(1) optimized) |
| Counting Sort | O(k) | Counting array |
| Radix Sort | O(n + k) | Buckets and counting arrays |

### Stability Comparison

| Algorithm | Stable | Notes |
|-----------|--------|-------|
| Bubble Sort | Yes | Adjacent swaps maintain order |
| Selection Sort | No | Swapping can change order of equals |
| Insertion Sort | Yes | Shifts maintain relative order |
| Shell Sort | No | Long-distance swaps |
| Merge Sort | Yes | Merge preserves relative order |
| Quick Sort | No | Partition can change order |
| Heap Sort | No | Heap operations not stable |
| Counting Sort | Yes | Stable implementation uses cumulative counts |
| Radix Sort | Yes | Requires stable subroutine |

---

## Practical Considerations for LeetCode 912

### Recommended Algorithms

1. **Merge Sort:** Guaranteed O(n log n), stable, predictable
2. **Heap Sort:** Guaranteed O(n log n), in-place possible
3. **Counting Sort:** Linear time when value range is small
4. **Radix Sort:** Linear time for integer inputs with small digit count
5. **Shell Sort:** Acceptable for medium datasets

### Algorithms to Avoid

1. **Bubble Sort, Selection Sort, Insertion Sort:** Cause TLE on large inputs
2. **Quick Sort (unoptimized):** May cause TLE on worst-case inputs (many duplicates, nearly sorted)

### Optimization Strategies

1. **Random Pivot Selection:** Mitigates worst-case performance in Quick Sort
2. **Strict Comparisons:** Prevents infinite loops on duplicate values
3. **Early Termination:** Improves best-case performance (Bubble Sort)
4. **Hybrid Approaches:** Combine different algorithms for optimal performance

---

## Conclusion

Understanding various sorting algorithms and their complexity characteristics is fundamental to algorithmic problem-solving. Each algorithm has its strengths and weaknesses:

- **Comparison-based sorts** are flexible but limited by O(n log n) lower bound
- **Non-comparison sorts** can achieve linear time but have restrictions on input type
- **Trade-offs** between time complexity, space complexity, stability, and practical performance must be considered

For competitive programming and technical interviews, Merge Sort, Heap Sort, and Counting Sort (when applicable) are reliable choices. Quick Sort can be faster in practice but requires careful implementation to avoid worst-case scenarios.

