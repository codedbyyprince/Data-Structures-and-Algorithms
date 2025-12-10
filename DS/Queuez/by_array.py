class Queuez:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            print('OVVERFLOW CONDITION ')
            return
        self.arr[self.size] = x
        self.size += 1