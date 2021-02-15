from Stack import Stack
import sys

def reverse_input(stack):
        for word in sys.stdin:
            stack.push(word.strip())
        while not stack.is_empty():
            print(stack.pop())
