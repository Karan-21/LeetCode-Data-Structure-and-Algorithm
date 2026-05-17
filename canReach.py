class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        q=deque([start])
        visited=set()
        n=len(nums)-1
        while q:
            node=q.popleft()
            if nums[node]==0:
                return True
            if node in visited:
                continue
            moves=[node+nums[node],node-nums[node]]
            visited.add(node)
            for i in moves:
                if 0<=i<=n:
                    q.append(i)
        return False
