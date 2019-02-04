class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        self.r, self.c = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    count += self.sum_adjacent(grid, (i, j))
        return count
    
    def sum_adjacent(self, grid, coord):
        count = 0
        for i, j in self.get_adjacent(coord):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                count += 1
        return count
    
    def get_adjacent(self, coord):
        row, col = coord
        for i in range(4):
            yield row + self.dy[i], col + self.dx[i]
