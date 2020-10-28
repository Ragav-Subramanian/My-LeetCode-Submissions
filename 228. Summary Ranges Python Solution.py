class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[]:
            return nums
        ans=[]
        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]+1!=nums[i]:
                if s==nums[i-1]:
                    ans.append(str(s))
                else:
                    ans.append(str(s)+"->"+str(nums[i-1]))
                s=nums[i]
        if s==nums[-1]:
            ans.append(str(s))
        else:
            ans.append(str(s)+"->"+str(nums[-1]))
        return ans