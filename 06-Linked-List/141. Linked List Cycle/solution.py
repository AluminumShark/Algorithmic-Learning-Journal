from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n)
# Space: O(1)
# Concept: Floyd's Tortoise and Hare (Slow/Fast Pointers).
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        S, F = head, head
        while F and F.next:
            S = S.next
            F = F.next.next
            if S == F:
                return True
        return False

