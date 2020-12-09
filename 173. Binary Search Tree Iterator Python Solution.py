# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ans=[]
        def helper(root):
            if root is None:
                return
            helper(root.left)
            self.ans.append(root.val)
            helper(root.right)
        helper(root)
        self.i=0
        self.l=len(self.ans)
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.i+=1
        return self.ans[self.i-1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.i!=self.l


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()