from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.len = 0
        self.storage = []
        self.queue = Queue()
        

    def append(self, value):
        class Item:
            def __init__(self,value):
                self.value = value

        item = Item(value)
        if self.len != self.capacity:
            self.storage.append(item)
            self.queue.enqueue(item)
            self.len += 1
        elif self.len == self.capacity:
            curitem = self.queue.dequeue()
            for i in self.storage:
                if i == curitem:
                    i.value = value
                    self.queue.enqueue(i)

    def get(self):
        values = [i.value for i in self.storage]
        return values 

RB = RingBuffer(3)
print(RB.get())
RB.append(2)
RB.append(4)
RB.append(6)
print(RB.get())
RB.append(8)
# RB.append(10)
# RB.append(12)
print(RB.get())
RB.append(10)
print(RB.get())

def add_50_elements_to_buffer(self):
        for i in range(50):
            self.append(i)

RB2 = RingBuffer(5)
add_50_elements_to_buffer(RB2)
print(RB2.get())
