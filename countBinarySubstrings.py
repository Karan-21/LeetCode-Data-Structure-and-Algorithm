class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Two Steps:
		
            Grouping array - Count consecutive 0 / 1 
                Ex. "0111001" into [1, 3, 2, 1]
				
            Then, Sum of minimum of adjacent elements in the grouping arrary.
				Ex. [1, 3, 2, 1]
					 \/  \/  \/
					 1 + 2 + 1  = 4
        """

        s += " "
        cnt = 1
        arr = []

        for i in range(len(s)-1):
            if s[i+1] == s[i]:
                cnt += 1
            else:
                arr.append(cnt)
                cnt = 1
                       
        
        result = 0

        if len(arr)==1:
            return result
        else:
            for i in range(len(arr)-1):
                result += min(arr[i], arr[i+1])
            return result
