class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=[]
        for i in set(nums):
            if nums.count(i)>len(nums)//3:
                a.append(i)
        return a