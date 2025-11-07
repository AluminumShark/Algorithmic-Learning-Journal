class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    """
    Finds the middle node of a singly linked list.
    If there are two middle nodes, return the second one.
    (Two-pass version: count first, then traverse again)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1) First pass: count total nodes
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        # 2) Second pass: move to the middle (count // 2 steps)
        cur = head
        for _ in range(count // 2):
            cur = cur.next

        # Return the middle node
        return cur
