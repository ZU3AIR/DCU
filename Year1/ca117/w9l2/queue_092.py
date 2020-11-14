class Queue(object):

    def __init__(self):
        self.LIST = []

    def dequeue(self):
        return self.LIST.pop(0)

    def enqueue(self, x):
        self.LIST.append(x)

    def first(self):
        return self.LIST[0]

    def __len__(self):
        return len(self.LIST)

    def is_empty(self):
        return len(self.LIST) == 0
