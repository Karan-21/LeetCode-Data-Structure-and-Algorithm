class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        queue = []

        res = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:

            node = queue.pop(0)

            res.append(node)

            for nei in adj[node]:

                indegree[nei] -= 1

                if indegree[nei] == 0:

                    queue.append(nei)
        
        return res if len(res) == numCourses else []
