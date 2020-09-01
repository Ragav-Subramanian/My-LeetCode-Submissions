int findMin(int* nums, int numsSize){
    if(numsSize==1)
        return nums[0];
int left=0,right=numsSize-1,mid;
    if(nums[left]<nums[right])
        return nums[left];
    while(left<=right)
    {
        mid=(left+right)/2;
        if(nums[mid]>nums[mid+1])
        {
            return nums[mid+1];
        }
        else if(nums[left]<=nums[mid])
        {
            left=mid+1;
        }
        else
        {
            right=mid-1;
        }
    }
    return 0;
}class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)