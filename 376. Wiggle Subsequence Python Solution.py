class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @lru_cache(None)
        def recurse(ind,g):
            mc=0
            for i in range(ind+1,len(nums)):
                if (g and nums[i]>nums[ind]) or ((not g) and nums[i]<nums[ind]):
                    mc=max(mc,1+recurse(i,not g))
            return mc
        if len(nums)<2:
            return len(nums)
        return 1+max(recurse(0,True),recurse(0,False))