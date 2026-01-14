# LeetCode 242: Valid Anagram

## Overview

Determine if two strings are anagrams of each other using character frequency counting.

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

**Example:**
```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

## Algorithm

### Solution 1: Hash Map

**Key Steps:**
1. Early return if lengths differ (cannot be anagrams)
2. Count character frequencies in string `s`
3. Decrement counts while iterating through string `t`
4. If any count goes negative or character not found, return false

### Solution 2: Counter (One-liner)

Use Python's `Counter` class to compare character frequencies directly.

## Complexity Analysis

### Solution 1: Hash Map
- **Time Complexity:** O(n) - two passes through the strings
- **Space Complexity:** O(k) - where k is the character set size (26 for lowercase letters)

### Solution 2: Counter
- **Time Complexity:** O(n) - Counter builds frequency map
- **Space Complexity:** O(k) - stores character frequencies

## Key Concepts

- **Hash Map**: Character frequency counting
- **Early Termination**: Length check optimization
- **Pattern**: Anagram detection via frequency comparison

## Implementation Details

### Hash Map Approach
- Use dictionary to store character counts
- `count.get(char, 0)` handles missing keys
- Decrement and check for negative values

### Counter Approach
- More Pythonic and concise
- Built-in comparison handles all edge cases

## Pattern Recognition

This problem demonstrates:
- Character frequency counting pattern
- Hash map for O(1) lookups
- Early termination optimization

## Related Problems

- Group Anagrams (LeetCode 49)
- Find All Anagrams in a String (LeetCode 438)
- Valid Palindrome (LeetCode 125)

## Edge Cases

- Empty strings (both empty -> true)
- Different lengths (always false)
- Single character strings
- Strings with repeated characters

## Files

- `solution.py`: Hash Map and Counter implementations

