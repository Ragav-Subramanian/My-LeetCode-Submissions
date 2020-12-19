class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i]>=nums[j]:
                    continue
                for k in range(j+1,len(nums)):
                    if nums[j]<nums[k]:
                        return True
        return False