class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a=0
        b=0
        for i,j in zip(secret,guess):
            if i==j:
                a+=1 
                secret=secret.replace(i,'*',1)
                guess=guess.replace(i,')',1)
        for j in guess:    
            if j in secret:
                b+=1 
                secret=secret.replace(j,'*',1)
        return str(a)+"A"+str(b)+"B"