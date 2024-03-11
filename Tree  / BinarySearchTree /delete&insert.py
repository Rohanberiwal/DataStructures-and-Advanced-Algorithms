class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def delete_helper(node, key):
            if node is None:
                return None
            
            if key < node.val:
                node.left = delete_helper(node.left, key)
            elif key > node.val:
                node.right = delete_helper(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                min_val = find_min(node.right)
                node.val = min_val
                node.right = delete_helper(node.right, min_val)
            return node
        
        def find_min(node):
            while node.left is not None:
                node = node.left
            return node.val
        
        root = delete_helper(root, key)
        
        def split_forest(node, key):
            if node is None:
                return []
            if node.val == key:
                left_subtree = node.left
                node.left = None
                return [left_subtree, node.right]
            elif key < node.val:
                left_forest = split_forest(node.left, key)
                return [node] + left_forest
            else:
                right_forest = split_forest(node.right, key)
                return [node] + right_forest
        
        return split_forest(root, key)
