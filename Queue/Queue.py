"""
This is the ADT for Queue data structure that can be used
Assumption : Rear end of the queue is at index 0 and front is at the end of the list
"""


class QueueADT:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek_front(self):
        return self.items[-1]

    def peek_rear(self):
        return self.items[0]
# Verification
#q = QueueADT()
#q.enqueue(4)
#q.enqueue('dog')
#q.enqueue(True)
#print(q.size())
