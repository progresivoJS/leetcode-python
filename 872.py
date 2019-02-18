# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        return self.inorder_traversal(root1) == self.inorder_traversal(root2)

    def inorder_traversal(self, root):
        result = []
        stack = []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    t = stack.pop()
                    if self.is_leaf(t):
                        result.append(t.val)
                    current = t.right
                else:
                    break
        return result

    def is_leaf(self, node):
        return node.left is None and node.right is None
