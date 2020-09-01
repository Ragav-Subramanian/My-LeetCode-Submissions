class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        t,tot=0,0
        for i in s[::-1]:
            if d[i] >= t:
                tot += d[i]
            else:
                tot -= d[i]
            t = d[i]
        return tot