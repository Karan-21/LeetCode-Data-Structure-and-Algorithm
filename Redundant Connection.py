class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,a,b):
        p1, p2 = self.find(a), self.find(b)

        if p1 == p2:
            return False
        
        self.parent[p1] = p2

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        uf = UnionFind(n)

        for a, b in edges:
            if not uf.union(a,b):
                return [a,b]
