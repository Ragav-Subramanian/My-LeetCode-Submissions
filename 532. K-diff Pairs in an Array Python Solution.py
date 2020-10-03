class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s=set()
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]>k:
                    break 
                if nums[j]-nums[i]==k:
                    s.add((nums[i],nums[j]))
        return len(s)