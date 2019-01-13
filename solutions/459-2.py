class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for size in range(1, (len(s) // 2) + 1):
            if len(s) % size != 0:
                continue
            i, j = 0, size
            pattern = s[:size]
            while j <= len(s):
                if s[i:j] != pattern:
                    break
                i, j = j, j + size
            if j > len(s):
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPattern('abcabc'))
    print(solution.repeatedSubstringPattern('abcdefg'))
    print(solution.repeatedSubstringPattern('abcabcabc'))
    print(solution.repeatedSubstringPattern('aabaabaabaabaab'))
    print(solution.repeatedSubstringPattern('abac'))