class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ''
        c=0
        for i in range(len(palindrome)//2):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'