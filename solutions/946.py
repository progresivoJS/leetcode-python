class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> 'bool':
        stack = []
        i = 0
        for num in popped:
            while i < len(pushed) and ((not stack) or stack[-1] != num):
                stack.append(pushed[i])
                i += 1
            if stack[-1] == num:
                stack.pop()
            else:
                return False
        return True
