class MyCircularDeque:

    def __init__(self, k: int):
        # Initialize a fixed-size circular buffer
        self.capacity = k                 # Maximum number of elements
        self.queue = [0] * k              # Underlying array
        self.front = 0                    # Points to the front element
        self.rear = 0                     # Points to the next insertion position at the rear
        self.size = 0                     # Current number of elements

    def insertFront(self, value: int) -> bool:
        # If full, cannot insert
        if self.isFull():
            return False

        # Move front backward circularly and insert the value
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        # If full, cannot insert
        if self.isFull():
            return False

        # Insert at rear and move rear forward circularly
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        # If empty, cannot delete
        if self.isEmpty():
            return False

        # Move front forward circularly
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        # If empty, cannot delete
        if self.isEmpty():
            return False

        # Move rear backward circularly
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        # Return the front element, or -1 if empty
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        # Return the last element, or -1 if empty
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        # Empty when size == 0
        return self.size == 0

    def isFull(self) -> bool:
        # Full when size == capacity
        return self.size == self.capacity
