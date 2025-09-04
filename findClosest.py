class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        yt=abs(z-y) #check dist btw y and z
        xt=abs(z-x) #dist btw z and x
        if yt>xt: #if x is closer to z
            return 1
        elif yt<xt: #if y closer to z
            return 2
        else: #when both at equal dist
            return 0
        
        
