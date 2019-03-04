class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        marked = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in marked and grid[r][c]):
                return 0
            marked.add((r, c))
            return 1 + area(r+1, c) + area(r, c+1) + area(r-1, c) + area(r, c-1)

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
