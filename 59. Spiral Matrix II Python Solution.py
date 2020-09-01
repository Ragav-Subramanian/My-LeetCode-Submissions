class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        final=[[0]*n for i in range(n)]
        v=1
        top,bottom,left,right=0,n-1,0,n-1
        while True:
            if left>right:
                break
            for i in range(left,right+1):
                final[top][i]=v
                v+=1
            top+=1 
            if bottom<top:
                break 
            for i in range(top,bottom+1):
                final[i][right]=v
                v+=1
            right-=1 
            if left>right:
                break 
            for i in range(right,left-1,-1):
                final[bottom][i]=v
                v+=1
            bottom-=1
            if top>bottom:
                break
            for i in range(bottom,top-1,-1):
                final[i][left]=v
                v+=1
            left+=1
        return final