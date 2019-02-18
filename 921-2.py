class Solution:
    def minAddToMakeValid(self, S: 'str') -> 'int':
        count = 0
        the_number_of_needed_left_parenthesis = 0
        for c in S:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    the_number_of_needed_left_parenthesis += 1
                else:
                    count -= 1
        the_number_of_needed_right_parenthesis = count
        return the_number_of_needed_left_parenthesis + the_number_of_needed_right_parenthesis
