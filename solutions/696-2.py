class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = []
        current = s[0]
        count = 0
        for c in s:
            if current == c:
                count += 1
            else:
                group.append(count)
                count = 1
                current = c
        group.append(count)
        
        result = 0
        for i in range(len(group) - 1):
            result += min(group[i], group[i + 1])
        return result