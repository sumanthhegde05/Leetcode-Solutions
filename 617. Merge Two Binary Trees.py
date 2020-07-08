# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        root = self.helper(t1,t2)
        return root
    
    def helper(self,t1: TreeNode,t2: TreeNode):
        if t1 is None and t2 is None:
            return
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        else: 
            tmp = TreeNode(t1.val+t2.val)
            tmp.left = self.helper(t1.left,t2.left)
            tmp.right = self.helper(t1.right,t2.right)
        return tmp
