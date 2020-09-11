class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f,b,m,l=0,0,nums[0],len(nums)
        for i in range(l):
            f=f*nums[i] or nums[i]
            b=b*nums[l-i-1] or nums[l-i-1]
            m=max(m,f,b)
        return m