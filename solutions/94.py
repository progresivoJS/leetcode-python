# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        inorder = []
        stack = []
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    target = stack.pop()
                    inorder.append(target.val)
                    current = target.right
                else:
                    break
        return inorder
