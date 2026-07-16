class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        test=sorted(set(nums))
        nums=list(test)
        ans=0
        res=[]
        if nums:

            for i in range(len(nums)-1):
                if nums[i+1]-nums[i]==1:
                    ans+=1
                else:
                    res.append(ans+1)
                    ans=0
            res.append(ans+1)
            return max(res)
        else:
            return 0