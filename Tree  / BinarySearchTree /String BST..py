# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:    
        def inorder(root  , listextra)  :
            if root is None :
                return 
            inorder(root.left , listextra)
            listextra.append(root.val)
            inorder(root.right , listextra)
        def func(root):
            if not root:
                return ""
            result = str(root.val)
            if root.left or root.right:
                result += "(" + func(root.left) + ")"
            if root.right:
                result += "(" + func(root.right) + ")"
            return result
        listextra  = []
        inorder(root  , listextra)
        print(listextra)
        print(func(root))
        return str(func(root))
