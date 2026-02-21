class Solution:
    def countPrimeSetBits(self, L, R):
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        
        ret = 0
        for i in range(L, R+1):
            one_count = bin(i).count('1')
            if one_count in prime_set:
                ret +=1
        
        return ret
