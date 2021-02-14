class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1 
        bfs=[(0,0,1)]
        grid[0][0]=1
        for i,j,d in bfs:
            if i==len(grid)-1 and j==len(grid)-1:
                return d 
            for a,b in [(i+1,j+1),(i-1,j-1),(i-1,j),(i,j-1),(i-1,j+1),(i+1,j-1),(i+1,j),(i,j+1)]:
                if 0<=a<len(grid) and 0<=b<len(grid) and grid[a][b]==0:
                    grid[a][b]=1
                    bfs.append((a,b,d+1))
        return -1