from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n)
# Space: O(1)
# Concept: Two Pointers with a Gap. Move Fast pointer n steps ahead, then move both until Fast reaches end.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        S, F = dummy, dummy

        # Move Fast pointer n steps ahead
        for _ in range(n):
            F = F.next

        # Move both until Fast reaches the end
        while F.next:
            S = S.next
            F = F.next

        # Remove the nth node
        S.next = S.next.next

        return dummy.next

