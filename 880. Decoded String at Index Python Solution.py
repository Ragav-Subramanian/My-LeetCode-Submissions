class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size=0
        for i in S:
            if i in "0123456789":
                size*=int(i)
            else:
                size+=1
        for i in S[::-1]:
            K%=size
            if K==0 and i.isalpha():
                return i
            if i in "0123456789":
                size//=int(i)
            else:
                size-=1