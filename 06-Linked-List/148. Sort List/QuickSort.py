from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Quick Sort on Singly Linked List (Demonstration Only — TLE on LeetCode 148)
    """

    def partition(self, left, right):
        """
        Partition the sublist [left, right) using left as pivot.
        Rearrange nodes by swapping their values (not node references).
        Returns the final pivot node position.
        """
        # Base case: single node or empty
        if left == right or left.next == right:
            return left

        pivot = left.val
        node_i, node_j = left, left.next

        while node_j != right:
            if node_j.val < pivot:
                node_i = node_i.next
                node_i.val, node_j.val = node_j.val, node_i.val
            node_j = node_j.next

        # Move pivot to its correct position
        node_i.val, left.val = left.val, node_i.val
        return node_i

    def quickSort(self, left, right):
        """
        Recursively apply Quick Sort to [left, right)
        """
        if left == right or left.next == right:
            return left

        pivot = self.partition(left, right)
        self.quickSort(left, pivot)
        self.quickSort(pivot.next, right)
        return left

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.quickSort(head, None)
