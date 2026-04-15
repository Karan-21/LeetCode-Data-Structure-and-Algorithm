class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        if target not in words:
            return -1
        i1=i2 = startIndex
        c1=0
        c2=0
        while words[i1]!=target:
            
            c1+=1
            i1+=1
            if i1==len(words):
                i1=0

        while words[i2]!=target:
            
            c2+=1
            i2-=1
            if i2==-1:
                i2=len(words)-1
        return min(c1,c2)
