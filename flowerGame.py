class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if n%2==0:
            en=n//2
            on=n//2
        else:
            en=n//2
            on=(n//2)+1
        if m%2==0:
            em=m//2
            om=m//2
        else:
            em=m//2
            om=(m//2)+1  
        return en*om+em*on      

       
