class Solution:
    def reorderSpaces(self, text: str) -> str:
        n=text.split()
        c=0
        for i in text:
            if i==" ":
                c+=1 
        if c==0:
            return text
        if len(n)==1:
            return n[0]+" "*c
        ans=(" "*(c//(len(n)-1))).join(n)
        ans+=(" "*(c%(len(n)-1)))
        return ans