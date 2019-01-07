class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        l, r = 0, len(S) - 1
        while l < r:
            while l < r and not S[l].isalpha():
                l += 1
            while l < r and not S[r].isalpha():
                r -= 1
            S[l], S[r] = S[r], S[l]
            l, r = l + 1, r - 1
        return ''.join(S)