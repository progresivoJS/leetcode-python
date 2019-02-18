class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        self.memo = {}
        result = []
        for i in range(num+1):
            result.append(self.count(i))
        return result
    
    def count(self, num):
        if num <= 1:
            return num
        if num in self.memo:
            return self.memo[num]
        self.memo[num] = self.count(num // 2) + (num % 2)
        return self.memo[num]
