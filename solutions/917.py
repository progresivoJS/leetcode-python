class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        l, r = 0, len(S) - 1
        
        while l < r:
            while l < len(S) - 1 and not S[l].isalpha():
                l += 1
            while r > 0 and not S[r].isalpha():
                r -= 1
            if l < r:
                S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        
        return ''.join(S)