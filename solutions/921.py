class Solution:
    def minAddToMakeValid(self, S: 'str') -> 'int':
        stack = []
        the_number_of_needed_left_parenthesis = 0
        for c in S:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    the_number_of_needed_left_parenthesis += 1
                else:
                    stack.pop()
        the_number_of_needed_right_parenthesis = len(stack)
        return the_number_of_needed_left_parenthesis + the_number_of_needed_right_parenthesis
