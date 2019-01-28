class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        for i in range(1, len(s)):
            result += roman[s[i]]
            if roman[s[i - 1]] < roman[s[i]]:
                result -= 2 * roman[s[i - 1]]
        return result + roman[s[0]]
