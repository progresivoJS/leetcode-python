# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def increasingBST(self, root: 'TreeNode') -> 'TreeNode':
        stack = []
        current = root
        prev = None
        ans = None
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    target = stack.pop()
                    target.left = None
                    if prev is not None:
                        prev.right = target
                    else:
                        ans = target
                    prev = target
                    current = target.right
                else:
                    break
        return ans
