class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        for i in range(0, len(s), 2 * k):
            result.append(''.join(reversed(s[i:i+k])))
            result.append(s[i+k : i+2*k :1])
        print(result)
        return ''.join(result)