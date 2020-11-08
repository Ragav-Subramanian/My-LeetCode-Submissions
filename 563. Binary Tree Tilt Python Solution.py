class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0
        self.valueSum(root)
        return self.total_tilt
    def valueSum(self,node):
        if not node:
            return 0
        left_sum = self.valueSum(node.left)
        right_sum = self.valueSum(node.right)
        tilt = abs(left_sum - right_sum)
        self.total_tilt += tilt
        return left_sum + right_sum + node.val
        