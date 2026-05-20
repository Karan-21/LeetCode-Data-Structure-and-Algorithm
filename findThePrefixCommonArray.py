from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        da=defaultdict(int)
        db=defaultdict(int)
        c=[]
        cnt=0
        for i in range(n):
            if A[i]==B[i]:
                cnt+=1
            else:
                if A[i] in db:
                    cnt+=1
                if B[i] in da:
                    cnt+=1
                da[A[i]]+=1
                db[B[i]]+=1
            c.append(cnt)
        return c
