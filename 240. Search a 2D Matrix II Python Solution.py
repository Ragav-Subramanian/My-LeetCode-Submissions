class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, cols - 1
        while low<rows and high>=0:
            if matrix[low][high] == target:
                return True
            elif target>matrix[low][high]:
                low+=1
            else:
                high-=1
        return False