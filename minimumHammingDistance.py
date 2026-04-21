class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        par = []
        rank = [1] * len(source)

        for i in range(len(source)):
            par.append(i)

        # print(rank)

        def union(nd1, nd2):

            # if nd1 == nd2:
            #     return
            
            n1 = find(nd1)
            n2 = find(nd2)

            if n1 == n2: return

            if rank[n1] > rank[n2]:
                rank[n1] += rank[n2]
                rank[n2] = 0
                par[n2] = n1
            else:
                rank[n2] += rank[n1]
                rank[n1] = 0
                par[n1] = n2

            return


        def find(n):

            while n != par[n]:
                
                n = par[n]
            
            return n

        hs = {}
        ind = set()
        for i, j in allowedSwaps:
            ind.add(i)
            ind.add(j)
            union(i, j)
        

        # print(par, rank)

        for i in range(len(par)):
            par[i] = find(par[i])
        
        # print(par, rank)

        for i in range(len(par)):
            tmp = par[i]
            if tmp in hs:
                if source[i] in hs[tmp]:
                    hs[tmp][source[i]] += 1
                else:
                    hs[tmp][source[i]] = 1
            else:
                hs[tmp] = {}
                hs[tmp][source[i]] = 1

        # print(hs)

        cnt = 0
        # for i in range(len(source)):
        #     if source[i] != target[i]:
        #         cnt += 1
    
        for i in range(len(source)):
            gr = find(i)
            if target[i] in hs[gr]:
                hs[gr][target[i]] -= 1
                # print(hs[gr])
                if hs[gr][target[i]] == 0:
                    del hs[gr][target[i]]
                # print(hs[gr])
                # if source[i] != target[i]:
                #     print("1")
                cnt += 1
        
        # for h in hs:

        
        return (len(source) - cnt)
