from typing import Optional

class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class MyLinkedList:
    """
    Singly linked list with a dummy head node.
    - `self.head` is a dummy (sentinel) node that simplifies edge cases
      (insert/delete at index 0) by ensuring there is always a node
      before the real first element.
    - `self.size` tracks the number of real elements in the list.
    """

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # dummy head, real data starts at head.next

    def get(self, index: int) -> int:
        """
        Return the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        # Move (index + 1) steps from dummy to land on the real node.
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Insert a node of value val before the first element of the list.
        After the insertion, the new node will be the first node of the list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the list.
        (Runs in O(n) here because we traverse to the end.)
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Insert a node of value val before the index-th node in the list.
        If index equals the length of the list, the node will be appended to the end.
        If index is greater than the length, the node will not be inserted.
        If index is negative, the node will be inserted at the head.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0

        # Find predecessor of the position to insert
        prev = self.head
        for _ in range(index):
            prev = prev.next

        node = ListNode(val)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        # Find predecessor of the node to delete
        prev = self.head
        for _ in range(index):
            prev = prev.next

        to_delete = prev.next
        prev.next = to_delete.next
        # (Optional in Python) del to_delete
        self.size -= 1
