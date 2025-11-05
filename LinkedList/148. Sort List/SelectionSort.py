from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Selection Sort on Linked List (Demonstration Only — TLE on LeetCode 148)
    """

    def selectionSort(self, head):
        """
        Traverse the linked list and repeatedly select the smallest node
        from the unsorted part, then place it at the current position.
        """
        node_i = head

        while node_i and node_i.next:
            # Assume current node is minimum
            minNode = node_i
            node_j = node_i.next

            # Find the node with the smallest value in the remaining list
            while node_j:
                if node_j.val < minNode.val:
                    minNode = node_j
                node_j = node_j.next

            # Swap values (not nodes) if a smaller one was found
            if minNode != node_i:
                node_i.val, minNode.val = minNode.val, node_i.val
            
            node_i = node_i.next

        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.selectionSort(head)
