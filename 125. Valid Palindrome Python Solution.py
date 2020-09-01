class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True
        v="!@#$%^&*(){}[];:.,/?></*-+~` _-="
        s=s.lower()
        for i in v:
            s=s.replace(i,"")
        s=s.replace("\"","").replace("\'","")
        print(s)
        return s==s[::-1]