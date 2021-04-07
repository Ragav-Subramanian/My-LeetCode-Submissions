class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a,b=0,0
        for i in s[:len(s)//2]:
            if i in "AEIOUaeiou":
                a+=1
        for i in s[len(s)//2:]:
            if i in "AEIOUaeiou":
                b+=1
        return a==b