class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ['1']
        for _ in range(n-1):
            s.append(self.say(s[-1]))
        return s[n-1]
    
    def say(self, s):
        assert s is not None
        count = 0
        repeat = ''
        
        res = []
        for c in s:
            if repeat == c:
                count += 1
            else:
                if count != 0:
                    res.append(str(count))
                    res.append(repeat)
                repeat = c
                count = 1
        res.append(str(count))
        res.append(repeat)
        return ''.join(res)