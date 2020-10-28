class Solution:
    def bagOfTokensScore(self, tokens: List[int], p: int) -> int:
        if not tokens or (p==0 and tokens[0]!=0):
            return 0
        tokens.sort()
        if tokens[0]>p:
            return 0
        i=0
        l=len(tokens)
        mc=0
        c=0
        while i<l:
            if tokens[i]<=p:
                c+=1 
                p-=tokens[i]
                i+=1 
            else:
                mc=max(mc,c)
                c-=1 
                l-=1
                p+=tokens[l]
        return max(mc,c)