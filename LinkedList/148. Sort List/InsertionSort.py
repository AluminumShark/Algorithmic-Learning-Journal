from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Insertion Sort on Linked List (Demonstration Only — TLE on LeetCode 148)
    """

    def insertionSort(self, head):
        if not head or not head.next:
            return head

        # Dummy head simplifies insertion logic
        dummyHead = ListNode(-1)
        dummyHead.next = head

        # Tail of the sorted portion
        sortedTail = head
        curr = head.next

        while curr:
            if sortedTail.val <= curr.val:
                # Current node is already in correct position
                sortedTail = sortedTail.next
            else:
                # Find the correct position to insert `curr` in sorted part
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next

                # Remove curr from its current position
                sortedTail.next = curr.next

                # Insert curr after prev
                curr.next = prev.next
                prev.next = curr

            # Move to next unsorted node
            curr = sortedTail.next

        return dummyHead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSort(head)
