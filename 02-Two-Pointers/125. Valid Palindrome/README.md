# LeetCode 125: Valid Palindrome

## Overview

Determine if a string is a palindrome using two pointers, considering only alphanumeric characters and ignoring cases.

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
```

## Algorithm

**Two Pointers Approach**:

**Key Steps:**
1. Initialize left and right pointers at string ends
2. Skip non-alphanumeric characters from both ends
3. Compare characters (case-insensitive)
4. If mismatch found, return false
5. If pointers meet/cross, return true

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the string
- **Space Complexity:** O(1) - only uses pointers

## Key Concepts

- **Two Pointers**: Compare from both ends
- **Character Filtering**: Skip non-alphanumeric
- **Case Insensitivity**: Use `.lower()` for comparison

## Implementation Details

### Character Methods
```python
s[L].isalnum()  # Returns True if alphanumeric
s[L].lower()    # Returns lowercase version
```

### Why `continue`?
Using `continue` makes the logic cleaner:
```python
if not s[L].isalnum():
    L += 1
    continue  # Skip to next iteration
```

## Pattern Recognition

This problem demonstrates:
- Two pointers for string comparison
- Character filtering/validation
- In-place string processing

## Alternative Approach

### Clean String First
```python
def isPalindrome(self, s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```
- Time: O(n), Space: O(n)
- Simpler but uses extra space

## Related Problems

- Valid Palindrome II (LeetCode 680)
- Palindrome Linked List
- Palindrome Number

## Edge Cases

- Empty string (is palindrome)
- Single character (is palindrome)
- Only non-alphanumeric characters
- Mixed case
- Spaces and punctuation

## Files

- `solution.py`: Two pointers implementation

