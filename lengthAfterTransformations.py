class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = collections.deque([0]*26)
        a = ord('a')
        for i in s:
            q[ord(i)-a] +=1

        for i in range(t):
            z = q.pop()
            q.appendleft(z)
            q[1]+=z

        return sum(q)%(10**9 + 7)
