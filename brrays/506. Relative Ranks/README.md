# LeetCode 506: Relative Ranks

## Overview

Assign ranks to athletes based on their scores, with special medals for top three positions.

## Problem Description

You are given an integer array `score` of size `n`, where `score[i]` is the score of the ith athlete in a competition. All scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
- The 1st place athlete's rank is "Gold Medal"
- The 2nd place athlete's rank is "Silver Medal"
- The 3rd place athlete's rank is "Bronze Medal"
- For the 4th place and the rest, their rank is their placement number

Return an array `answer` of size `n` where `answer[i]` is the rank of the ith athlete.

**Example:**
```
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
```

## Algorithm

**Shell Sort with Index Preservation**: Sort scores while maintaining original indices, then assign ranks.

**Key Steps:**
1. Pair each score with its original index: `(score, index)`
2. Sort the pairs by score in descending order using Shell Sort
3. Assign ranks based on sorted position:
   - 1st place: "Gold Medal"
   - 2nd place: "Silver Medal"
   - 3rd place: "Bronze Medal"
   - Others: rank number as string

## Complexity Analysis

- **Time Complexity:** O(n^(3/2)) to O(n²) - depends on gap sequence used in Shell Sort
- **Space Complexity:** O(n) - for storing pairs and result array

## Alternative Approaches

1. **Heap-based approach**: O(n log n)
   - Use max heap to get sorted order
   - More predictable time complexity

2. **Sorting with custom comparator**: O(n log n)
   - Use built-in sort with score-index pairs
   - Most straightforward implementation

3. **Counting sort**: O(n + k) where k is score range
   - Efficient if score range is small and bounded

## Implementation Details

- Shell Sort variant for sorting
- Index preservation using tuples `(score, index)`
- Descending order sort (highest score first)
- Special handling for top three positions

## Pattern Recognition

This problem demonstrates:
- Sorting with index preservation
- Rank assignment algorithms
- Custom sorting with metadata
- Score-based ranking systems

## Use Cases

- Leaderboard systems
- Ranking algorithms
- Score-based competitions
- Top-k selection with special handling

## Optimization Note

For better performance, consider:
- Using built-in `sorted()` with custom key (O(n log n))
- Heap-based approach for more predictable complexity
- Counting sort if score range is bounded and small

## Files

- `ShellSort.py`: Shell Sort implementation with rank assignment

