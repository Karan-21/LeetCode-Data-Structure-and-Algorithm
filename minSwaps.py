class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def mv(x): #find the index of largest 1 entry in each row
            if sum(x):
                return max((i for i in range(len(x)) if x[i]==1))
            return 0
        line = [mv(e) for e in grid] #reduced to 1D array
            
        #return -1 if infeasible
        for i, e in enumerate(sorted(line)):
            if i < e:
                return -1

        #at this point we know it's feasible
        ret = 0
        i = 0
        while i < len(line):
            if line[i] > i: #this means the entry at i-th position is violating
                #now find the minimum possible value of j which would satisfy line[j] <= i
                #we can now swap this until the reach position i
                j = i+1
                while line[j] > i: 
                    j += 1
                ret += j-i #the number of swaps needed, minimal at this step
                line[i:j+1] = [line[j]] + line[i:j] #rearrange the array based on swap order
            i += 1    
        return ret #ret equals to minimum number of swaps
