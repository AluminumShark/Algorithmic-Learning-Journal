from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, prev: Optional["ListNode"] = None, next: Optional["ListNode"] = None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    """
    Doubly linked list with two sentinels:
      - self.head: dummy head (no real value)
      - self.tail: dummy tail (no real value)
    Real nodes live between head and tail. Sentinels simplify insert/delete at ends.
    self.size tracks the number of REAL nodes.
    """

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _node_at(self, index: int) -> Optional[ListNode]:
        """
        Internal helper: return the node AT position `index` (0-based) among REAL nodes.
        Assumes 0 <= index < self.size.
        Chooses direction (from head or tail) to minimize steps.
        """
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        """
        Return the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        return self._node_at(index).val

    def addAtHead(self, val: int) -> None:
        """
        Insert node with value `val` at the head (index 0).
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append node with value `val` at the tail (index == size).
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Insert node with value `val` BEFORE the index-th node.
        - If index == size: append to tail.
        - If index > size: do nothing.
        - If index < 0: treat as 0 (insert at head).
        Runs in O(min(index, size - index)).
        """
        if index > self.size:
            return
        if index < 0:
            index = 0

        # Find predecessor (pred) and successor (succ) around insertion point.
        if index == self.size:
            # Insert before tail sentinel
            pred, succ = self.tail.prev, self.tail
        else:
            succ = self._node_at(index)
            pred = succ.prev

        node = ListNode(val, pred, succ)
        pred.next = node
        succ.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node if index is valid.
        Runs in O(min(index, size - index)).
        """
        if index < 0 or index >= self.size:
            return

        node = self._node_at(index)
        pred, succ = node.prev, node.next
        pred.next = succ
        succ.prev = pred
        # (Optional in Python) del node
        self.size -= 1
