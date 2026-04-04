class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or (x, y) in visited:
                return 0
            
            visited.add((x, y))
            area = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                area += dfs(nx, ny)
            
            return area
        
        for i in range(m):
            for j in range(n):
                max_area = max(max_area, dfs(i, j))
        
        return max_area

