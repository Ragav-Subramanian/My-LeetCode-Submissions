class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]:
            return []
        if len(matrix)==1:
            return matrix[0]
        final=[]
        top,bottom,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        while True:
            if left>right:
                break
            for i in range(left,right+1):
                final.append(matrix[top][i])
            top+=1 
            if bottom<top:
                break 
            for i in range(top,bottom+1):
                final.append(matrix[i][right])
            right-=1 
            if left>right:
                break 
            for i in range(right,left-1,-1):
                final.append(matrix[bottom][i])
            bottom-=1
            if top>bottom:
                break
            for i in range(bottom,top-1,-1):
                final.append(matrix[i][left])
            left+=1
        return final