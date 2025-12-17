# LeetCode 28: Find the Index of the First Occurrence in a String

## Overview

Implement string matching algorithms to find the first occurrence of a pattern (needle) in a text (haystack), demonstrating multiple approaches including brute force, KMP, and Rabin-Karp algorithms.

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example:**
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "haystack".
```

## Algorithm Implementations

### 1. KMP Algorithm (Recommended)
**Time Complexity:** O(n + m) - where n is text length, m is pattern length  
**Space Complexity:** O(m) - for the LPS (Longest Prefix Suffix) array

**Key Steps:**
1. **Build LPS Array**: Preprocess pattern to find longest prefix-suffix for each position
2. **Pattern Matching**: Use LPS array to avoid unnecessary comparisons
   - On mismatch, use LPS to determine next comparison position
   - Avoids backtracking in text

**Advantages:**
- Linear time complexity
- No backtracking in text
- Optimal for repeated patterns

### 2. Brute Force
**Time Complexity:** O(n × m) - worst case  
**Space Complexity:** O(1)

**Key Steps:**
1. Try matching pattern at each position in text
2. On mismatch, shift pattern by one position
3. Continue until match found or text exhausted

**Characteristics:**
- Simple to implement
- Inefficient for large inputs
- Good for educational purposes

### 3. Rabin-Karp Algorithm
**Time Complexity:** O(n × m) worst case, O(n + m) average case  
**Space Complexity:** O(1)

**Key Steps:**
1. Compute hash of pattern
2. Slide window over text, compute hash of each substring
3. Compare hashes first, then verify character-by-character if hashes match

**Characteristics:**
- Hash-based approach
- Average case efficient
- Requires collision handling

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Best For |
|-----------|----------------|------------------|----------|
| KMP | O(n + m) | O(m) | General purpose |
| Brute Force | O(n × m) | O(1) | Simple cases |
| Rabin-Karp | O(n + m) avg | O(1) | Multiple patterns |

## Key Insights

### KMP Algorithm
- **LPS Array**: Stores length of longest proper prefix which is also suffix
- **No Backtracking**: Text pointer never moves backward
- **Efficient**: Each character in text is examined at most once

### Brute Force
- **Simple**: Easy to understand and implement
- **Inefficient**: May re-examine same characters multiple times

### Rabin-Karp
- **Hash-based**: Uses rolling hash for efficiency
- **Collision Handling**: Must verify matches character-by-character
- **Multiple Patterns**: Can search for multiple patterns efficiently

## Implementation Details

### KMP - LPS Construction
```python
# Build prefix table (LPS array)
for right in range(1, m):
    while left > 0 and p[left] != p[right]:
        left = next[left - 1]  # Fall back
    if p[left] == p[right]:
        left += 1
    next[right] = left
```

### KMP - Pattern Matching
```python
# Use LPS to avoid backtracking
for i in range(n):
    while j > 0 and T[i] != p[j]:
        j = next[j - 1]  # Use LPS to skip
    if T[i] == p[j]:
        j += 1
    if j == m:
        return i - j + 1  # Match found
```

## Pattern Recognition

This problem demonstrates:
- String matching algorithms
- Pattern preprocessing techniques
- Optimization strategies
- Trade-offs between algorithms

## Use Cases

- Text search engines
- DNA sequence matching
- Pattern recognition
- String processing libraries

## Related Problems

- Repeated Substring Pattern
- Shortest Palindrome
- Implement strStr() variations
- String matching in multiple texts

## Edge Cases

- Empty needle (return 0)
- Needle longer than haystack (return -1)
- Needle not found (return -1)
- Multiple occurrences (return first)
- Needle equals haystack (return 0)

## Algorithm Selection Guide

- **KMP**: Best for general-purpose string matching
- **Brute Force**: Simple cases, educational purposes
- **Rabin-Karp**: Multiple pattern search, rolling hash scenarios

## Files

- `KMP.py`: Knuth-Morris-Pratt algorithm implementation
- `BruteForce.py`: Simple brute force approach
- `Rabin-Karp.py`: Hash-based Rabin-Karp algorithm

