class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        while left<=right:
            mid=(left+right)//2
            try:
                if nums[mid]==target:
                    return mid 
                elif nums[mid]>target:
                     right=mid-1 
                else:
                    left=mid+1
            except:
                return -1
        return -1