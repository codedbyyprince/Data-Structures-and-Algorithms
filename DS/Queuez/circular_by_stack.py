# approach enqueue costly
class queue_by_stack_en_costly:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            return 
        self.s1.pop()
    
    def front(self):
        if not self.s1:
            return 
        return self.s1[-1]


# approach dequeue costly
class queue_by_stack_de_costly:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeu(self):
        if not self.s1 and not self.s2:
            return 
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        self.s2.pop()

    def get_front(self):
        if self.s2:
            return self.s2[-1]
        elif self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        return -1 