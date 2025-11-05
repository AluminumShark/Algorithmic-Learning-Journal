from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    """
    Sort a singly linked list in O(n log n) time using Merge Sort.
    Rationale:
      - Linked lists have O(1) insertion/merge at head, but no random access,
        so merge sort is preferred over quicksort/heap sort for lists.
    """

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return the head of the merged list.
        Uses a dummy head to simplify pointer manipulation.
        """
        dummyHead = ListNode(-1)
        curr = dummyHead

        # Merge while both lists have nodes
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        # Append the remaining nodes (only one of left/right is non-empty)
        curr.next = left if left else right
        return dummyHead.next

    def mergeSort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Top-down merge sort on linked list:
          1) Split the list into two halves via slow/fast pointers.
          2) Recursively sort each half.
          3) Merge the two sorted halves.
        """
        # Base case: empty list or single node is already sorted
        if not head or not head.next:
            return head

        # Find the middle: slow stops at end of left half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into [head .. slow] and [slow.next .. end]
        rightHead = slow.next
        slow.next = None

        # Sort both halves
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(rightHead)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
