# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        preorder = []
        stack = []
        current = root
        while True:
            if current:
                preorder.append(current.val)
                stack.append(current)
                current = current.left
            else:
                if stack:
                    target = stack.pop()
                    current = target.right
                else:
                    break
        return preorder
