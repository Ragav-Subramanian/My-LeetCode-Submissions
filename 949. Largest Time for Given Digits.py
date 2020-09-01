#from itertools import permutations
#Above import statement is not neccessary as leetcode by default imports maximum of the packages and functions
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        arr = list(permutations(sorted(A, reverse=True)))
        
        for h1, h2, m1, m2 in arr:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                return '{}{}:{}{}'.format(h1,h2,m1,m2)
        return ''