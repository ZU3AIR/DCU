from Queue import Queue

def split(q):
    """ A split function which will split a queue into two.
        The function returns a tuple containing the two queues.
    """
    que1 = len(q)
    que2 = len(q)
    que3 = len(q)
    
    Q = Queue()
    Q2 = Queue()
    for i in range(len(q)):
        if i % 2:
            Q.enqueue(q.dequeue())
        else:
            Q2.enqueue(q.dequeue())
    return Q, Q2