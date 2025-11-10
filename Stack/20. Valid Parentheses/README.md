# LeetCode 20: Valid Parentheses

## Overview

Determine if a string containing parentheses, brackets, and braces is valid using a stack-based approach.

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

**Example:**
```
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

## Algorithm

**Stack-Based Matching**: Use a stack to track opening brackets and match them with closing brackets.

**Key Steps:**
1. Early return for odd-length strings (cannot be valid)
2. Iterate through each character:
   - If opening bracket `([{`: push to stack
   - If closing bracket `)]}`: 
     - Check if stack is non-empty and top matches
     - If match: pop from stack
     - If no match: return false immediately
3. After processing all characters, stack must be empty

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the string
- **Space Complexity:** O(n) - worst case when all characters are opening brackets

## Key Insight

The stack maintains the order of opening brackets. When we encounter a closing bracket, it must match the most recent unmatched opening bracket (LIFO property).

## Implementation Details

- **Early Optimization**: Check odd-length strings first
- **Direct Matching**: Compare closing bracket with stack top
- **Immediate Failure**: Return false as soon as mismatch detected
- **Final Validation**: Stack must be empty for valid string

## Pattern Recognition

This problem demonstrates:
- Stack LIFO property for matching pairs
- Parentheses/brackets validation pattern
- Early termination optimization

## Use Cases

- Expression validation
- Code syntax checking
- XML/HTML tag matching
- Nested structure validation

## Related Problems

- Minimum Remove to Make Valid Parentheses
- Longest Valid Parentheses
- Remove Invalid Parentheses
- Generate Parentheses

## Edge Cases

- Empty string (valid)
- Odd-length string (invalid)
- Only opening brackets
- Only closing brackets
- Nested valid brackets
- Unmatched brackets

## Files

- `Stack.py`: Stack-based validation implementation

