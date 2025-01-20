class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        nMap = defaultdict(list)

        indegree = [0] * numCourses

        for a, b in prerequisites:
            nMap[b].append(a)
            indegree[a] += 1
        
        queue = []
        res = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:

            node = queue.pop(0)

            res.append(node)

            for nei in nMap[node]:

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return True if len(res) == numCourses else False        
        
