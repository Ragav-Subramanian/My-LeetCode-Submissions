class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        twosums={}
        ans=0
        for i in range(len(arr)):
            ans+=twosums.get(target-arr[i],0)
            for j in range(i):
                twosums[arr[i]+arr[j]]=twosums.get(arr[i]+arr[j],0)+1
        return ans%(10**9+7)