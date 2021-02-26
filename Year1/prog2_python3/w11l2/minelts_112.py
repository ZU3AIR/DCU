
import sys
from priority_queue_112 import PQ

def main():
    p = PQ()
    for l in sys.stdin:
        p.insert(int(l.strip()))

    while p.size() != int(sys.argv[1]):
        p.delMax()

    while p.size() != 0:
        print(p.delMax())

if __name__ == '__main__':
    main()
