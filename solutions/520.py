class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        are_capitals = list(map(is_capital, word))
        if all(are_capitals):
            return True
        if not any(are_capitals):
            return True
        if are_capitals[0] and not any(are_capitals[1:]):
            return True
        return False

def is_capital(c):
    return c >= 'A' and c <= 'Z'