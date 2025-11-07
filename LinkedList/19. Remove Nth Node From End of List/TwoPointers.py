from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    """
    Removes the Nth node from the end of a singly linked list in one pass.
    Uses the two-pointer (fast & slow) technique.
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node before the head to handle edge cases (like deleting head)
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # Move 'fast' pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until 'fast' reaches the end
        # When 'fast' is None, 'slow' is right before the target node
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the Nth node from the end
        slow.next = slow.next.next

        # Return the new head (dummy.next handles the case where head was deleted)
        return dummy.next
