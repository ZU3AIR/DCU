class PQ(object):

    def __init__(self):
        self.d = {}
        self.n = 0

    def exch(self, j, k):
        self.d[j], self.d[k] = self.d[k], self.d[j]

    def insert(self, x):
        self.n += 1
        self.d[self.n] = x
        self.swim(self.n)

    def swim(self, k):
        while k > 1 and self.d[k // 2] < self.d[k]:
            self.exch(k, k // 2)
            k = k // 2

    def delMax(self):
        x = self.d[1]
        self.exch(1, self.n)
        del(self.d[self.n])
        self.n -= 1
        self.sink(1)
        return x

    def size(self):
        return len(self.d)

    def getMax(self):
        return int(self.d[1])

    def bigger(self, j, k):
        try:
            return max([j, k], key=self.d.__getitem__)
        except KeyError:
            return j

    def sink(self, k):
        while (2 * k <= self.n):
            j = 2 * k
            j = self.bigger(j, j + 1)
            if self.d[k] >= self.d[j]:
                break
            self.exch(k, j)
            k = j

    def is_empty(self):
        return len(self.d) == 0
