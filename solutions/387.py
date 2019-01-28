class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = {}
        for c in s:
            try:
                alpha[c] += 1
            except:
                alpha[c] = 1
        for i, c in enumerate(s):
            if alpha[c] == 1:
                return i
        return -1
