class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n=len(nums)
        sl=SortedList()
        next_idx=[i+1 for i in range(n)]
        prev_idx=[i-1 for i in range(n)]
        for i in range(n-1):
            sl.add((nums[i]+nums[i+1],i))
        cur_sm=0
        for i in range(n-1):
            cur_sm+=nums[i+1]<nums[i]
        ans=0
        while cur_sm>0:
            ans+=1
            val,idx=sl.pop(0)
            x,y=idx,next_idx[idx]
            x1=prev_idx[x]
            if x1>=0:
                rem_val=nums[x1]+nums[x]
                new=nums[x1]+val
                sl.remove((rem_val,x1))
                sl.add((new,x1))
                
                cur_sm-=nums[x]<nums[x1]
                cur_sm+=val<nums[x1]
            
            y1=next_idx[y]
            cur_sm-=nums[y]<nums[x]
            if y1<n:
                rem_val=nums[y]+nums[y1]
                new=val+nums[y1]
                sl.remove((rem_val,y))
                sl.add((new,x))
                
                cur_sm-=nums[y1]<nums[y]
                cur_sm+=nums[y1]<val
                
                prev_idx[y1]=x
            
            next_idx[x]=y1
            nums[x]=val
        return ans
