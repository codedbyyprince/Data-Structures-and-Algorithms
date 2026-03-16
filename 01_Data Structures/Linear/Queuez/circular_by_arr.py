class MyQueue:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [None] * cap
        self.front = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            print("Queue is full")
            return
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1 
    
    def dequeue(self):
        if self.size == 0:
            print('Queue is empty ')
            return - 1
        res = self.arr[self.front]
        self.front = (self.front + 1 )% self.capacity
        self.size -= 1
        return res 

    def get_rear(self):
        if self.size == 0:
            print('Queue is empty')
            return -1 
        rear = (self.front + self.size -1 ) % self.capacity
        return self.arr[rear]
    
    def get_front(self):
        if self.size == 0:
            print('Queue is empty ')
            return -1
        return self.arr[self.front]

if __name__ == "__main__":
    q = MyQueue(5)
    
    q.enqueue(10)
    print("Front:", q.get_front(), "Rear:", q.get_rear())
    
    q.enqueue(20)
    print("Front:", q.get_front(), "Rear:", q.get_rear())
    
    q.enqueue(30)
    print("Front:", q.get_front(), "Rear:", q.get_rear())
    
    print("Dequeue:", q.dequeue())
    print("Front:", q.get_front(), "Rear:", q.get_rear())
    
    q.enqueue(40)
    print("Front:", q.get_front(), "Rear:", q.get_rear())
    
    print("Dequeue:", q.dequeue())
    print("Front:", q.get_front(), "Rear:", q.get_rear())
