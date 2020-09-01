class Solution:
    def intToRoman(self, num: int) -> str:
        mp = [[1000, "M"],[900, "CM"],[500, "D"],[400, "CD"],[100, "C"],[90, "XC"],[50, "L"],[40, "XL"],[10, "X"],[9, "IX"],[5, "V"],[4, "IV"],[1, "I"]]
        ans = ""
        i = 0
        while num != 0:
            if num % mp[i][0] != num:
                num -= mp[i][0]
                ans += mp[i][1]
            else:
                i += 1
        return ans
