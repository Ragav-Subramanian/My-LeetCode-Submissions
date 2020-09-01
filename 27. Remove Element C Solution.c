int removeElement(int* nums, int numsSize, int val){
int i,j;
    for(i=0;i<numsSize;i++)
{
    if(nums[i]==val)
    {
        j=i;
        while(i<numsSize-1)
        {
            nums[i]=nums[i+1];
            i++;
        }
        numsSize--;
        i=j-1;
        
    }
}
    return numsSize;
}

