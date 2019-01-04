class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        dic = {}
        for log in logs:
            p = log.find(' ') + 1
            identifier, remain_log = log[:p], log[p:]
            dic[remain_log] = identifier
            
            if remain_log[0].isalpha():
                letter_logs.append(remain_log)
            else:
                digit_logs.append(remain_log)
            
        letter_logs.sort()
        result = []
        for letter_log in letter_logs:
            l = [dic[letter_log], letter_log]
            result.append(''.join(l))
        for digit_log in digit_logs:
            l = [dic[digit_log], digit_log]
            result.append(''.join(l))
        return result