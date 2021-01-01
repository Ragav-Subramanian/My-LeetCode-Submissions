class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        l=len(arr)
        for val in pieces:
            v=None
            try:
                v=arr.index(val[0])+1
            except:
                return False
            for i in range(1,len(val)):
                if v>=l or val[i]!=arr[v]:
                    return False 
                v+=1
        return True