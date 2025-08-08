class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dfs(a,b):
            if a<=0 and b <=0:
                return 0.5
            elif a<=0:
                return 1
            elif b<=0:
                return 0
            else:
                return 0.25 * (dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75))
        return 1 if n > 4450 else dfs(n,n)   # How to know 4450 ? ⇣⇣⇣

        # print(dfs(1000,1000))            # 0.9765650521094358
        # print(dfs(10000,10000))          # 0.9999999999159161
        # for i in range(1000,10000):
        #     if 1-dfs(i,i) <= 10**(-5):
        #         print(i)                 # 4451
        #         break   
