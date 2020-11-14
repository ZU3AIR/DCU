from stack_092 import Stack
import sys

l = "({["
r = ")}]"

def other_bracket(n):
    if n in l:
        return r[l.index(n)]
    return l[r.index(n)]

def matcher(line):
    stack = Stack()
    for x in line:
        if x in l:
            stack.push(x)
        elif x in r:
            if stack.is_empty():
                return False
            if stack.top() != other_bracket(x):
                return False

            stack.pop()
    return stack.is_empty()
