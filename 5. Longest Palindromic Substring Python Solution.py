class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        if len(s)==1:
            return s
        if len(s)==2:
            return s[0]
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-i+1):
                #print(s[j:j+i])
                if s[j:j+i]==s[j:j+i][::-1]:
                    return s[j:j+i]