class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(set(nums))==1 and list(set(nums))[0]==0:
            return "0"
        def compare(n1, n2):
            if int(n1+n2)>int(n2+n1):
                return -1
            else:
                return 1
        return "".join(sorted(map(str,nums),key=cmp_to_key(compare)))