class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        str_list = []
        self.dfs(t, str_list)
        return ''.join(str_list)
        
    def dfs(self, t, str_list):
        if t is None:
            return
        str_list.append(str(t.val))
        if t.left or t.right:
            str_list.append('(')
            self.dfs(t.left, str_list)
            str_list.append(')')
        if t.right:
            str_list.append('(')
            self.dfs(t.right, str_list)
            str_list.append(')')