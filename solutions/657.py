class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for move in moves:
            if move is 'U':
                y += 1
            elif move is 'D':
                y -= 1
            elif move is 'L':
                x -= 1
            elif move is 'R':
                x += 1
        return x == 0 and y == 0