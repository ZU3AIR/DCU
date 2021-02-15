from LinkedList import LinkedList

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()
        
    def push(self, item):
        # Your code here
        self.ll.add(item)
        return self
        
    def pop(self):
        # Your code here
        return self.ll.remove()
        
    def is_empty(self):
        # Your code here
        return self.ll.is_empty()