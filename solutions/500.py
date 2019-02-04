class Solution:
    rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            if self.is_same_row_word(word.lower()):
                result.append(word)
        return result

    def is_same_row_word(self, word):
        if not word:
            return False

        group = -1
        for index, row in enumerate(self.rows):
            if word[0] in row:
                group = index
                break

        for c in word:
            if c not in self.rows[group]:
                return False
        else:
            return True
