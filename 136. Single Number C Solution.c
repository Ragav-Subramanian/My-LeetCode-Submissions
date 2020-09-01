int singleNumber(int* nums, int numsSize){
int i,j;
    for(i=0;i<numsSize;i++)
    {int c=0;
        for(j=0;j<numsSize;j++)
        {
            if(i==j)
            {
                continue;
            }
            else if(nums[i]==nums[j])
            {
                c++;
            }
        }
     if(c==0)
     {
         return nums[i];
     }
    }
    return 0;
}

