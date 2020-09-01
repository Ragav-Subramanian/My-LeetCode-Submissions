class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)//2
        for i in set(nums):
            if nums.count(i)>l:
                return i