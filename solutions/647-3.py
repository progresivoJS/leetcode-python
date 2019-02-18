class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        n = len(s)
        count = 0
        for i in range(n):
            dp[i][i] = True
        for c in range(n):
            for r in range(c):
                if r+1 == c:
                    dp[r][c] = 1 if s[r] == s[c] else 0
                else:
                    dp[r][c] = 1 if s[r] == s[c] and dp[r+1][c-1] else 0
        return sum([sum(row) for row in dp])
