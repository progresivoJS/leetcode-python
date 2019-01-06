class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        result = []
        for index, word in enumerate(S.split()):
            word = list(word)
            if first in vowels:
                word.append('ma')
            else:
                word = word[1:]
                word.append(first)
                word.append('ma')
            word.append('a'*(index+1))
            result.append(''.join(word))
        return ' '.join(result)