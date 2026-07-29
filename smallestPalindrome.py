class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt       = {k: v//2  for k,v in sorted(Counter(s).items()) if v>1}
        lgs,n,chs = sum(math.lgamma(v+1) for v in cnt.values()), len(s), []
        for rest in range(n//2, 0, -1):
            for ch,f in iter((k,v) for k,v in cnt.items() if v):
                logperm = lgamma(rest) - (newlgs:= lgs -lgamma(f+1) +lgamma(f))
                if  k<=1 or math.log(k-1) +1e-7 < logperm:
                    chs.append(ch); cnt[ch] -=1; lgs = newlgs
                    break
                else:
                    k -= int(round(exp(logperm), 0))
        return  "" if len(chs) < n//2  else (
            (half:= ''.join(chs)) + (s[n//2] if n&1 else "") + half[::-1]
        )
        
