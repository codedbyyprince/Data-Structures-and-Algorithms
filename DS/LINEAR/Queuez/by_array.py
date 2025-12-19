class Queuez:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            print('OVERFLOW CONDITION ')
            return
        self.arr[self.size] = x
        self.size += 1
        print(self.arr)
        return 

    def dequeue(self):
        if self.size == 0:
            print('UNDERFLOW CONDITION')

        for i in range(1 , self.size):
            self.arr[i-1] = self.arr[i]
        self.size -= 1
        print(self.arr)
        return

    def get_front(self):
        if self.size == 0:
            print('QUEUE IS EMPTY ')
            return -1 
        return self.arr[0]
            
    def get_rear(self):
        if self.size == 0:
            print('QUEUE IS READY')
            return
        print(self.arr[self.size - 1])
        return 
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

q = Queuez(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.dequeue()
q.enqueue(60)
print(q.get_front())