# Linked List Problems

This directory contains solutions and implementations for linked list-related algorithmic problems.

## Overview

Linked lists are fundamental data structures in computer science, consisting of nodes connected by pointers. This collection demonstrates various linked list operations, implementations, and problem-solving techniques.

## Problems

### [707. Design Linked List](707.%20Design%20Linked%20List/)
- Comprehensive linked list implementation
- Both singly and doubly linked list variants
- Complete CRUD operations (Create, Read, Update, Delete)
- Sentinel node patterns for edge case handling

## Data Structure Characteristics

### Singly Linked List
- Each node points to the next node
- One-way traversal
- Memory efficient (one pointer per node)
- Insertion/deletion: O(1) at known position, O(n) for search

### Doubly Linked List
- Each node points to both previous and next nodes
- Bidirectional traversal
- More memory overhead (two pointers per node)
- Can optimize access by choosing traversal direction
- Insertion/deletion: O(1) at known position, O(min(i, n-i)) for indexed access

## Common Patterns

### Sentinel/Dummy Nodes
- Dummy head node simplifies operations at the beginning
- Dummy tail node (for doubly linked lists) simplifies operations at the end
- Eliminates special cases for empty list or edge positions

### Two-Pointer Technique
- Fast and slow pointers for cycle detection
- Finding middle node
- Reversing linked list

### Pointer Manipulation
- Careful pointer updates to maintain list integrity
- Handling edge cases (empty list, single node, etc.)

## Key Operations Complexity

| Operation | Singly Linked List | Doubly Linked List |
|-----------|-------------------|-------------------|
| Access by index | O(n) | O(min(i, n-i)) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n) | O(1) |
| Insert at index | O(n) | O(min(i, n-i)) |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n) | O(1) |
| Delete at index | O(n) | O(min(i, n-i)) |
| Search | O(n) | O(n) |

## Learning Objectives

This collection demonstrates:
- Linked list data structure implementation
- Sentinel node patterns
- Pointer manipulation techniques
- Edge case handling
- Time/space complexity trade-offs
- Comparison between singly and doubly linked lists

## Topics Covered

- Basic linked list operations
- Sentinel node implementation
- Bidirectional traversal optimization
- Index-based operations
- Memory management considerations

