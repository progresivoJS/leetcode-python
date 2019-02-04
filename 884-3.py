class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        word_dict = {}
        for word in (A + ' ' + B).split():
            word_dict[word] = word_dict.get(word, 0) + 1
        return [key for key, value in word_dict.items() if value == 1]
