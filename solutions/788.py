class Solution:
    dic = {
        '0': '0',
        '1': '1',
        '8': '8',
        '2': '5',
        '5': '2',
        '6': '9',
        '9': '6',
    }
    
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(N):
            if self.is_good_number(i+1):
                count += 1
        return count

    def is_good_number(self, N):
        N = str(N)
        new = []
        for c in N:
            try:
                new.append(self.dic[c])
            except KeyError:
                return False
        new = ''.join(new)
        if int(N) == int(new):
            return False
        return True