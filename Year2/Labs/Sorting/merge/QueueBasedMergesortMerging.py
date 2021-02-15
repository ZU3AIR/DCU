from Queue import Queue

def merge(q1, q2, q):
    """ this function will merge q1 and q2 into q.
        Assuming that q1 and q2 are sorted, this function will
        return q such that q contains the combined elements of q1 and q2 and
        q will also be sorted.
        
        The function returns nothing. The result will be contained in the queue parameter.
    """

    while not q1.isempty() and not q2.isempty():
        if q1.first() < q2.first():
            q.enqueue(q1.dequeue())
        else:
            q.enqueue(q2.dequeue())
    while not q1.isempty():
        q.enqueue(q1.dequeue())
    while not q2.isempty():
        q.enqueue(q2.dequeue())