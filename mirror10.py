from itertools import islice, count

class Solution:
    def kMirror(self, k: int, N: int) -> int:
        return sum(islice((n for n in mirror10() if iskm(n, k)), N)) # islice(seq, n) is just like seq[:n], but works for Iterator

def mirror10(): # generator for base-10 mirror numbers
    yield from range(1, 10)
    for l in count(start=1): # i.e. range(1, inf)
        for n in range(10**(l - 1), 10**l): # e.g. n = 10 to 99 when l = 2
            yield int(str(n) + str(n)[::-1]) # e.g. 12 21
        for n in range(10**(l - 1), 10**l):
            yield from (int(str(n) + str(t) + str(n)[::-1]) for t in range(10))  # e.g. 12 0 21
                
def iskm(n, k): # True iff n is a k-mirror number
    digits = []
    while n > 0:
        n, r = divmod(n, k)
        digits.append(r)
    return digits == digits[::-1]
