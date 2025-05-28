from collections import deque, defaultdict

class Solution:
    def bfs(self, adj, k, N, start):
        visited = [False] * N
        queue = deque([(start, 0)])
        visited[start] = True
        count = 0

        while queue:
            node, dist = queue.popleft()
            if dist > k:
                continue
            count += 1

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))

        return count

    def findCount(self, edges, k):
        N = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return [self.bfs(adj, k, N, i) for i in range(N)]

    def maxTargetNodes(self, edges1, edges2, k):
        ans1 = self.findCount(edges1, k)
        ans2 = self.findCount(edges2, k - 1)
        max2 = max(ans2)
        return [a + max2 for a in ans1]
