class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(i-j)<=k and abs(nums[i]-nums[j])<=t:
                    return True
        return False