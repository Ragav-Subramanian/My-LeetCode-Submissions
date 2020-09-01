
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize,int target,int* returnSize)
{
    int i,j;
    int* ret=(int*)malloc(sizeof(int)*4);
    for(i=0;i<numsSize;i++)
    {
        for(j=0;j<numsSize;j++)
        {
             if((nums[i]+nums[j])==target && i!=j)
            {
                ret[0]=i;
                ret[1]=j;
                *returnSize=2;
                return ret;
            }
        }
        
    }
    return 0;
}

