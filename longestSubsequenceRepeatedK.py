class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        candidates=[el for el,freq in Counter(s).items() if freq>=k]
        
        def helper(s1):
            i=total=0
            for el in s:
                if el==s1[i]:
                    i+=1
                    if i==len(s1):
                        i=0
                        total+=1
                        if total==k: return True
            return False
        
        res=''
        deque=collections.deque([''])
        while deque:
            cur=deque.popleft()
            for el in candidates:
                new=cur+el
                if helper(new):
                    if len(new)>len(res): res=new
                    elif len(new)==len(res): res=max(res,new)
                    deque.append(new)
        return res
