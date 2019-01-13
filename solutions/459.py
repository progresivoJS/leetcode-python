class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for size in range(1, (len(s) // 2) + 1):
            if len(s) % size != 0:
                continue
            for i in range(len(s)):
                if s[i % size] != s[i]:
                    break
            else:
                return True
        return False