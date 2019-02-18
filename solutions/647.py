class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        self.memo = {}
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    count += 1
        return count
    
    def is_palindrome(self, s, start, end):
        """
        return whether given s[start:end+1] is palindrome
        """
        if start == end:
            return True
        if start + 1 == end:
            return s[start] == s[end]
        
        if (start, end) in self.memo:
            return self.memo[start, end]
        
        if s[start] == s[end]:
            self.memo[start, end] = self.is_palindrome(s, start+1, end-1)
            count += 1
        else:
            self.memo[start, end] = False
        return self.memo[start, end]
