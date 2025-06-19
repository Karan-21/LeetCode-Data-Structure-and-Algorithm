class Solution:
    def partitionArray(self, v: List[int], k: int,idx=0 ,ans=0) -> int:
        v.sort()
        for i in range(len(v)):
            if v[i] - v[idx]>k:
                ans+=1
                idx=i
        return ans+1
        
