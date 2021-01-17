class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==1:
            return 5 
        if n==2:
            return 15
        c=0
        for i in combinations_with_replacement(['a','e','i','o','u'],n):
            c+=1 
        return c