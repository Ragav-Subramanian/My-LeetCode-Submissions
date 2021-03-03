class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0 
        m=max(nums)
        for i in range(m):
            if i not in nums:
                return i
        return m+1