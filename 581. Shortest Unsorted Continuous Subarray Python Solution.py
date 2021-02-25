class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=len(nums)
        r=0
        temp=nums[:]
        nums.sort()
        for i in range(len(nums)):
            if temp[i]!=nums[i]:
                r=max(r,i)
                l=min(l,i)
        return 0 if r-l<0 else r-l+1