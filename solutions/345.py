class Solution:
    def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s
    s = list(s)
    vowels = set("aeiouAEIOU")
    i, j = 0, len(s) - 1
    while True:
        while s[i] not in vowels:
            i += 1
            if i >= j:
                break
        while s[j] not in vowels:
            j -= 1
            if i >= j:
                break

        if i >= j:
            break
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return ''.join(s)