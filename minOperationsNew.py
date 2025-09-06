class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        breakpoints = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]
        psums = [0, 3, 27, 171, 939, 4779, 23211, 109227, 502443, 2271915, 10136235, 44739243, 195734187, 850045611, 3668617899]
        
        def get_subtotal(v):
            index = bisect_right(breakpoints, v)
            return psums[index-1] + index * (v-breakpoints[index-1])

        return sum((get_subtotal(r+1) - get_subtotal(l) + 1) // 2 for l, r in queries)
