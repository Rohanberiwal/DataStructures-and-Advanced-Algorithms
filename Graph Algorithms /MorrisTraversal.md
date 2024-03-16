# Morris Traversal

The Morris Traversal is a method for performing an inorder traversal of a binary tree without using recursion or a stack. It was proposed by J. H. Morris in 1979 as a space-efficient alternative to traditional traversal methods.

## Algorithm Overview

1. **Start**: Begin at the root of the tree.
2. **Traversal**:
   - While the current node is not NULL:
     - If the current node has no left child, visit the current node and move to its right child.
     - If the current node has a left child:
       - Find the rightmost node in the left subtree (the inorder predecessor of the current node).
       - If the rightmost node's right child is NULL, set it to point to the current node and move to the left child of the current node.
       - If the rightmost node's right child is already pointing to the current node, revert its right child to NULL, visit the current node, and move to its right child.

## Features

- **Space Efficiency**: Morris Traversal achieves space efficiency by utilizing the NULL pointers in tree nodes to store temporary information, resulting in a space complexity of O(1).
- **Inorder Traversal**: Morris Traversal performs an inorder traversal of the binary tree, visiting nodes in ascending order of their values.
- **No Recursion or Stack**: Unlike traditional traversal methods, Morris Traversal does not require recursion or an explicit stack to keep track of nodes, making it memory-efficient.

## Considerations

- **Temporary Modification**: Morris Traversal temporarily modifies the structure of the tree during traversal, which may not always be desirable.
- **Preservation of Tree Structure**: The algorithm changes the tree structure by adding temporary pointers, which may not be acceptable in scenarios where the original tree structure needs to be preserved.

## Example

```python
def morris_inorder(root):
    current = root
    while current is not None:
        if current.left is None:
            print(current.val)
            current = current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right
            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print(current.val)
                current = current.right

# Example usage:
# Assuming TreeNode class is defined with attributes val, left, right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

morris_inorder(root)
