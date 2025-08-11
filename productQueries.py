class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        powers_mul = [1]
        
        # [1] minimum number of powers implies that all of them are unique,
        #     thus, the powers are encoded by the corresponding bits in the
        #     binary decomposition of 'n';
        #     here, we precompute all consecutive products
        for i in range(30): 
            if n & 1<<i:                
                powers_mul.append((1<<i) * powers_mul[-1])
        
        answers = []
        
        # [2] once we precomputed all consecutive products, querying
        #     is trivial, i.e., just divide the marginal products 
        for left, right in queries:
            answers.append((powers_mul[right+1] // powers_mul[left]) % 1_000_000_007)
            
        return answers
