class Solution:
    def reverse(self, x: int) -> int:
        n = False
        if x < 0:
            n = True
            x = x * -1
        s = str(x)[::-1]
        num = int(s)
        if n:
            num = num*-1
        if(abs(num) > (2 ** 31 - 1)):
            return 0
        return num