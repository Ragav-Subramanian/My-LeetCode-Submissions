class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        l=len(flowerbed)
        for i in range(l):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==l-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                c+=1
        return c>=n
