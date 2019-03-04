class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        count = 0
        score = 0
        for c in S:
            if c == '(':
                count += 1
                opened = True
            elif c == ')':
                if opened:
                    score += pow(2, count-1)
                    count -= 1
                    opened = False
                else:
                    count -= 1
        return score
