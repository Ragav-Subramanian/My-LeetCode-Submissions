class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        v = dividend/divisor 
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        if v<0:
            return int(str(v).split(".")[0])
        else:
            return int(v)