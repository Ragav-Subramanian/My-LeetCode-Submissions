class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k!=0 and len(nums)!=1:
            nums[:-k], nums[-k:] = nums[-k:], nums[:-k]