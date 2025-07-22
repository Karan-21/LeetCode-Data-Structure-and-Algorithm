class Solution:
    def maximumUniqueSubarray(self, arr: List[int]) -> int:
        
        # SLIDING WINDOW
        
        s=set()
        curr=0
        maxi=0
        i=0
        j=0
        
        while j<len(arr):
            if arr[j] in s:
                s.remove(arr[i])
                curr-=arr[i]
                i+=1
            
            else:
                s.add(arr[j])
                curr+=arr[j]
                maxi=max(maxi,curr)
                j+=1
            
        return maxi
