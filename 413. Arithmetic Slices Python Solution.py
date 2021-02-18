class Solution:
    def numberOfArithmeticSlices(self, a: List[int]) -> int:
        s=0
        def slices(i):
            if i<2:
                return 0
            ap=0
            if a[i]-a[i-1]==a[i-1]-a[i-2]:
                ap=1+slices(i-1)
                nonlocal s
                s+=ap
            else:
                slices(i-1)
            return ap
        slices(len(a)-1)
        return s