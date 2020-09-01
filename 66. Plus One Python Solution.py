class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num="".join(list(map(str,digits)))
        return list(map(int,list(str(int(num)+1))))