class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        stack = []
        score = 0
        for c in S:
            if c == '(':
                stack.append('(')
                opened = True
            elif c == ')':
                if opened:
                    score += pow(2, len(stack)-1)
                    stack.pop()
                    opened = False
                else:
                    stack.pop()
        return score
