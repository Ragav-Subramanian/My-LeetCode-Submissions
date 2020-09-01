class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        l=[[1],[1,1]]
        for i in range(2,numRows):
            t=[1]
            for j in range(1,len(l[-1])):
                t.append(l[-1][j-1]+l[-1][j])
            t.append(1)
            l.append(t)
        return l