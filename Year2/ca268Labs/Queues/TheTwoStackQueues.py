# Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue:
    def __init__(self):
        self.enqstack = Stack()
        self.deqstack = Stack()
        self.size = 0
        # Initialise the queue
        # YOUR CODE HERE

    def isempty(self):
        # YOUR CODE HERE
        return self.enqstack.isempty() and self.deqstack.isempty()

    def enqueue(self, object):
        # YOUR CODE HERE
        self.size += 1
        self.enqstack.push(object)

    def dequeue(self):
        # YOUR CODE HERE
        self.size = 1
        if not self.deqstack.isempty():
            return self.deqstack.pop()
        while not self.enqstack.isempty():
            self.deqstack.push(self.enqstack.pop())
        
        return self.deqstack.pop()