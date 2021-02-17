class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        left=0
        right=len(height)-1 
        while left<right:
            ma = max(ma,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left+=1 
            else:
                right-=1 
        return ma