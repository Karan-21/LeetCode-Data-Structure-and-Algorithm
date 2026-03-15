class Fancy:

    def __init__(self):
        self.arr = []
        self.pre = [[1, 0]]

    def append(self, val: int) -> None:
        self.arr.append(val)
        self.pre.append(list(self.pre[-1]))
    def addAll(self, inc: int) -> None:
        self.pre[-1][1] += inc

    def multAll(self, m: int) -> None:
        self.pre[-1][0] *= m
        self.pre[-1][1] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
			
        c, d = self.pre[-1]
        a, b= self.pre[idx]
        # e*(a*x+b) + f = c*x + d
		# e*a = c
		# e*b + f = d
        e = c//a
        f = d-e*b

        return (e*self.arr[idx] + f) % (10**9+7)
