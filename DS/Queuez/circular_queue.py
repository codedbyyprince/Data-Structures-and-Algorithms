class MyQueue:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [None] * cap
        self.front = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            print("Queue is full")
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1
        return self.arr 
    
    def dequeue(self, x):
        if self.size == 0:
            print('Queue is empty ')
            return - 1
        res = self.arr[self.front]
        self.front = (self.front + 1 )% self.capacity
        return res 