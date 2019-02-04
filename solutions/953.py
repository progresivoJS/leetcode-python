class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        mapper = dict()
        for i, c in enumerate(order):
            mapper[c] = i

        for i in range(len(words)-1):
            pre_word = words[i]
            next_word = words[i+1]
            for j in range(min(len(pre_word), len(next_word))):
                if mapper[pre_word[j]] < mapper[next_word[j]]:
                    break
                elif mapper[pre_word[j]] == mapper[next_word[j]]:
                    continue
                else:
                    return False
            else:
                if len(pre_word) > len(next_word):
                    return False
        return True
