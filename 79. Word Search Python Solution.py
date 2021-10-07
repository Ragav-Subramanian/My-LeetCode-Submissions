class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def search(i,j,ind,wl):
            if ind==wl:
                return True
            if i<0 or i>=m or j<0 or j>=n:
                return False 
            if word[ind]==board[i][j]:
                temp=board[i][j]
                board[i][j]='0'
                ans = (search(i,j+1,ind+1,wl) or search(i+1,j,ind+1,wl) or search(i,j-1,ind+1,wl) or search(i-1,j,ind+1,wl))
                board[i][j]=temp
                return ans
            else:
                return False
        l=len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if search(i,j,0,l):
                        return True
        return False