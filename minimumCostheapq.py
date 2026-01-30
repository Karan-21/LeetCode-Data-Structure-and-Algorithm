from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Construct a directed conversion graph using defaultdict
        graph = defaultdict(list)
        nodes = set(original + changed)
        for u, v, w in zip(original, changed, cost):
            graph[u].append((v, w))

        # Precompute Dijkstra's algorithm results for all nodes
        def dijkstra(s):
            dist = {node: float("inf") for node in nodes}
            dist[s] = 0
            queue = [(0, s)]
            while queue:
                d, node = heappop(queue)
                if d > dist[node]:
                    continue
                for v, w in graph[node]:
                    new_dist = d + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heappush(queue, (new_dist, v))
            return dist

        dist_map = {node: dijkstra(node) for node in nodes}

        # Main DP loop
        n = len(source)
        print(len(source), len(original))
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # this check is O(n*m)
        for i in range(1, n + 1):
            for node in nodes:
                length = len(node)
                l = max(0, i-length)

                src, des = source[l:i], target[l:i]

                if source[i-1] == target[i-1]:
                    dp[i] = min(dp[i], dp[i-1])
                if src in graph and des in nodes:
                    dp[i] = min(dp[i], dp[l] + dist_map[src].get(des, float("inf")))
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1
