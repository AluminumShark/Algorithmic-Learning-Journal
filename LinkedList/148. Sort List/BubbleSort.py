# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Bubble Sort on Linked List (Demonstration Only — TLE on LeetCode 148)
    """

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bubbleSort(head)

    def bubbleSort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node_i = head
        tail = None  # marks the sorted tail portion
        
        while node_i:
            node_j = head
            while node_j and node_j.next != tail:
                if node_j.val > node_j.next.val:
                    # Swap node values
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            tail = node_j
            node_i = node_i.next
        
        return head
