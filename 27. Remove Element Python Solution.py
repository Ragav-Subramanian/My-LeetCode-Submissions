class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        i=0
        for j in range(len(nums)):
            if val!=nums[j]:
                nums[i]=nums[j]
                i+=1
        return i