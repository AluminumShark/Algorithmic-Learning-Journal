from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n)
# Space: O(1)
# Concept: Find Middle (Slow/Fast) -> Reverse Second Half -> Merge Two Halves.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find Middle
        S, F = head, head
        while F and F.next:
            S = S.next
            F = F.next.next
        
        # 2. Reverse Second Half
        prev, cur = None, S
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # 3. Merge two halves
        list1, list2 = head, prev
        while list2.next:
            tmp1 = list1.next
            tmp2 = list2.next

            list1.next = list2
            list2.next = tmp1

            list1 = tmp1
            list2 = tmp2

