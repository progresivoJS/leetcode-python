class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        left, right = '', ''
        if t.left or t.right:
            left = '(' + self.tree2str(t.left) + ')'
        if t.right:
            right = '(' + self.tree2str(t.right) + ')'
        
        return "{}{}{}".format(t.val, left, right)