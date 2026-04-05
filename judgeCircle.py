class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c=0
        for i in moves:
            if i =='U':
                c+=1
            elif i=='D':
                c-=1
            elif i == 'L':
                c+=20
            else:
                c-=20
        if c==0:
            return True
        return False
        
