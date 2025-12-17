class MyCircularQueue:

    def __init__(self, k: int):
        # To distinguish between full and empty states,
        # allocate one extra space (k + 1) in the queue.
        self.capacity = k + 1
        self.queue = [0 for _ in range(k + 1)]
        self.front = 0        # Points to the position before the first element
        self.rear = 0         # Points to the last element

    def enQueue(self, value: int) -> bool:
        # If the queue is full, cannot enqueue
        if self.isFull():
            return False

        # Move rear forward circularly and insert value
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        # If the queue is empty, cannot dequeue
        if self.isEmpty():
            return False
        
        # Move front forward circularly
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        # Return the front element, or -1 if empty
        if self.isEmpty():
            return -1
        return self.queue[(self.front + 1) % self.capacity]

    def Rear(self) -> int:
        # Return the rear element, or -1 if empty
        if self.isEmpty():
            return -1
        return self.queue[self.rear % self.capacity]

    def isEmpty(self) -> bool:
        # Queue is empty when front and rear coincide
        return self.rear == self.front

    def isFull(self) -> bool:
        # Queue is full when next position of rear meets front
        return (self.rear + 1) % self.capacity == self.front
