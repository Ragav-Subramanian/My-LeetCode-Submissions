
class Solution:
    def nextPermutation(self, number: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(number)==1:
            return
        i=len(number)-2 
        while i>=0 and number[i+1]<=number[i]:
            i-=1
        if i==-1:
            number.sort()
            return 
        j=len(number)-1
        while j>=0 and number[j]<=number[i]:
            j-=1
        number[i],number[j]=number[j],number[i]
        number[i+1:]=number[i+1:][::-1]