class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit = []
        for log in logs:
            if log.split()[1].isalpha():
                letter.append(log)
            else:
                digit.append(log)
            
        letter.sort(key = lambda x: x[x.find(' ') + 1:])
        result = []
        for log in letter:
            result.append(log)
        for log in digit:
            result.append(log)
        return result