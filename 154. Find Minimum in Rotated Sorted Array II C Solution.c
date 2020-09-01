
int findMin(int* nums, int numsSize){
 int start=0,end=numsSize-1;
         while(start<end){
             int mid=(start+end)/2; 
             if(nums[mid]<nums[end])
                 end=mid;                
             else if(nums[mid]>nums[end])
                 start=mid+1;         
             else
                 end--;                 
         }
         return nums[end];
}