# LeetCode 912: Sort an Array - Comprehensive Sorting Algorithms Study

## Overview

This directory contains an in-depth study of sorting algorithms implemented for LeetCode Problem 912 (Sort an Array). The project demonstrates systematic learning and analysis of fundamental sorting techniques, from basic quadratic-time algorithms to advanced linear-time approaches.

## Project Structure

```
912. Sort an Array/
├── README.md                          # This file
├── Sorting_Algorithms_Analysis.md     # Comprehensive analysis document
├── BubbleSort.py                      # O(n²) comparison-based sort
├── SelectionSort.py                   # O(n²) comparison-based sort
├── InsertionSort.py                   # O(n²) comparison-based sort
├── ShellSort.py                       # Improved insertion sort variant
├── MergeSort.py                       # O(n log n) divide-and-conquer
├── QuickSort.py                       # O(n log n) average-case partition-based
├── QuickSortHoare.py                  # Quick Sort with Hoare partition scheme
├── QuickSortPythonic.py               # Quick Sort using list comprehensions
├── HeapSort.py                        # O(n log n) heap-based sort
├── CountingSort.py                    # O(n + k) linear-time integer sort
├── RadixSort.py                       # O(d × n) digit-based sort (non-negative)
└── RadixSortFixed.py                  # Radix Sort with negative number support
```

## Documentation

### Main Analysis Document

**Sorting_Algorithms_Analysis.md** provides a comprehensive analysis including:
- Detailed algorithm descriptions and implementations
- Time and space complexity analysis for each algorithm
- Comparative analysis tables
- Practical considerations for competitive programming
- Recommendations for LeetCode 912

## Algorithm Categories

### 1. Quadratic-Time Comparison Sorts (O(n²))
- **Bubble Sort**: Adjacent element swapping with early termination optimization
- **Selection Sort**: Repeated minimum element selection
- **Insertion Sort**: Builds sorted array incrementally

**Note**: These algorithms demonstrate TLE (Time Limit Exceeded) on LeetCode 912 but serve as important educational examples of fundamental sorting concepts.

### 2. Sub-Quadratic Comparison Sorts
- **Shell Sort**: Gap-based insertion sort optimization (typically O(n^(3/2)))

### 3. Efficient Comparison Sorts (O(n log n))
- **Merge Sort**: Stable divide-and-conquer algorithm with guaranteed O(n log n) performance
- **Quick Sort**: Efficient average-case performance with multiple partitioning strategies
- **Heap Sort**: Heap-based sorting with guaranteed O(n log n) complexity

### 4. Linear-Time Non-Comparison Sorts
- **Counting Sort**: Integer sorting with O(n + k) complexity where k is the value range
- **Radix Sort**: Digit-by-digit sorting achieving O(d × n) where d is the number of digits

## Implementation Notes

### Code Quality
- All implementations follow consistent class structure with `Solution` class
- Type hints used throughout for clarity (`from typing import List`)
- Comprehensive comments explaining algorithm steps
- Production considerations noted (e.g., TLE warnings, optimization strategies)

### Key Features
- Multiple variants of Quick Sort demonstrating different partition schemes
- Negative number handling in Radix Sort implementation
- Early termination optimizations where applicable
- Randomized pivot selection for Quick Sort to avoid worst-case scenarios

## Complexity Summary

| Algorithm | Time Complexity | Space Complexity | Stability | Status on LC 912 |
|-----------|----------------|------------------|-----------|------------------|
| Bubble Sort | O(n²) | O(1) | Stable | TLE |
| Selection Sort | O(n²) | O(1) | Unstable | TLE |
| Insertion Sort | O(n²) | O(1) | Stable | TLE |
| Shell Sort | O(n^(3/2)) | O(1) | Unstable | Accepted |
| Merge Sort | O(n log n) | O(n) | Stable | Accepted |
| Quick Sort | O(n log n) avg | O(log n) | Unstable | Accepted* |
| Heap Sort | O(n log n) | O(n) | Unstable | Accepted |
| Counting Sort | O(n + k) | O(k) | Stable | Accepted |
| Radix Sort | O(d × n) | O(n + k) | Stable | Accepted |

*Quick Sort may cause TLE on worst-case inputs with many duplicates

## Learning Objectives

This project demonstrates:

1. **Systematic Algorithm Study**: Comprehensive coverage of major sorting algorithms
2. **Complexity Analysis**: Detailed time and space complexity understanding
3. **Practical Problem Solving**: Application to competitive programming challenges
4. **Code Quality**: Clean, well-documented, and maintainable implementations
5. **Trade-off Analysis**: Understanding when to use which algorithm based on constraints

## Usage

Each Python file can be run independently and contains a `Solution` class with a `sortArray` method compatible with LeetCode 912's interface:

```python
from typing import List

solution = Solution()
sorted_array = solution.sortArray([5, 2, 3, 1])
```

## References

- LeetCode Problem: [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)
- Comprehensive analysis available in `Sorting_Algorithms_Analysis.md`

---

**Note**: This project is part of a larger algorithmic learning journal demonstrating systematic study of computer science fundamentals for graduate-level computer science applications.

