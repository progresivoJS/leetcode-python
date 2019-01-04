class Solution:
    
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            swap(s, i, j)
            i += 1
            j -= 1
        
        return ''.join(s)

def swap(s, i, j):
    s[i], s[j] = s[j], s[i]