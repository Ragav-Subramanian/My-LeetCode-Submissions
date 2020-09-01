class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        T=nums1+nums2 
        T.sort()
        return T[len(T)//2] if len(T)%2 else (T[len(T)//2]+T[len(T)//2-1])/2