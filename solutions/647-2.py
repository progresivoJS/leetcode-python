class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        dp = {}
        n = len(s)
        for i in range(n):
            dp[i, i] = True
        for c in range(n):
            for r in range(c):
                if r+1 == c:
                    dp[r, c] = (s[r] == s[c])
                else:
                    dp[r, c] = (s[r] == s[c] and dp[r+1, c-1])
        count = 0
        for _, value in dp.items():
            count += 1 if value else 0
        return count
