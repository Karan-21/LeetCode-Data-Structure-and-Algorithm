class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        roots = [i for i in range(n)]
        
        # if roots[n] == 0 or find(n) == 0, means person n knows the secrete
        roots[firstPerson] = 0
        
        def find(x):
            if roots[x] == x:
                return x
            roots[x] = find(roots[x])
            return roots[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # x or y knows the secrete, make both as known secrete
                if rootX == 0 or rootY == 0:
                    roots[rootY] = roots[rootX] = 0
                # Neither x nor y  knows the secrete, just union them into the same group
                else:
                    roots[rootY] = rootX
        
        meetings.sort(key=lambda m:m[2])
        N = len(meetings)
        i = 0
        while i < N:
            # aggregate meetings at the same time
            sameTimeMeetings = [meetings[i]]
            while i < N-1 and meetings[i+1][2] == meetings[i][2]:
                i = i+1
                sameTimeMeetings.append(meetings[i])
                continue
            
            # union people in the same time meetings into groups
            for x,y,time in sameTimeMeetings:
                union(x, y)
                
            # reset the union groups that people do not know the secrete from meetings
            for x,y,time in sameTimeMeetings:
                rootX = find(x)
                # Since x and y are unioned into same group, if x does not know the secret, y does not know either
                if rootX != 0:
                    roots[x] = x
                    roots[y] = y
                            
            i+=1

        return [i for i in range(n) if find(i) == 0]
