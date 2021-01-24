class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if mat==[]:
            return []
        r,c=len(mat),len(mat[0])
        for i in range(r):
            j=0
            t=[]
            ti=i
            while i<r and j<c:
                t.append(mat[i][j])
                i+=1
                j+=1  
            i=ti
            j=0
            t.sort(reverse=True)
            while i<r and j<c:
                mat[i][j]=t.pop()
                i+=1
                j+=1 
        for j in range(1,c):
            i=0
            t=[]
            ti=j
            while i<r and j<c:
                t.append(mat[i][j])
                i+=1
                j+=1  
            j=ti
            i=0
            t.sort(reverse=True)
            while i<r and j<c:
                mat[i][j]=t.pop()
                i+=1
                j+=1 
        return mat