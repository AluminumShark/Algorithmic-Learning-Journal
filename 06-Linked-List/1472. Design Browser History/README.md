# LeetCode 1472: Design Browser History

## Overview

Design a browser history system using a doubly linked list to support forward and backward navigation.

## Problem Description

You have a browser of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:
- `BrowserHistory(homepage)`: Initializes the object with the homepage of the browser
- `visit(url)`: Visits `url` from the current page. It clears up all the forward history
- `back(steps)`: Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history at most `steps`
- `forward(steps)`: Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history at most `steps`

**Example:**
```
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");
browserHistory.visit("facebook.com");
browserHistory.visit("youtube.com");
browserHistory.back(1);      // return "facebook.com"
browserHistory.back(1);      // return "google.com"
browserHistory.forward(1);   // return "facebook.com"
browserHistory.visit("linkedin.com");
browserHistory.forward(2);   // return "linkedin.com" (no forward history)
browserHistory.back(2);      // return "google.com"
browserHistory.back(7);      // return "leetcode.com"
```

## Algorithm

**Doubly Linked List**: Use a doubly linked list where each node represents a page, with `prev` and `next` pointers for navigation.

**Key Design:**
- Each node stores a URL and links to previous/next pages
- `curr` pointer tracks current page
- `visit()` clears forward history by setting `curr.next = None`
- `back()` and `forward()` move `curr` pointer along the list

**Key Steps:**

1. **Visit**:
   - Clear forward history: `curr.next = None`
   - Create new node with URL
   - Link new node to current: `newPage.prev = curr`, `curr.next = newPage`
   - Move `curr` to new page

2. **Back**:
   - Move `curr` backward up to `steps` times
   - Stop if `curr.prev` is None
   - Return current URL

3. **Forward**:
   - Move `curr` forward up to `steps` times
   - Stop if `curr.next` is None
   - Return current URL

## Complexity Analysis

- **Time Complexity:**
  - `visit()`: O(1)
  - `back(steps)`: O(steps) - but bounded by history length
  - `forward(steps)`: O(steps) - but bounded by forward history length
- **Space Complexity:** O(n) - where n is the number of visited pages

## Key Insight

Doubly linked list is ideal for bidirectional navigation:
- `prev` pointer enables backward movement
- `next` pointer enables forward movement
- Natural representation of browser history

## Implementation Details

### Node Structure
- `val`: URL string
- `prev`: Link to previous page
- `next`: Link to next page

### Forward History Clearing
- When visiting new page, `curr.next = None` clears forward history
- Mimics real browser behavior

### Boundary Handling
- `back()` stops when `curr.prev` is None (at homepage)
- `forward()` stops when `curr.next` is None (no forward history)

## Pattern Recognition

This problem demonstrates:
- Doubly linked list for bidirectional traversal
- State management with current pointer
- History/undo-redo pattern
- Browser-like navigation system

## Use Cases

- Browser history implementation
- Undo-redo functionality
- Navigation systems
- State management with history

## Related Problems

- Design Linked List
- LRU Cache (similar history management)
- Design Snake Game

## Edge Cases

- Visiting page when at end of history
- Back/forward beyond available history
- Multiple visits clearing forward history
- Single page (homepage only)

## Alternative Approaches

1. **Two Stacks**: O(steps) for back/forward
   - Back stack and forward stack
   - More complex but similar performance

2. **Array with Index**: O(1) access but O(n) for visit
   - Array stores URLs
   - Index tracks current position
   - Visit requires array manipulation

## Files

- `DoublyLinkedList.py`: Doubly linked list implementation

