class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0 for i in range(3)]
        cols = [0 for i in range(3)]
        d1 = 0
        d2 = 0
        for i in range(len(moves)):
            if i%2==0:
                r,c=moves[i]
                if r==c:
                    d1+=1
                if r+c==2:
                    d2+=1
                rows[r]+=1
                cols[c]+=1
                if d1==3 or d2==3 or rows[r]==3 or cols[c]==3:
                    return "A"
            else:
                r,c=moves[i]
                if r==c:
                    d1+=10
                if r+c==2:
                    d2+=10
                rows[r]+=10
                cols[c]+=10
                if d1==30 or d2==30 or rows[r]==30 or cols[c]==30:
                    return "B"
        return "Draw" if len(moves)==9 else "Pending"