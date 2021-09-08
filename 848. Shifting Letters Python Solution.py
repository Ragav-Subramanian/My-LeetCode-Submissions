class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans=""
        sh=0
        for i in range(len(s)-1,-1,-1):
            sh+=shifts[i]
            sh%=26
            t=ord(s[i])+sh
            if t>=123:
                t=97+t%123
            ans+=chr(t)
        return ans[::-1]