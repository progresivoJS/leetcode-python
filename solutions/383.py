class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for c in magazine:
            try:
                dic[c] += 1
            except:
                dic[c] = 1
        for c in ransomNote:
            if dic.get(c) and dic[c] > 0:
                dic[c] -= 1
            else:
                return False
        return True