class Solution:
    def titleToNumber(self, s: str) -> int:
        c=0 
        d=dict(zip(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],range(1,27)))
        for i,key in enumerate(s):
            c*=26
            c+=d[key]
        return c