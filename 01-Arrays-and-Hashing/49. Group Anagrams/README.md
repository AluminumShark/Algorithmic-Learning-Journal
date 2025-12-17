# LeetCode 49: Group Anagrams

## Overview

Group strings that are anagrams of each other using hash map with clever key generation.

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Example:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]
```

## Algorithm

### Solution 1: Sorting

**Key Steps:**
1. For each string, sort its characters to create a canonical key
2. Group strings with the same sorted key together
3. Return all groups

### Solution 2: Character Count

**Key Steps:**
1. For each string, create a count array of 26 characters
2. Use the count tuple as a hash key
3. Group strings with the same count signature

## Complexity Analysis

### Solution 1: Sorting
- **Time Complexity:** O(m × n log n) - where m is number of strings, n is average string length
- **Space Complexity:** O(m × n) - storing all strings in groups

### Solution 2: Character Count
- **Time Complexity:** O(m × n) - linear scan of each character
- **Space Complexity:** O(m × n) - storing all strings plus O(26) for count array

## Key Concepts

- **Hash Map Grouping**: Use canonical form as key
- **Anagram Signature**: Sorted string or character count
- **defaultdict**: Simplifies group initialization

## Implementation Details

### Sorting Approach
- `sorted(s)` returns list of characters
- `''.join()` converts back to string key
- Simple but has O(n log n) per string

### Character Count Approach
- Fixed-size array for lowercase letters
- `ord(char) - ord('a')` maps 'a'-'z' to 0-25
- `tuple(count)` makes it hashable for dict key

## Pattern Recognition

This problem demonstrates:
- Hash map for grouping elements
- Canonical form generation
- Trade-off between time and implementation complexity

## Related Problems

- Valid Anagram (LeetCode 242)
- Find All Anagrams in a String (LeetCode 438)
- Find Resultant Array After Removing Anagrams

## Edge Cases

- Empty strings
- Single character strings
- All strings are anagrams
- No anagrams exist
- Strings with all same characters

## Files

- `solution.py`: Sorting and Character Count implementations

