class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = [int(c) for c in str(int(a) + int(b))]
        carry = 0
        for i in range(len(s)):
            s[-(i+1)] += carry
            carry = 0
            if s[-(i+1)] >= 2:
                carry = 1
                s[-(i+1)] -= 2
        if carry != 0:
            s.insert(0, carry)
        return ''.join([str(c) for c in s])