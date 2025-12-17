from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Merge two sorted linked lists into a single sorted list.
    Uses a dummy head node for clean pointer handling.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify edge cases
        dummy = ListNode(-1)
        cur = dummy

        # Traverse both lists, linking the smaller node each time
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next  # Advance the merged list pointer

        # Append the remaining nodes (only one of them is non-empty)
        cur.next = list1 if list1 else list2

        # Return the merged sorted list (skip the dummy node)
        return dummy.next
