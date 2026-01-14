# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# Solution: Min-Heap (Priority Queue)
# ============================================================
# Time: O(n log k) where n = total nodes, k = number of lists
# Space: O(k) for the heap
#
# Key Insight: Why store (val, index, node)?
# -------------------------------------------
# Python's heapq compares tuples element by element.
# If two nodes have the same value, it tries to compare the second element.
#
# Problem: ListNode objects are not comparable!
#   heapq.heappush(heap, (node.val, node))  # Error if values tie!
#
# Solution: Add a unique index as tie-breaker:
#   heapq.heappush(heap, (node.val, i, node))
#
# Now comparisons never reach the ListNode:
#   (5, 0, nodeA) vs (5, 1, nodeB) -> compares indices, not nodes
#
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Initialize heap with head of each list
        # Store (value, list_index, node) to avoid ListNode comparison
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = cur = ListNode(-1)

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            # If this list has more nodes, push the next one
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        cur.next = None  # Ensure the list is properly terminated
        return dummy.next

