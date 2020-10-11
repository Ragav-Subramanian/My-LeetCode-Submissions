class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda i: i[1])
        res, end = 0, float('-inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res