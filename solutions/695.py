class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
    
    
    def dfs(self, grid, row, col):
        count = 1
        grid[row][col] = -1
        for i in range(4):
            new_row = row + self.dy[i]
            new_col = col + self.dx[i]
            if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 1:
                count += self.dfs(grid, new_row, new_col)
        return count

