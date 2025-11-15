class Solution:
    def numberOfSubstrings(self, S: str) -> int:
        N = len(S)
        MAGIC = int(N**0.5) + 1
        zeros = deque(i for i, c in enumerate(S) if c=='0')
        zeros.append(N)
        ans = 0

        for i in range(N):
            while zeros and zeros[0] < i:
                zeros.popleft()
            
            prev = i
            for num_zeros, cur in enumerate(zeros):
                if num_zeros >= MAGIC: break

                # dealing with substring left=i, right in [prev, cur)
                min_length = max(prev - i + 1, num_zeros * num_zeros + num_zeros)
                max_length = cur - i
                ans += max(max_length - min_length + 1, 0)

                prev = cur
        
        return ans
