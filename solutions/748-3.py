class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        counter = dict()
        for c in licensePlate.lower():
            if c.isalpha():
                counter[c] = counter.get(c, 0) + 1
        
        best = None
        for word in words:
            copy_counter = copy.copy(counter)
            for c in word:
                if c in copy_counter:
                    copy_counter[c] -= 1
                    if copy_counter[c] == 0:
                        copy_counter.pop(c)
            if not copy_counter and (best is None or len(word) < len(best)):
                    best = word
        return best
