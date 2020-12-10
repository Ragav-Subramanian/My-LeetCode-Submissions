class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l=len(A)
        i=0
        while i+1<l and A[i]<A[i+1]:
            i+=1 
        if i==0 or i==l-1:
            return False
        while i+1<l and A[i]>A[i+1]:
            i+=1
        return i==l-1