class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Function to find all prime factors of a number
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        gr = {}  # Map: prime factor → list of indices whose values are divisible by it
        for i in range(n):
            fac = prime_factors(arr[i])
            for ele in fac:
                if ele in gr:
                    gr[ele].append(i)     
                else:
                    gr[ele] = [i]         

        h = [[0, -0]]  # Min-heap with [distance, negative index] (negative for getting greater index)
        dis = [inf] * n
        dis[0] = 0        

        while h:
            val, node = heapq.heappop(h)  
            if node == -(n - 1):          
                return val
            node = -node             

            # Adjacent left move
            if node - 1 >= 0 and dis[node - 1] > val + 1:
                dis[node - 1] = val + 1
                heapq.heappush(h, [val + 1, -(node - 1)])

            # Adjacent right move
            if node + 1 < n and dis[node + 1] > val + 1:
                dis[node + 1] = val + 1
                heapq.heappush(h, [val + 1, -(node + 1)])

            # Prime teleportation move using prime factors of arr[node]
            if arr[node] in gr:
                for nei in gr[arr[node]]:
                    if dis[nei] > val + 1:
                        dis[nei] = val + 1
                        heapq.heappush(h, [val + 1, -nei])
