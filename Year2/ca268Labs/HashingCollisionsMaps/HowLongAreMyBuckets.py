# Add a method called length() to the LinkedList class which returns
# the number of elements in the list. It should leave the list
# unchanged.The LinkedList class is shown below:

#
#  Just a class to store the item and the next pointer
#
class Node:
    def init(self, item, next):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def add(self, item):
        self.head = Node(item, self.head)
        self.count = self.count +1
    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            self.count = self.count -1
            return item

    def is_empty(self):
        return self.head == None
    def length(self):
        return self.count

#Your function will be tested by the following program:

import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()

    ll = LinkedList()
    # call the students function
    print(ll.length())   # Empty list, length should return 0

    for item in items:
        ll.add(item)

    # call the students function
    print(ll.length())

    # check that the first item removed from the list is the same as the last one added
    same = ll.remove() == items.pop()

    # call the students function again ... should be one shorter.
    print(ll.length())

    while not ll.is_empty() and len(items) > 0:
        same = same and ll.remove() == items.pop()

    if not same or not ll.is_empty() or len(items) != 0:
        print("the list has been modified!");

if name == "main":
    main()