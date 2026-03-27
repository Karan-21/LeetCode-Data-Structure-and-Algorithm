class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        col = len(mat[0])

        for i in range(len(mat)):

            for j in range(len(mat[0])):

                if mat[i][j] != mat[i][(j+k) % col]:

                    return False
        
        return True
