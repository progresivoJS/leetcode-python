class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        word_dict = {}
        for word in (A + ' ' + B).split():
            try:
                word_dict[word] += 1
            except KeyError:
                word_dict[word] = 1
        result = []
        for key, value in word_dict.items():
            if value == 1:
                result.append(key)
        return result
