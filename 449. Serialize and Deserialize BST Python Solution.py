# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.ans=""
        def preorder(root):
            if root is None:
                return
            self.ans+=str(root.val)+" "
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return self.ans
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        root=None
        def insertIntoBST(root,val):
            if root==None:
                root=TreeNode(val)
                return root
            if root.val>val:
                if root.left is None:
                    root.left=TreeNode(val)
                else:
                    root.left=insertIntoBST(root.left,val)
            else:
                if root.right is None:
                    root.right=TreeNode(val)
                else:
                    root.right=insertIntoBST(root.right,val)
            return root
        for i in data.split():
            root=insertIntoBST(root,int(i))
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans