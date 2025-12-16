class MyQueue:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [None] * cap
        self.front = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            return "Queue is full"
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1
        return self.arr 