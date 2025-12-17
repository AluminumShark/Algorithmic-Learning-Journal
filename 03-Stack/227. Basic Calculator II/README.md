# LeetCode 227: Basic Calculator II

## Overview

Evaluate a mathematical expression string containing `+`, `-`, `*`, `/` and non-negative integers, respecting operator precedence.

## Problem Description

Given a string `s` which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2³¹, 2³¹ - 1]`.

**Example:**
```
Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1
```

## Algorithm

**Stack-Based Evaluation with Operator Precedence**: Process numbers and operators, using stack to handle precedence.

**Key Steps:**
1. Initialize stack and default operator as `'+'`
2. Parse string character by character:
   - Skip whitespace
   - If digit: parse complete number (handle multi-digit)
   - Apply previous operator to number:
     - `+`: push number to stack
     - `-`: push negative number to stack
     - `*`: pop top, multiply, push result
     - `/`: pop top, divide, push result (truncate toward zero)
   - If operator: update current operator
3. Sum all values in stack for final result

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the string
- **Space Complexity:** O(n) - stack storage for numbers

## Key Insight

By processing `*` and `/` immediately and storing `+`/`-` operations in the stack:
- High precedence operators (`*`, `/`) are evaluated immediately
- Low precedence operators (`+`, `/`) are deferred to the end
- Final sum of stack gives correct result

## Implementation Details

### Number Parsing
- Manual parsing using ASCII subtraction: `ord(char) - ord('0')`
- Handle multi-digit numbers by accumulating digits
- Continue parsing while next character is digit

### Operator Handling
- Default operator is `'+'` for first number
- Apply previous operator when encountering new number
- Update operator when encountering operator character

### Division Truncation
- Use `int()` to truncate toward zero (not floor division)
- Handles negative numbers correctly

## Pattern Recognition

This problem demonstrates:
- Stack-based expression evaluation
- Operator precedence handling
- Deferred evaluation pattern
- String parsing techniques

## Use Cases

- Expression evaluators
- Calculator implementations
- Mathematical expression parsing
- Operator precedence handling

## Related Problems

- Basic Calculator (with parentheses)
- Basic Calculator III
- Expression Add Operators
- Evaluate Reverse Polish Notation

## Edge Cases

- Whitespace in expression
- Multi-digit numbers
- Negative results from division
- Single number (no operators)
- Consecutive operators (handled by design)

## Alternative Approaches

1. **Two-Pass Approach**: 
   - First pass: evaluate `*` and `/`
   - Second pass: evaluate `+` and `-`
   - More complex but clearer separation

2. **Shunting Yard Algorithm**: 
   - Convert to postfix notation
   - Evaluate postfix expression
   - More general but overkill for this problem

## Files

- `Stack.py`: Stack-based calculator with operator precedence

