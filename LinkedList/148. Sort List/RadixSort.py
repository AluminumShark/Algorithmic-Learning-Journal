# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    """
    Radix Sort (base-10) on a singly linked list.
    Works only for non-negative integers.
    """

    def radixSort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1) Find the maximum value to determine number of digit passes
        max_val = 0
        cur = head
        while cur:
            max_val = max(max_val, cur.val)
            cur = cur.next

        # 2) Sort by each digit (least-significant digit first)
        exp = 1  # 10⁰, 10¹, 10², ...
        while max_val // exp > 0:
            # Create 10 buckets for digits 0-9
            buckets = [[] for _ in range(10)]

            # Distribute values into buckets according to current digit
            cur = head
            while cur:
                digit = (cur.val // exp) % 10
                buckets[digit].append(cur.val)
                cur = cur.next

            # Rebuild linked list from buckets
            dummy = ListNode(-1)
            tail = dummy
            for bucket in buckets:
                for num in bucket:
                    tail.next = ListNode(num)
                    tail = tail.next
            head = dummy.next

            # Move to the next digit place
            exp *= 10

        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.radixSort(head)
